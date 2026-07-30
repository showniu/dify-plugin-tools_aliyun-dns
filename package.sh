#!/usr/bin/env bash
# 打包阿里云 DNS Dify 插件为 .difypkg 文件
# 用法：bash package.sh

set -e

PLUGIN_NAME="aliyun-dns"
OUTPUT="${PLUGIN_NAME}.difypkg"

cd "$(dirname "$0")"

echo "📦 正在打包插件：${PLUGIN_NAME} ..."

# 清理旧包
rm -f "${OUTPUT}"

# 打包（difypkg 本质是 zip；-D 不写入目录条目，否则 Dify 解包时会报 "read provider: is a directory"）
zip -rD "${OUTPUT}" \
  manifest.yaml \
  requirements.txt \
  main.py \
  icon.svg \
  README.md \
  PRIVACY.md \
  readme/ \
  _assets/ \
  provider/ \
  tools/ \
  --exclude "**/__pycache__/*" \
  --exclude "**/*.pyc" \
  --exclude "**/.DS_Store"

echo "✅ 打包完成：$(pwd)/${OUTPUT}"
echo "📁 文件大小：$(du -sh ${OUTPUT} | cut -f1)"
echo ""
echo "👉 下一步：在 Dify 控制台 -> 插件 -> 安装插件 -> 本地上传，选择该文件"
