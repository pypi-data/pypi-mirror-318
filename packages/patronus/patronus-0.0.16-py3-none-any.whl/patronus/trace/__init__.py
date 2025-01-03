import atexit
import json
import random
import traceback
import typing
import functools
import time
import uuid

import opentelemetry
from opentelemetry import trace
from opentelemetry._logs import SeverityNumber
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.trace import TraceFlags

from opentelemetry import _logs
from opentelemetry.sdk import _logs as logs
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.trace.export import BatchSpanProcessor

logger_provider = logs.LoggerProvider()
_logs.set_logger_provider(logger_provider)

app = "non-default"
headers = {"pat-project-name": "Hello", "x-api-key": "sk-FgvQiD_0UgJMPqyuX3TcBnddSI7IBApguZ3VTcg9hvo"}

exporter = OTLPLogExporter(headers=headers)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = logs.LoggingHandler(logger_provider=logger_provider)

texp = OTLPSpanExporter(headers=headers)
tprov = TracerProvider()
tprov.add_span_processor(BatchSpanProcessor(texp))

atexit.register(logger_provider.shutdown)
atexit.register(tprov.shutdown)

# logger = _logs.get_logger("patronus")
logger = logger_provider.get_logger("patronus")
tracer = tprov.get_tracer("patronus")

def jsonify(v: typing.Any):
    try:
        return json.loads(json.dumps(v))
    except TypeError:
        return str(v)


def clean_dict(d: dict):
    if isinstance(d, dict):
        keys_to_delete = []
        for k, v in d.items():
            if v is None:
                keys_to_delete.append(k)
            else:
                clean_dict(v)
        for k in keys_to_delete:
            del d[k]
    if isinstance(d, list):
        for item in d:
            clean_dict(item)


def traced(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__) as span:

            # TODO remove
            time.sleep(random.random()/10)

            attributes = {
                # "pat.app": app,
                "pat.experiment.id": str(uuid.uuid4()),
                "function_name": func.__name__
            }

            span: trace.Span
            span.set_attributes(attributes)
            span_ctx = span.get_span_context()
            ret = None
            exc = None
            exc_info = None
            try:
                ret = func(*args, **kwargs)
            except Exception as e:
                exc = e
                exc_info = traceback.format_exc()

            sev = SeverityNumber.ERROR if exc else SeverityNumber.INFO
            body = {
                "input": {
                    **{f"{i}": jsonify(arg) for i, arg in enumerate(args)},
                    **{k: jsonify(v) for k, v in kwargs.items()},
                },
                "output": jsonify(ret) or {},
            }
            if exc is not None:
                body["exception"] = str(exc)
                body["stack_trace"] = exc_info

            log = logs.LogRecord(
                timestamp=time.time_ns(),
                trace_flags=TraceFlags.SAMPLED,
                trace_id=span_ctx.trace_id,
                span_id=span_ctx.span_id,
                severity_text=sev.name,
                severity_number=sev,
                body=body,
                attributes={"pat.log_type": "function_call", **attributes},
            )
            # print(log.to_json())
            logger.emit(log)

            if exc:
                raise exc
            return ret

    return wrapper