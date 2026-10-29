# Dùng skill trên web: ChatGPT, Claude, Gemini và các nền tảng khác

Repo này không chỉ dành cho OpenCode/Claude Code. Dưới đây là cách đưa cùng một bộ quy tắc soạn văn bản
của Đảng vào các chat web, kèm đúng file cần dùng cho từng nơi và cách kiểm tra sau khi cài.

## Chọn nhanh

| Nơi dùng | Cách làm | File |
|---|---|---|
| **Claude web** (claude.ai) | Upload skill dạng ZIP | [`../dist/van-ban-dang.zip`](../dist/van-ban-dang.zip) |
| **Claude Projects** | Instructions + knowledge files | [`../chat-prompt.md`](../chat-prompt.md) + `references/` |
| **ChatGPT Plus/Pro/Team** - Custom Instructions | Dán vào 2 ô: giới thiệu + quy tắc | [`chatgpt-about-you.txt`](chatgpt-about-you.txt) + [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt) |
| **ChatGPT free** - Custom Instructions | Bản rút gọn (1.500 ký tự/ô) | [`chatgpt-about-you.txt`](chatgpt-about-you.txt) + [`chatgpt-instructions-1500.txt`](chatgpt-instructions-1500.txt) |
| **ChatGPT Projects** | Instructions + upload file | [`../chat-prompt.md`](../chat-prompt.md) + `references/` |
| **ChatGPT Custom GPT** | Configure + Knowledge | [`../chat-prompt.md`](../chat-prompt.md) + `references/` |
| **Gemini Gems** | Instructions + file | [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt) |
| **Copilot, Grok, DeepSeek, Qwen...** | Dán đầu cuộc trò chuyện | [`../chat-prompt.md`](../chat-prompt.md) |
| **OpenCode, Claude Code, Antigravity CLI** | Chép thư mục skill vào máy | `../van-ban-dang/` |

Giới hạn thực tế (kiểm tra lại khi nền tảng đổi): Custom Instructions của ChatGPT là **5.000 ký tự** với gói
trả phí, **1.500** với gói free; ChatGPT Projects nhận instructions tới **8.000 ký tự**; Gem/Project của Claude
và Gemini nhận instructions dài hơn nhưng nên dùng bản ngắn rồi bổ sung bằng file.

## Link tải nhanh (mở là thấy nội dung, không cần clone)

- ZIP cho Claude: <https://github.com/alexnguyenhao/skill-van-ban-dang/releases/latest/download/van-ban-dang.zip>
- Instructions 5.000 ký tự: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-dang/main/web/chatgpt-instructions-5000.txt>
- Instructions 1.500 ký tự: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-dang/main/web/chatgpt-instructions-1500.txt>
- Giới thiệu bản thân: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-dang/main/web/chatgpt-about-you.txt>
- Bản đầy đủ dán vào chat: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-dang/main/chat-prompt.md>

---

## 1. Claude trên web (claude.ai) - cách tốt nhất

Claude đọc được cả bộ skill, tự gọi khi thấy việc soạn văn bản, không cần dán prompt mỗi lần.

1. Mở **claude.ai** → đăng nhập.
2. **Settings** (bánh răng góc dưới trái) → **Capabilities** → bật **Code execution and file creation**.
   Không bật mục này thì phần Skills không dùng được (skill cần đọc file và chạy script sinh `.docx`).
