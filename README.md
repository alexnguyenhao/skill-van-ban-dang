# Skill: Văn bản Đảng (chuẩn Hướng dẫn 05-HD/VPTW)

Skill cho AI soạn thảo **văn bản của Đảng** đúng thể loại, đúng thẩm quyền, đúng thể thức và đúng văn phong.
Nội dung được học trực tiếp từ hai văn bản:

- **Hướng dẫn số 05-HD/VPTW ngày 27/5/2026** của Văn phòng Trung ương Đảng về thể thức và kỹ thuật trình bày
  văn bản của Đảng (36 trang; thay thế Hướng dẫn 36-HD/VPTW ngày 04/3/2018).
- **Quy định số 399-QĐ/TW ngày 09/01/2026** của Ban Bí thư về thể loại, thẩm quyền ban hành và thể thức văn
  bản của Đảng (thay thế Quy định 66-QĐ/TW và Quy định 223-QĐ/TW).

Dùng được cho: nghị quyết, kết luận, quyết định, quy định, quy chế, chỉ thị, hướng dẫn, chương trình,
kế hoạch, báo cáo, thông báo, tờ trình, công văn, biên bản, thông tri của cấp uỷ, ban thường vụ, chi bộ.

**Mặc định của bản này:** cơ quan **Đảng uỷ xã Lộc Hưng**; ô 2 hai dòng `ĐẢNG BỘ TỈNH [...]` +
`ĐẢNG UỶ XÃ LỘC HƯNG`; địa danh `Lộc Hưng`; ký hiệu `NQ/ĐU`, `KL/ĐU`, `QĐ/ĐU`...; khối ký `T/M ĐẢNG UỶ`
(Bí thư, Phó Bí thư) và `T/L ĐẢNG UỶ` (Chánh Văn phòng Đảng uỷ). Tên người ký đang để `[...]`.
Toàn bộ cấu hình nằm trong
[`van-ban-dang/assets/co-quan-mac-dinh.md`](van-ban-dang/assets/co-quan-mac-dinh.md) - đổi cơ quan chỉ cần
sửa file đó.

> Văn bản của UBND, Chủ tịch UBND dùng skill [`van-ban-chinh-phu`](https://github.com/alexnguyenhao/skill-van-ban-chinh-phu).
> Bảng đối chiếu hai hệ thống: `van-ban-dang/references/so-sanh-nha-nuoc.md`.

## Nội dung

```
van-ban-dang/
├── SKILL.md                          # bài học cốt lõi: hỏi trước, 15 thể loại, 9 thành phần, quyền hạn ký, 10 lỗi
├── references/
│   ├── the-thuc.md                   # 9 thành phần bắt buộc + 6 bổ sung, sơ đồ ô 1-15, bảng cỡ chữ, lề, bản sao
│   ├── the-loai.md                   # 25 thể loại, ký hiệu, thẩm quyền cấp xã, bố cục từng thể loại
│   ├── quyen-han-ky.md               # T/M, K/T, T/L, Q., bảng theo cấp, xác nhận chữ ký, biên bản, liên cơ quan
│   ├── cach-viet.md                  # công thức viết từng thể loại, câu mở - câu kết, câu chỉ đạo mẫu
│   ├── ngon-ngu.md                   # văn phong Đảng, viết hoa, viết tắt, từ ngữ cần tránh
│   ├── checklist.md                  # kiểm tra trước khi trình ký (7 nhóm, in ra được)
│   └── so-sanh-nha-nuoc.md           # bảng khác biệt với Nghị định 30/2020/NĐ-CP và lỗi do lẫn hệ thống
├── assets/
│   ├── co-quan-mac-dinh.md           # cấu hình: Đảng uỷ xã Lộc Hưng, số ký hiệu, người ký, khối ký, nơi nhận
│   ├── mau-nghi-quyet.md             # khung nghị quyết
│   ├── mau-ket-luan.md               # khung kết luận
│   ├── mau-quy-che.md                # khung quy định / quy chế
│   ├── mau-bao-cao.md                # khung báo cáo
│   ├── mau-cong-van.md               # khung công văn
│   └── vi-du-nghi-quyet.json         # dữ liệu mẫu chạy được với script sinh .docx
└── scripts/
    └── tao_docx.py                   # sinh .docx đúng A4, lề 20/20/30/15, Times New Roman 14, dãn dòng 20 pt
```

Ngoài thư mục skill, repo còn có: `chat-prompt.md` (bản dán vào chat, 7.843 ký tự), `web/` (hướng dẫn
ChatGPT/Claude/Gemini/Copilot... + bản instructions 5.000 và 1.500 ký tự), `dist/van-ban-dang.zip`
(gói upload Claude), `build-zip.py`, `install-agy.sh`, `index.json` (catalog HTTP cho OpenCode).

## Cài đặt

### OpenCode

```bash
git clone https://github.com/alexnguyenhao/skill-van-ban-dang.git /tmp/vb-dang
mkdir -p ~/.config/opencode/skills
cp -r /tmp/vb-dang/van-ban-dang ~/.config/opencode/skills/
```

Hoặc trỏ vào thư mục repo trong `opencode.json`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["/duong/dan/toi/skill-van-ban-dang"]
}
```

Hoặc dùng như catalog HTTP:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-dang/main/"]
}
```

Sau khi cài, gọi bằng `@van-ban-dang` hoặc nói "viết nghị quyết của Đảng uỷ".

### Claude Code

```bash
cp -r /tmp/vb-dang/van-ban-dang ~/.claude/skills/
```

### Antigravity CLI (agy)

```bash
curl -fsSL https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-dang/main/install-agy.sh | bash
```

