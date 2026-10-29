#!/usr/bin/env python3
"""Đóng gói skill thành file ZIP để upload lên Claude (Settings -> Capabilities -> Skills).

Quy tắc của Claude:
  - Gốc ZIP là thư mục skill, không lồng thêm thư mục cha.
  - Tên thư mục trùng với trường `name` trong frontmatter SKILL.md.
  - `name` phải lowercase-kebab-case (a-z, 0-9, dấu gạch nối).

Trong repo, SKILL.md dùng `name: Văn bản Đảng` (để OpenCode hiển thị đẹp),
nên script này ghi lại bản SKILL.md trong ZIP với `name: van-ban-dang`.
Bản trong repo không bị sửa.

Dùng: python build-zip.py  ->  dist/van-ban-dang.zip
"""

from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parent
SKILL_DIR = ROOT / "van-ban-dang"
OUT = ROOT / "dist" / "van-ban-dang.zip"
ZIP_ROOT = "van-ban-dang"

INCLUDE = ["SKILL.md", "references", "assets", "scripts"]
SKIP_SUFFIX = {".pyc"}


def readme_for_skill() -> str:
    """SKILL.md phiên bản Claude: name kebab-case, bỏ qua nếu không có frontmatter."""
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    front, body = text[:end], text[end:]
    front = re.sub(r"(?m)^name:.*$", "name: van-ban-dang", front, count=1)
    return front + body


def add(zf: zipfile.ZipFile, path: Path, arcname: str) -> None:
    if path.is_dir():
        for child in sorted(path.rglob("*")):
            if child.is_file() and child.suffix not in SKIP_SUFFIX:
                add(zf, child, f"{arcname}/{child.relative_to(path).as_posix()}")
        return
    if path.suffix in SKIP_SUFFIX:
        return
    zf.writestr(f"{ZIP_ROOT}/{arcname}", path.read_bytes())


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f"{ZIP_ROOT}/SKILL.md", readme_for_skill())
        for item in INCLUDE[1:]:
            p = SKILL_DIR / item
            if p.exists():
                add(zf, p, item)
    size = OUT.stat().st_size
    print(f"{OUT} ({size / 1024:.0f} KB)")
    with zipfile.ZipFile(OUT) as zf:
        for name in zf.namelist():
            print("  ", name)


if __name__ == "__main__":
    main()
