# Privacy Policy

## Data Collection

This plugin (Aliyun DNS) collects and processes the following data solely for the purpose of managing DNS records via the Alibaba Cloud DNS API:

- **Alibaba Cloud AccessKey ID and AccessKey Secret**: Provided by you when authorizing the plugin. These credentials are stored securely by the Dify platform (the Secret is stored as an encrypted `secret-input` field) and are only used to authenticate API requests to `alidns.aliyuncs.com`.
- **Domain names and DNS record data**: Domain names, hostnames (RR), record types, record values, TTL and related parameters that you provide when invoking the tools. These are transmitted directly to the Alibaba Cloud DNS API to perform the requested operations.

## Data Usage

- All data is used exclusively to call the official Alibaba Cloud DNS API (`alidns.aliyuncs.com`).
- The plugin does **not** store, cache, or persist any credentials or DNS data by itself.
- The plugin does **not** transmit any data to third-party services other than Alibaba Cloud.
- The plugin does **not** collect any telemetry, analytics, or usage statistics.
- No personal data is processed beyond what is strictly required to perform the DNS operations you request.

## Third-Party Services

This plugin interacts with **Alibaba Cloud DNS (Alidns)**. Your use of Alibaba Cloud services is governed by the [Alibaba Cloud Privacy Policy](https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-privacy-policy).

## Data Retention

The plugin itself retains no data. Credential storage and lifecycle are fully managed by the Dify platform; removing the plugin authorization deletes the stored credentials from Dify.

## Security Recommendation

We recommend using a RAM sub-account AccessKey with the minimum required permission policy (`AliyunDNSFullAccess`, or `AliyunDNSReadOnlyAccess` for read-only scenarios) instead of your primary account credentials.

## Contact

For privacy-related questions, please open an issue at the source repository: [showniu/dify-plugin-tools_aliyun-dns](https://github.com/showniu/dify-plugin-tools_aliyun-dns/issues).
