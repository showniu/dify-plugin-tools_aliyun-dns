"""
Tool: add_record
Add a new DNS record to a domain on Alibaba Cloud DNS.
"""
from __future__ import annotations

from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from .aliyun_dns_base import build_client
from alibabacloud_alidns20150109 import models as dns_models


class AddRecordTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict,
    ) -> Generator[ToolInvokeMessage, None, None]:
        access_key_id = self.runtime.credentials.get("access_key_id", "")
        access_key_secret = self.runtime.credentials.get("access_key_secret", "")

        domain_name: str = tool_parameters.get("domain_name", "").strip()
        rr: str = tool_parameters.get("rr", "").strip()
        record_type: str = tool_parameters.get("type", "").strip()
        value: str = tool_parameters.get("value", "").strip()
        ttl: int = int(tool_parameters.get("ttl", 600))
        priority: int = int(tool_parameters.get("priority", 10))

        if not domain_name:
            yield self.create_text_message("错误：domain_name 参数不能为空。")
            return
        if not rr:
            yield self.create_text_message("错误：rr（主机记录）参数不能为空。")
            return
        if not record_type:
            yield self.create_text_message("错误：type（记录类型）参数不能为空。")
            return
        if not value:
            yield self.create_text_message("错误：value（记录值）参数不能为空。")
            return

        try:
            client = build_client(access_key_id, access_key_secret)

            request = dns_models.AddDomainRecordRequest(
                domain_name=domain_name,
                rr=rr,
                type=record_type,
                value=value,
                ttl=ttl,
            )
            if record_type == "MX":
                request.priority = priority

            response = client.add_domain_record(request)
            record_id = response.body.record_id

            full_host = f"{rr}.{domain_name}" if rr != "@" else domain_name
            msg = (
                f"✅ DNS 记录添加成功！\n\n"
                f"- **记录 ID**：`{record_id}`\n"
                f"- **域名**：{full_host}\n"
                f"- **类型**：{record_type}\n"
                f"- **记录值**：{value}\n"
                f"- **TTL**：{ttl} 秒\n"
            )
            if record_type == "MX":
                msg += f"- **MX 优先级**：{priority}\n"

            yield self.create_text_message(msg)
            yield self.create_json_message(
                {
                    "record_id": record_id,
                    "domain_name": domain_name,
                    "rr": rr,
                    "type": record_type,
                    "value": value,
                    "ttl": ttl,
                    "priority": priority if record_type == "MX" else None,
                }
            )

        except Exception as e:
            yield self.create_text_message(f"添加 DNS 记录失败：{str(e)}")
