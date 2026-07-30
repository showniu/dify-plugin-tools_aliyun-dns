"""
Aliyun DNS base helper: wraps alibabacloud-alidns20150109 SDK calls
and provides shared utilities for all tool implementations.
"""
from __future__ import annotations

from typing import Any

from alibabacloud_alidns20150109 import models as dns_models
from alibabacloud_alidns20150109.client import Client as AlidnsClient
from alibabacloud_tea_openapi import models as open_api_models


def build_client(access_key_id: str, access_key_secret: str) -> AlidnsClient:
    """Create an authenticated Alibaba Cloud DNS client."""
    config = open_api_models.Config(
        access_key_id=access_key_id.strip(),
        access_key_secret=access_key_secret.strip(),
    )
    config.endpoint = "alidns.aliyuncs.com"
    return AlidnsClient(config)


def format_record(record: Any) -> dict:
    """Convert a SDK record object to a plain dict."""
    return {
        "record_id": getattr(record, "record_id", ""),
        "domain_name": getattr(record, "domain_name", ""),
        "rr": getattr(record, "rr", ""),
        "type": getattr(record, "type", ""),
        "value": getattr(record, "value", ""),
        "ttl": getattr(record, "ttl", 600),
        "priority": getattr(record, "priority", None),
        "status": getattr(record, "status", ""),
        "line": getattr(record, "line", "default"),
        "locked": getattr(record, "locked", False),
        "weight": getattr(record, "weight", None),
    }
