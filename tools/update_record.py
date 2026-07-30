"""
Tool: update_record
Update an existing DNS record on Alibaba Cloud DNS by RecordId.
"""
from __future__ import annotations

from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from .aliyun_dns_base import build_client
from alibabacloud_alidns20150109 import models as dns_models


class UpdateRecordTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict,
    ) -> Generator[ToolInvokeMessage, None, None]:
        access_key_id = self.runtime.credentials.get("access_key_id", "")
        access_key_secret = self.runtime.credentials.get("access_key_secret", "")

        record_id: str = tool_parameters.get("record_id", "").strip()
        rr: str = tool_parameters.get("rr", "").strip()
        record_type: str = tool_parameters.get("type", "").strip()
        value: str = tool_parameters.get("value", "").strip()
        ttl: int = int(tool_parameters.get("ttl", 600))
        priority: int = int(tool_parameters.get("priority", 10))

        if not record_id:
            yield self.create_text_message("错误：record_id 参数不能为空，请先通过查询接口获取记录 ID。")
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

            request = dns_models.UpdateDomainRecordRequest(
                record_id=record_id,
                rr=rr,
                type=record_type,
                value=value,
                ttl=ttl,
            )
            if record_type == "MX":
                request.priority = priority

            response = client.update_domain_record(request)
            updated_id = response.body.record_id

            msg = (
                f"✅ DNS 记录修改成功！\n\n"
                f"- **记录 ID**：`{updated_id}`\n"
                f"- **主机记录**：{rr}\n"
                f"- **类型**：{record_type}\n"
                f"- **新记录值**：{value}\n"
                f"- **TTL**：{ttl} 秒\n"
            )
            if record_type == "MX":
                msg += f"- **MX 优先级**：{priority}\n"

            yield self.create_text_message(msg)
            yield self.create_json_message(
                {
                    "record_id": updated_id,
                    "rr": rr,
                    "type": record_type,
                    "value": value,
                    "ttl": ttl,
                    "priority": priority if record_type == "MX" else None,
                }
            )

        except Exception as e:
            yield self.create_text_message(f"修改 DNS 记录失败：{str(e)}")