3. Vào **Customize** → **Skills** → **Upload skill**.
4. Chọn file `dist/van-ban-dang.zip` (hoặc tải từ
   [Releases](https://github.com/alexnguyenhao/skill-van-ban-dang/releases)).
5. Claude hiện thông tin skill: `van-ban-dang` - Văn bản Đảng. Gạt công tắc sang **On**.
6. Mở chat mới và gõ việc cần làm, Claude tự nạp skill:

   > Viết nghị quyết của Đảng uỷ xã Lộc Hưng về phương hướng, nhiệm vụ năm 2026, Bí thư ký.

**Lưu ý về ZIP:** gốc ZIP phải là thư mục skill (`van-ban-dang/`), tên thư mục trùng trường `name` trong
`SKILL.md` và phải là chữ thường có gạch nối. Trong repo, `SKILL.md` ghi `name: Văn bản Đảng` để OpenCode
hiển thị đẹp; vì vậy **đừng nén thư mục bằng tay** - chạy:

```bash
python build-zip.py     # tạo dist/van-ban-dang.zip với name: van-ban-dang
```

Claude không chạy được script Python nếu chưa bật code execution. Khi cần file Word, yêu cầu thẳng:
*"Xuất văn bản trên thành file .docx theo đúng lề 20/20/30/15 mm, Times New Roman 14, dãn dòng 20 pt"*.

## 2. Claude Projects (bản free cũng có)

1. **Projects** → **New project** → đặt tên "Văn bản Đảng".
2. **Set project instructions** → dán toàn bộ [`../chat-prompt.md`](../chat-prompt.md)
   (7.843 ký tự, dưới giới hạn 8.000).
3. **Add content / Files** → upload các file trong `van-ban-dang/references/`
   (`the-thuc.md`, `the-loai.md`, `quyen-han-ky.md`, `cach-viet.md`, `ngon-ngu.md`, `checklist.md`,
   `so-sanh-nha-nuoc.md`) và 7 file trong `van-ban-dang/assets/`.
4. Trong project, yêu cầu viết văn bản. Claude đọc file đã upload và trả lời theo đúng quy tắc.

## 3. ChatGPT - Custom Instructions (nhanh nhất)

Bản trong repo đã cấu hình sẵn cho **Đảng uỷ xã Lộc Hưng**: ô 2 hai dòng `ĐẢNG BỘ TỈNH [...]` +
`ĐẢNG UỶ XÃ LỘC HƯNG`, ký hiệu `NQ/ĐU`, `KL/ĐU`, `QĐ/ĐU`..., khối ký `T/M ĐẢNG UỶ`, `T/L ĐẢNG UỶ`.
Tên Bí thư, Phó Bí thư, Chánh Văn phòng đang để `[...]` - điền vào file
[`chatgpt-about-you.txt`](chatgpt-about-you.txt) trước khi dán.

1. **Settings** → **Personalization** → **Custom instructions**.
2. Ô thứ nhất ("What should ChatGPT know about you?"): dán [`chatgpt-about-you.txt`](chatgpt-about-you.txt)
   (1.110 ký tự).
3. Ô thứ hai ("How should ChatGPT respond?"):
   - gói Plus/Pro/Team/Enterprise: dán [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt)
     (4.919 ký tự)
   - gói free: dán [`chatgpt-instructions-1500.txt`](chatgpt-instructions-1500.txt) (1.400 ký tự)
4. **Save** → mở chat mới. Custom Instructions áp cho mọi cuộc trò chuyện.

Bản 5.000 ký tự đủ: hỏi trước khi viết, chọn thể loại, 9 thành phần thể thức, quyền hạn ký, nơi nhận,
bố cục từng thể loại, câu mẫu, trình bày, 10 lỗi, định dạng câu trả lời.

## 4. ChatGPT Projects (giữ được cả bộ tài liệu)

1. **ChatGPT** → **Projects** → **New project**.
2. **Project instructions** → dán [`../chat-prompt.md`](../chat-prompt.md) (7.843 ký tự, dưới giới hạn 8.000).
3. **Add files** → upload `references/*.md` + `assets/*.md` (tối đa ~25 file).
4. Chat trong project. Nếu cần file Word: bật **Code interpreter/Canvas** rồi yêu cầu xuất `.docx`.

Project giữ tài liệu giữa các cuộc trò chuyện nên phù hợp khi làm nhiều văn bản trong cùng một đợt
(ví dụ cả bộ hồ sơ đại hội chi bộ).

## 5. ChatGPT Custom GPT (dùng chung cho cả nhóm)

1. **Explore GPTs** → **Create** → tab **Configure**.
2. **Instructions**: dán [`../chat-prompt.md`](../chat-prompt.md).
3. **Knowledge**: upload `references/*.md` và `assets/*.md`.
4. **Capabilities**: bật **Code Interpreter & Data Analysis** để sinh được `.docx`.
5. **Create** → chọn "Only me", "Anyone with a link" hoặc "GPT Store".

Lưu ý: Custom GPT chia sẻ cho người khác thì họ thấy cả file knowledge - không đưa vào đó thông tin nội bộ
chưa công khai.

## 6. Gemini Gems

1. **Gemini** → **Gems** → **New Gem**.
2. Ô instructions: dán [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt) (vừa giới hạn Gem).
3. **Add files** → upload `references/the-thuc.md`, `references/the-loai.md`, `references/quyen-han-ky.md`,
   `references/checklist.md`, `assets/co-quan-mac-dinh.md`.
4. **Save**.
5. Nếu Gem cắt bớt nội dung, dán [`chatgpt-instructions-1500.txt`](chatgpt-instructions-1500.txt) vào ô
   instructions và để các file `references/` gánh phần chi tiết.

## 7. Copilot, Grok, DeepSeek, Qwen và chat khác

Không có chỗ lưu instructions? Dán [`../chat-prompt.md`](../chat-prompt.md) làm tin nhắn đầu tiên, sau đó nêu
yêu cầu. Cách này tốn token mỗi cuộc nhưng dùng được ở mọi nơi, kể cả app điện thoại.

Mẹo giữ ngữ cảnh: dán prompt một lần rồi tiếp tục trong cùng cuộc trò chuyện; đừng mở cuộc mới cho từng văn bản.

## 8. Cài trong máy (OpenCode, Claude Code, Antigravity CLI)

```bash
git clone https://github.com/alexnguyenhao/skill-van-ban-dang.git /tmp/vb-dang
cp -r /tmp/vb-dang/van-ban-dang ~/.config/opencode/skills/     # OpenCode
cp -r /tmp/vb-dang/van-ban-dang ~/.claude/skills/              # Claude Code
bash /tmp/vb-dang/install-agy.sh /tmp/vb-dang                  # Antigravity CLI
```

Bản cài trong máy đọc được toàn bộ `references/`, chạy được `scripts/tao_docx.py` và tự nạp theo mô tả
trong `SKILL.md`.

## Giới hạn ký tự và cách xử lý

| Nơi nhận | Giới hạn | File dùng | Ghi chú |
|---|---|---|---|
| ChatGPT Custom Instructions (trả phí) | 5.000 ký tự/ô | `chatgpt-instructions-5000.txt` (4.919) | tính cả xuống dòng |
| ChatGPT Custom Instructions (free) | 1.500 ký tự/ô | `chatgpt-instructions-1500.txt` (1.400) | |
| ChatGPT Projects | 8.000 ký tự | `chat-prompt.md` (7.843) | thêm file không tính vào đây |
| ChatGPT Custom GPT | 8.000 ký tự | `chat-prompt.md` | Knowledge tối đa ~20 file |
| Claude Project instructions | dài hơn ChatGPT | `chat-prompt.md` | thêm file không tính vào đây |
| Gemini Gem instructions | ô ngắn | `chatgpt-instructions-1500.txt` | thêm file cho phần chi tiết |
| Claude Skill (ZIP) | không giới hạn thực tế | `dist/van-ban-dang.zip` | đọc cả thư mục |

Nếu bị báo vượt ký tự: kiểm tra đã dán đúng bản chưa (5.000 so với 1.500), và nhớ rằng một số trình duyệt
đếm thêm ký tự xuống dòng - các file trong repo đã chừa dung sai cho việc này.

## Câu lệnh mẫu

```
Viết nghị quyết của Đảng uỷ xã Lộc Hưng về phương hướng, nhiệm vụ năm 2026. Bí thư ký.
Căn cứ Điều lệ Đảng và Quy chế làm việc của Ban Chấp hành Đảng bộ xã nhiệm kỳ 2025 - 2030.
```

```
Viết kết luận của Ban Thường vụ Đảng uỷ về công tác chuẩn bị đại hội chi bộ nhiệm kỳ 2027 - 2030,
có phân công người chủ trì và thời hạn hoàn thành từng việc.
```

```
Kiểm tra thể thức văn bản sau và sửa lỗi: [dán văn bản]
```

```
Chuyển nghị quyết này thành file .docx đúng lề 20/20/30/15 mm, Times New Roman 14, dãn dòng 20 pt,
không hiện số trang ở trang đầu.
```

## Kiểm tra sau khi cài

Dán câu này để kiểm tra model đã nhận đúng quy tắc. Câu trả lời đúng phải có: ô 2 hai dòng có dấu `*`,
`Số 05-NQ/ĐU` **không** có dấu hai chấm, `T/M ĐẢNG UỶ`, kết thúc bằng dấu chấm, nơi nhận có
`Lưu Văn phòng Đảng uỷ.`

```
Thử viết giúp tôi dòng số và ký hiệu của một nghị quyết tháng 2 năm 2026 của Đảng uỷ xã,
kèm khối ký của Bí thư và 3 dòng nơi nhận.
```

Nếu model trả về `Số: 05-NQ/ĐU`, `TM. ĐẢNG UỶ` hoặc `./.` thì chưa nhận đúng instructions - kiểm tra lại
bước dán/upload.

## Xử lý sự cố

| Hiện tượng | Nguyên nhân | Cách sửa |
|---|---|---|
| Model vẫn dùng `TM.`, `Số:` có dấu hai chấm | Chưa nạp instructions hoặc nạp bản cũ | Dán lại file trong `web/`, mở chat mới |
| Không thấy mục Skills ở Claude | Chưa bật Code execution | Settings → Capabilities → bật |
| Upload ZIP báo lỗi | ZIP nén tay, có thư mục cha | Chạy `python build-zip.py` rồi upload lại |
| Bị cắt khi dán 5.000 ký tự | Đang dùng gói free | Dùng bản 1.500 ký tự |
| Không xuất được `.docx` | Chưa bật code interpreter/code execution | Bật trong cài đặt, hoặc yêu cầu dán nội dung để tự tạo file |
| Trả lời thiếu chi tiết thể thức | Chỉ dán instructions, chưa upload references | Upload thêm `references/` vào Project/Gem |

## Khác biệt so với bản cài trong máy

| | Bản cài (OpenCode / Claude Code / agy) | Bản web |
|---|---|---|
| Nạp skill | Tự động theo mô tả trong `SKILL.md` | Upload ZIP (Claude) hoặc dán instructions |
| Chạy `tao_docx.py` | Có, tạo file thật đúng lề | Chỉ khi bật code execution / code interpreter |
| Đọc toàn bộ references | Có | Có (Claude ZIP) hoặc chỉ phần đã upload |
| Cập nhật | `git pull` rồi chép lại thư mục | Dán lại file hoặc upload ZIP mới |

Nếu chỉ cần một việc gấp mà không muốn cấu hình: dán `chat-prompt.md` là đủ khoảng 90% chất lượng.
