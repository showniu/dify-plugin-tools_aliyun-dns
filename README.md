# Aliyun DNS Plugin for Dify

A Dify tool plugin for managing Alibaba Cloud (Aliyun) DNS records — list, add, update, delete, enable and disable DNS records through the Alibaba Cloud DNS API.

[简体中文](./readme/README_zh_Hans.md)

## Tools

| Tool | Description |
|------|-------------|
| `list_records` | List DNS records of a domain, with optional filters by hostname (RR), record type and value |
| `add_record` | Add a new DNS record to a domain |
| `update_record` | Update an existing DNS record by its Record ID |
| `delete_record` | Delete a DNS record by its Record ID |
| `set_record_status` | Enable or disable a DNS record without deleting it |

## Prerequisites

### Alibaba Cloud AccessKey

You need an **AccessKey ID** and **AccessKey Secret** of an Alibaba Cloud account.

> **A RAM sub-account is strongly recommended**, granted with the minimum required policy:
> - Read-only: `AliyunDNSReadOnlyAccess`
> - Read-write (required for all tools): `AliyunDNSFullAccess`

Create an AccessKey in the [Alibaba Cloud RAM Console](https://ram.console.aliyun.com/manage/ak).

## Installation

1. Install this plugin from the Dify Marketplace, or upload the packaged `.difypkg` file via **Plugins → Install Plugin → Local upload**.
2. Open the plugin authorization dialog and fill in your **AccessKey ID** and **AccessKey Secret**.
3. The plugin validates the credentials by calling the `DescribeDomains` API. If validation fails, check that the key exists, is enabled, and the RAM user has been granted the DNS policy.

## Usage Examples

After authorization, the tools can be used in Dify Agents or Workflows:

- *List records*: "List all A records of example.com"
- *Add record*: "Add an A record `www` for example.com pointing to 1.2.3.4 with TTL 600"
- *Update record*: "Change the value of record 123456789 to 5.6.7.8"
- *Delete record*: "Delete DNS record 123456789"
- *Enable/Disable*: "Disable DNS record 123456789"

## Supported Record Types

| Type | Description |
|------|-------------|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Canonical name (alias) |
| MX | Mail exchange |
| TXT | Text record (SPF / domain verification, etc.) |
| NS | Name server |
| SRV | Service locator |
| CAA | CA authorization |
| REDIRECT_URL | Implicit URL forwarding |
| FORWARD_URL | Explicit URL forwarding |

## Notes

- `delete_record` is irreversible. Always verify the Record ID (via `list_records`) before deleting.
- `update_record` requires all fields to be provided, even if unchanged.
- MX records require an additional `priority` field (1–50; lower value means higher priority).
- Follow the principle of least privilege: use a RAM sub-account instead of your primary account credentials.

## Project Structure

```
aliyun-dns/
├── manifest.yaml             # Plugin manifest
├── requirements.txt          # Python dependencies
├── main.py                   # Plugin entrypoint
├── README.md
├── PRIVACY.md
├── readme/
│   └── README_zh_Hans.md     # Simplified Chinese README
├── _assets/
│   └── icon.svg              # Plugin icon
├── provider/
│   ├── aliyun_dns.yaml       # Provider definition (credentials)
│   └── aliyun_dns.py         # Credential validation
└── tools/
    ├── aliyun_dns_base.py    # Shared SDK helpers
    ├── list_records.py / .yaml
    ├── add_record.py / .yaml
    ├── update_record.py / .yaml
    ├── delete_record.py / .yaml
    └── set_record_status.py / .yaml
```

## License & Source

Source code: [showniu/dify-plugin-tools_aliyun-dns](https://github.com/showniu/dify-plugin-tools_aliyun-dns)

## Privacy

See [PRIVACY.md](./PRIVACY.md).
