from .core import *
from os import environ

environ["TRACELOOP_METRICS_ENABLED"] = "false"

def init_traceloop():
    try:
        from traceloop.sdk import Traceloop
        Traceloop.init(
            app_name="keywordsai",
            api_endpoint=KEYWORDSAI_BASE_URL,
            api_key=KEYWORDSAI_API_KEY,
        )

    except ImportError as e:
        raise ImportError("Tracing is not enabled, please run `pip install keywordsai-sdk[trace]`")