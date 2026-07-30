"""
Tool: delete_record
Delete a DNS record from Alibaba Cloud DNS by RecordId.
"""
from __future__ import annotations

from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from .aliyun_dns_base import build_client
from alibabacloud_alidns20150109 import models as dns_models


class DeleteRecordTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict,
    ) -> Generator[ToolInvokeMessage, None, None]:
        access_key_id = self.runtime.credentials.get("access_key_id", "")
        access_key_secret = self.runtime.credentials.get("access_key_secret", "")

        record_id: str = tool_parameters.get("record_id", "").strip()

        if not record_id:
            yield self.create_text_message("错误：record_id 参数不能为空，请先通过查询接口获取记录 ID。")
            return

        try:
            client = build_client(access_key_id, access_key_secret)

            request = dns_models.DeleteDomainRecordRequest(record_id=record_id)
            response = client.delete_domain_record(request)
            deleted_id = response.body.record_id

            msg = (
                f"✅ DNS 记录删除成功！\n\n"
                f"- **已删除记录 ID**：`{deleted_id}`\n\n"
                f"⚠️ 此操作不可撤销，记录已从阿里云 DNS 中永久移除。"
            )

            yield self.create_text_message(msg)
            yield self.create_json_message({"deleted_record_id": deleted_id})

        except Exception as e:
            yield self.create_text_message(f"删除 DNS 记录失败：{str(e)}")
