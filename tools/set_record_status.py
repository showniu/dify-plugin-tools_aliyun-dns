"""
Tool: set_record_status
Enable or disable a DNS record on Alibaba Cloud DNS without deleting it.
"""
from __future__ import annotations

from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from .aliyun_dns_base import build_client
from alibabacloud_alidns20150109 import models as dns_models


class SetRecordStatusTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict,
    ) -> Generator[ToolInvokeMessage, None, None]:
        access_key_id = self.runtime.credentials.get("access_key_id", "")
        access_key_secret = self.runtime.credentials.get("access_key_secret", "")

        record_id: str = tool_parameters.get("record_id", "").strip()
        status: str = tool_parameters.get("status", "").strip()

        if not record_id:
            yield self.create_text_message("错误：record_id 参数不能为空。")
            return
        if status not in ("Enable", "Disable"):
            yield self.create_text_message("错误：status 参数必须为 Enable 或 Disable。")
            return

        try:
            client = build_client(access_key_id, access_key_secret)

            request = dns_models.SetDomainRecordStatusRequest(
                record_id=record_id,
                status=status,
            )
            response = client.set_domain_record_status(request)
            resp_record_id = response.body.record_id
            resp_status = response.body.status

            status_label = "✅ 已启用" if resp_status == "ENABLE" else "⏸ 已停用"
            action_label = "启用" if status == "Enable" else "停用"

            msg = (
                f"✅ DNS 记录{action_label}成功！\n\n"
                f"- **记录 ID**：`{resp_record_id}`\n"
                f"- **当前状态**：{status_label}\n"
            )

            yield self.create_text_message(msg)
            yield self.create_json_message(
                {
                    "record_id": resp_record_id,
                    "status": resp_status,
                }
            )

        except Exception as e:
            yield self.create_text_message(f"设置 DNS 记录状态失败：{str(e)}")
