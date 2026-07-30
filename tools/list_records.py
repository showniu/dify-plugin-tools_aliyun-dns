"""
Tool: list_records
Query DNS records for a domain on Alibaba Cloud DNS.
"""
from __future__ import annotations

import json
from typing import Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from .aliyun_dns_base import build_client, format_record
from alibabacloud_alidns20150109 import models as dns_models


class ListRecordsTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict,
    ) -> Generator[ToolInvokeMessage, None, None]:
        access_key_id = self.runtime.credentials.get("access_key_id", "")
        access_key_secret = self.runtime.credentials.get("access_key_secret", "")

        domain_name: str = tool_parameters.get("domain_name", "").strip()
        rr_keyword: str = tool_parameters.get("rr_keyword", "").strip() or None
        type_keyword: str = tool_parameters.get("type_keyword", "").strip() or None
        value_keyword: str = tool_parameters.get("value_keyword", "").strip() or None
        page_number: int = int(tool_parameters.get("page_number", 1))
        page_size: int = int(tool_parameters.get("page_size", 20))

        if not domain_name:
            yield self.create_text_message("错误：domain_name 参数不能为空。")
            return

        try:
            client = build_client(access_key_id, access_key_secret)

            request = dns_models.DescribeDomainRecordsRequest(
                domain_name=domain_name,
                page_number=page_number,
                page_size=page_size,
            )
            if rr_keyword:
                request.rrkey_word = rr_keyword
            if type_keyword:
                request.type_key_word = type_keyword
            if value_keyword:
                request.value_key_word = value_keyword

            response = client.describe_domain_records(request)
            body = response.body

            total_count: int = body.total_count or 0
            records_obj = body.domain_records
            record_list = records_obj.record if records_obj and records_obj.record else []

            records = [format_record(r) for r in record_list]

            summary_lines = [
                f"域名：{domain_name}",
                f"总记录数：{total_count}，当前页：{page_number}，每页：{page_size}，本次返回：{len(records)} 条",
            ]
            if records:
                summary_lines.append("")
                summary_lines.append("| 序号 | 记录ID | 主机记录 | 类型 | 记录值 | TTL | 状态 |")
                summary_lines.append("|------|--------|----------|------|--------|-----|------|")
                for i, r in enumerate(records, 1):
                    status_label = "✅ 启用" if r["status"] == "ENABLE" else "⏸ 停用"
                    summary_lines.append(
                        f"| {i} | `{r['record_id']}` | {r['rr']} | {r['type']} "
                        f"| {r['value']} | {r['ttl']}s | {status_label} |"
                    )
            else:
                summary_lines.append("未找到匹配的解析记录。")

            yield self.create_text_message("\n".join(summary_lines))
            yield self.create_json_message(
                {
                    "total_count": total_count,
                    "page_number": page_number,
                    "page_size": page_size,
                    "records": records,
                }
            )

        except Exception as e:
            error_msg = str(e)
            yield self.create_text_message(f"查询 DNS 记录失败：{error_msg}")
