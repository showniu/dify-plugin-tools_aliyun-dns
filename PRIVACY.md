# Privacy Policy / 隐私政策

## English

### Data Collection

This plugin (Aliyun DNS) collects and processes the following data solely for the purpose of managing DNS records via the Alibaba Cloud DNS API:

- **Alibaba Cloud AccessKey ID and AccessKey Secret**: Provided by you when configuring the plugin. These credentials are stored securely by the Dify platform (the Secret is stored as an encrypted `secret-input` field) and are only used to authenticate API requests to `alidns.aliyuncs.com`.
- **Domain names and DNS record data**: Domain names, hostnames (RR), record types, record values, TTL and related parameters that you provide when invoking the tools. These are transmitted directly to the Alibaba Cloud DNS API to perform the requested operations.

### Data Usage

- All data is used exclusively to call the official Alibaba Cloud DNS API (`alidns.aliyuncs.com`).
- The plugin does **not** store, cache, or persist any credentials or DNS data by itself.
- The plugin does **not** transmit any data to third-party services other than Alibaba Cloud.
- The plugin does **not** collect any telemetry, analytics, or usage statistics.

### Third-Party Services

This plugin interacts with **Alibaba Cloud DNS (Alidns)**. Your use of Alibaba Cloud services is governed by the [Alibaba Cloud Privacy Policy](https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-privacy-policy).

### Security Recommendation

We recommend using a RAM sub-account AccessKey with the minimum required permission policy (`AliyunDNSFullAccess` or `AliyunDNSReadOnlyAccess`) instead of your primary account credentials.

## 中文

### 数据收集

本插件（阿里云 DNS）仅为通过阿里云 DNS API 管理解析记录而收集和处理以下数据：

- **阿里云 AccessKey ID 与 AccessKey Secret**：由您在配置插件时提供。凭证由 Dify 平台安全存储（Secret 以加密的 `secret-input` 形式保存），仅用于对 `alidns.aliyuncs.com` 的 API 请求鉴权。
- **域名与解析记录数据**：您在调用工具时提供的域名、主机记录（RR）、记录类型、记录值、TTL 等参数，将直接传输至阿里云 DNS API 以执行相应操作。

### 数据使用

- 所有数据仅用于调用阿里云官方 DNS API（`alidns.aliyuncs.com`）。
- 本插件自身**不**存储、缓存或持久化任何凭证或 DNS 数据。
- 本插件**不**向阿里云以外的任何第三方服务传输数据。
- 本插件**不**收集任何遥测、分析或使用统计数据。

### 第三方服务

本插件与**阿里云云解析 DNS（Alidns）**交互。您对阿里云服务的使用受[阿里云隐私政策](https://terms.aliyun.com/legal-agreement/terms/privacy_policy_full/20240924133948899/20240924133948899.html)约束。

### 安全建议

建议使用授予最小权限策略（`AliyunDNSFullAccess` 或 `AliyunDNSReadOnlyAccess`）的 RAM 子账号 AccessKey，而非主账号凭证。