Script tải ZIP từ Releases, giải nén vào `~/.gemini/antigravity-cli/skills/van-ban-dang/` và đặt
`name: van-ban-dang` (agy lấy trường này làm tên slash command). Cài từ bản clone:

```bash
bash install-agy.sh /duong/dan/toi/skill-van-ban-dang
```

Trong `agy`: gõ `/skills` để xem skill đã nhận, `/van-ban-dang` để gọi trực tiếp. Chạy một lần không vào TUI:

```bash
agy -p "Viết nghị quyết của Đảng uỷ xã Lộc Hưng về nhiệm vụ năm 2026, Bí thư ký"
```

### Cursor, Codex, Windsurf, Cline và các agent khác

- Clone repo, trỏ agent đọc `van-ban-dang/SKILL.md` khi làm văn bản; hoặc
- Chép nội dung `van-ban-dang/SKILL.md` vào `AGENTS.md` / `.cursor/rules` / system prompt.

### Dùng trên web (ChatGPT, Claude, Gemini)

- **Claude web**: upload [`dist/van-ban-dang.zip`](dist/van-ban-dang.zip) ở Settings → Customize → Skills
  (bật Settings → Capabilities → *Code execution and file creation*).
- **ChatGPT**: dán [`web/chatgpt-about-you.txt`](web/chatgpt-about-you.txt) vào ô 1 và
  [`web/chatgpt-instructions-5000.txt`](web/chatgpt-instructions-5000.txt) vào ô 2 của Custom Instructions
  (bản free dùng [`web/chatgpt-instructions-1500.txt`](web/chatgpt-instructions-1500.txt)); hoặc tạo Project
  rồi upload `chat-prompt.md` + `references/`.
- **Gemini Gems**: dán cùng file instructions, upload thêm `references/`.

Hướng dẫn từng bước cho từng nền tảng, giới hạn ký tự, cách kiểm tra sau khi cài và xử lý sự cố:
xem [`web/README.md`](web/README.md). Dựng lại ZIP sau khi sửa skill: `python build-zip.py`.

Chỉ cần dùng ngay trong một cuộc trò chuyện: dán toàn bộ [`chat-prompt.md`](chat-prompt.md) làm tin nhắn đầu.

## Ví dụ sử dụng

```
@van-ban-dang viết Kết luận của Ban Thường vụ Đảng uỷ về công tác chuẩn bị đại hội chi bộ
nhiệm kỳ 2027 - 2030, phân công 4 việc có chủ trì - thời hạn - sản phẩm.
```

Skill sẽ: hỏi "Làm văn bản gì, ai ký?" → chọn thể loại và số ký hiệu → dựng khối đầu (tiêu đề, tên cơ quan,
số, địa danh ngày tháng) → viết căn cứ, nội dung, tổ chức thực hiện → ráp nơi nhận, thẩm quyền ký → tự chạy
checklist thể thức.

## Sinh file Word

```bash
pip install python-docx
python van-ban-dang/scripts/tao_docx.py \
    van-ban-dang/assets/vi-du-nghi-quyet.json \
    -o "Nghi-quyet-05.docx"
```

Script tự đặt: A4 dọc, lề trên/dưới 20 mm - trái 30 mm - phải 15 mm, Times New Roman 14, dãn dòng Exactly
20 pt, tiêu đề `ĐẢNG CỘNG SẢN VIỆT NAM` 15 đậm có đường kẻ, ô 2 hai dòng + dấu `*`, `Số 05-NQ/ĐU`,
địa danh in nghiêng, tên loại 16 đậm + `-----`, khối ký `T/M`/`T/L`, `Nơi nhận:` 14 gạch chân + danh sách 12,
số trang 14 ở đầu trang và ẩn trang 1. Xem hướng dẫn JSON đầy đủ ở đầu file script.

## Cập nhật

```bash
cd skill-van-ban-dang && git pull
cp -r van-ban-dang/SKILL.md van-ban-dang/references van-ban-dang/assets van-ban-dang/scripts \
      ~/.config/opencode/skills/van-ban-dang/
```

## Nguồn và giới hạn

- Nội dung pháp lý tóm lược từ Hướng dẫn 05-HD/VPTW ngày 27/5/2026 và Quy định 399-QĐ/TW ngày 09/01/2026.
  Hai văn bản này là căn cứ đang áp dụng cho thể thức văn bản của Đảng (đã kiểm chứng năm 2026).
- Trước khi ban hành văn bản có hiệu lực, luôn đối chiếu lại văn bản gốc và quy chế làm việc của cấp uỷ;
  một số quy định riêng của tỉnh uỷ có thể khác về ký hiệu cơ quan.
- Skill hỗ trợ soạn thảo, không thay thế trách nhiệm của người kiểm tra thể thức và người ký văn bản.
- Tên Bí thư, Phó Bí thư, Chánh Văn phòng Đảng uỷ đang để `[...]` - phải điền trước khi dùng thật.

## English

A reusable AI skill for drafting Vietnamese Communist Party documents according to Guidance
05-HD/VPTW (27 May 2026) and Regulation 399-QĐ/TW (9 Jan 2026): document types and issuing authority,
9 mandatory layout components, `Số 05-NQ/ĐU` numbering, `T/M` / `K/T` / `T/L` signing conventions,
recipient block, drafting formulas, a review checklist, and a python-docx generator
(A4, 20/20/30/15 mm margins, Times New Roman 14, exact 20 pt line spacing).
Install by copying `van-ban-dang/` into your agent's skills directory or paste `chat-prompt.md` into any
chat model. For web chat: upload `dist/van-ban-dang.zip` as a Claude skill, or paste the files in `web/`
into ChatGPT Custom Instructions / Projects; see `web/README.md`.

## Giấy phép

MIT - xem [LICENSE](LICENSE).
