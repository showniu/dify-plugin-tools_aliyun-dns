# 阿里云 DNS Dify 插件

通过阿里云 DNS API 管理域名解析记录的 Dify Tool 插件，支持查询、添加、修改、删除和启停 DNS 解析记录。

## 功能

| 工具 | 说明 |
|------|------|
| `list_records` | 查询域名下的 DNS 解析记录列表，支持按主机记录、类型、记录值筛选 |
| `add_record` | 为域名添加新的 DNS 解析记录 |
| `update_record` | 通过记录 ID 修改已有 DNS 解析记录 |
| `delete_record` | 通过记录 ID 删除 DNS 解析记录 |
| `set_record_status` | 启用或停用 DNS 解析记录（不删除） |

## 目录结构

```
aliyun-dns/
├── manifest.yaml             # 插件主清单
├── requirements.txt          # Python 依赖
├── README.md
├── _assets/
│   └── icon.svg              # 插件图标
├── provider/
│   ├── __init__.py
│   └── aliyun_dns.yaml       # Provider 配置（凭证定义）
└── tools/
    ├── __init__.py
    ├── aliyun_dns_base.py    # 共享工具函数
    ├── list_records.py       # 查询记录
    ├── list_records.yaml
    ├── add_record.py         # 添加记录
    ├── add_record.yaml
    ├── update_record.py      # 修改记录
    ├── update_record.yaml
    ├── delete_record.py      # 删除记录
    ├── delete_record.yaml
    ├── set_record_status.py  # 启停记录
    └── set_record_status.yaml
```

## 前提条件

### 1. 阿里云 AccessKey

需要阿里云账号的 **AccessKey ID** 和 **AccessKey Secret**。

> **推荐使用 RAM 子账号** 并授予最小权限策略：
> - 只读权限：`AliyunDNSReadOnlyAccess`
> - 读写权限：`AliyunDNSFullAccess`

获取地址：[阿里云 RAM 控制台](https://ram.console.aliyun.com/manage/ak)

### 2. Python 依赖

```bash
pip install -r requirements.txt
```

## 安装到 Dify

### 方式一：打包上传

```bash
# 安装 Dify 插件 CLI
pip install dify-plugin-cli

# 打包插件
dify plugin package ./aliyun-dns

# 在 Dify 控制台 -> 插件 -> 安装插件 -> 本地上传，选择生成的 .difypkg 文件
```

### 方式二：本地调试

```bash
# 启动调试服务
dify plugin debug
```

## 使用示例

配置好凭证后，在 Dify 的 Agent 或 Workflow 中可使用以下工具：

### 查询 DNS 记录
```
查询 example.com 域名下所有 A 记录
```

### 添加 DNS 记录
```
为 example.com 添加一条 www 的 A 记录，指向 1.2.3.4，TTL 设为 600 秒
```

### 修改 DNS 记录
```
将记录 ID 为 123456789 的 DNS 记录值改为 5.6.7.8
```

### 删除 DNS 记录
```
删除记录 ID 为 123456789 的 DNS 记录
```

### 启停 DNS 记录
```
停用记录 ID 为 123456789 的 DNS 记录
```

## 支持的记录类型

| 类型 | 说明 |
|------|------|
| A | IPv4 地址解析 |
| AAAA | IPv6 地址解析 |
| CNAME | 别名解析 |
| MX | 邮件服务器记录 |
| TXT | 文本记录（SPF/域名验证等） |
| NS | 名称服务器 |
| SRV | 服务位置记录 |
| CAA | CA 证书授权 |
| REDIRECT_URL | URL 隐性转发 |
| FORWARD_URL | URL 显性转发 |

## 注意事项

- `delete_record` 为不可逆操作，删除前请确认记录 ID 正确
- 修改记录时需提供所有字段（即使未变更）
- MX 记录需额外提供 `priority` 优先级字段（1-50，数值越小优先级越高）
- 建议使用 RAM 子账号并遵循最小权限原则
