#!/usr/bin/env bash
# Cài skill "Văn bản Đảng" vào Antigravity CLI (agy).
#
#   bash install-agy.sh                 # tải bản mới nhất từ GitHub Releases
#   bash install-agy.sh /duong/dan/repo # cài từ bản clone trong máy
#
# Mặc định cài toàn cục vào ~/.gemini/antigravity-cli/skills/
# Đổi chỗ cài: AGY_SKILLS_DIR=/duong/dan bash install-agy.sh
set -euo pipefail

SKILL="van-ban-dang"
DEST="${AGY_SKILLS_DIR:-$HOME/.gemini/antigravity-cli/skills}"
ZIP_URL="https://github.com/alexnguyenhao/skill-van-ban-dang/releases/latest/download/van-ban-dang.zip"
SRC="${1:-}"

command -v unzip >/dev/null || { echo "Thiếu unzip. Cài: sudo apt install unzip" >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

mkdir -p "$DEST"
rm -rf "${DEST:?}/$SKILL"

if [ -n "$SRC" ]; then
  cp -r "$SRC/$SKILL" "$DEST/$SKILL"
else
  echo "Đang tải $ZIP_URL"
  curl -fsSL "$ZIP_URL" -o "$tmp/skill.zip"
  unzip -q "$tmp/skill.zip" -d "$DEST"
fi

# ZIP trên Releases đã có name: van-ban-dang; bản clone trong repo thì chưa.
# agy dùng trường name làm tên slash command nên cần lowercase-kebab-case.
SKILL_MD="$DEST/$SKILL/SKILL.md"
if [ -f "$SKILL_MD" ] && ! grep -q '^name: van-ban-dang$' "$SKILL_MD"; then
  sed -i.bak 's/^name:.*/name: van-ban-dang/' "$SKILL_MD"
  rm -f "$SKILL_MD.bak"
fi

echo "Đã cài: $DEST/$SKILL"
echo "Mở agy, gõ /skills để xem, hoặc /van-ban-dang để gọi trực tiếp."
