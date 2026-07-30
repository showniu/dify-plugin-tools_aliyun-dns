from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from alibabacloud_alidns20150109 import models as dns_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109.client import Client as AlidnsClient


class AliyunDnsProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            config = open_api_models.Config(
                access_key_id=str(credentials.get("access_key_id", "")).strip(),
                access_key_secret=str(credentials.get("access_key_secret", "")).strip(),
            )
            config.endpoint = "alidns.aliyuncs.com"
            client = AlidnsClient(config)
            request = dns_models.DescribeDomainsRequest(page_size=1)
            client.describe_domains(request)
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
