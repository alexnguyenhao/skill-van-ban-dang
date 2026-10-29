# Cấu hình cơ quan mặc định - Đảng uỷ xã Lộc Hưng

Đây là phần "cấu hình" của skill: mọi văn bản mặc định lấy thông tin trong file này, **không hỏi lại** những gì
đã có ở đây. Khi chuyển sang đơn vị khác, chỉ cần sửa file này (giữ nguyên các file quy tắc).

## 1. Cơ quan ban hành

| Trường | Giá trị |
| --- | --- |
| Ô 2 (dòng trên) | `ĐẢNG BỘ TỈNH [...]` - tên tỉnh, ghi đúng tên gọi chính thức |
| Ô 2 (dòng dưới) | `ĐẢNG UỶ XÃ LỘC HƯNG` |
| Dấu ngăn cách | dấu sao `*` đặt dưới tên cơ quan, phía trên số và ký hiệu |
| Ô 4 | `Lộc Hưng, ngày ... tháng ... năm ...` |
| Ô 13 | Địa chỉ: [...] - Điện thoại: [...] - Email: [...] |

Lý do ô 2 có hai dòng: Hướng dẫn 05-HD/VPTW mục 2.1.2.c quy định văn bản của ban chấp hành đảng bộ, ban thường vụ
đảng uỷ xã, phường, đặc khu **ghi tên đảng bộ cấp trên trực tiếp và tên đảng uỷ ban hành văn bản** (xã trực thuộc
tỉnh theo mô hình chính quyền địa phương 2 cấp).

Văn bản của chi bộ trực thuộc:

```
ĐẢNG UỶ XÃ LỘC HƯNG
CHI BỘ [TÊN CHI BỘ]
*
```

## 2. Số và ký hiệu

Cấu trúc: `Số [số]-[ký hiệu thểloại]/[ký hiệu cơ quan]` - **không có dấu hai chấm sau chữ "Số"**.

| Thể loại | Mẫu | Cơ quan |
| --- | --- | --- |
| Nghị quyết | `Số 05-NQ/ĐU` | Đảng uỷ xã |
| Nghị quyết của Ban Thường vụ | `Số 05-NQ/BTVĐU` | Ban Thường vụ |
| Kết luận | `Số 03-KL/ĐU` | Đảng uỷ xã |
| Quyết định | `Số 07-QĐ/ĐU` | Đảng uỷ xã |
| Quy định | `Số 02-QĐ/ĐU` | Đảng uỷ xã |
| Quy chế | `Số 12-QC/ĐU` | Đảng uỷ xã |
| Chỉ thị | `Số 04-CT/ĐU` | Đảng uỷ xã |
| Hướng dẫn | `Số 09-HD/ĐU` | Đảng uỷ xã |
| Chương trình | `Số 15-CTr/ĐU` | Đảng uỷ xã |
| Kế hoạch | `Số 21-KH/ĐU` | Đảng uỷ xã |
| Báo cáo | `Số 08-BC/ĐU` | Đảng uỷ xã |
| Thông báo | `Số 06-TB/ĐU` | Đảng uỷ xã |
| Tờ trình | `Số 11-TTr/ĐU` | Đảng uỷ xã |
| Công văn | `Số 18-CV/ĐU` | Đảng uỷ xã |
| Biên bản | `Số 02-BB/ĐU` | Đảng uỷ xã |
| Thông tri | `Số 03-TT/ĐU` | Đảng uỷ xã |
| Văn bản của chi bộ | `Số 01-NQ/CB` | Chi bộ |

- Số ghi liên tục từ `01` cho **mỗi tên loại** trong một nhiệm kỳ cấp uỷ; số nhỏ hơn 10 phải thêm `0`.
- Số văn bản mật ghi liên tục cùng số văn bản không mật của cùng tên loại.
- Chưa biết số thì ghi `Số ...-NQ/ĐU`, **không tự bịa số**.

## 3. Người ký mặc định

| Lĩnh vực / loại việc | Người ký | Ô 7a | Ô 7b |
| --- | --- | --- | --- |
| Nghị quyết, kết luận, quy định, quy chế, chỉ thị, chương trình của Đảng uỷ | Bí thư **[...]** | `T/M ĐẢNG UỶ` | `BÍ THƯ` |
| Cùng loại, khi Bí thư vắng, được phân công | Phó Bí thư **[...]** | `T/M ĐẢNG UỶ` | `PHÓ BÍ THƯ` |
| Văn bản của Ban Thường vụ | Bí thư hoặc Phó Bí thư | `T/M BAN THƯỜNG VỤ` | `BÍ THƯ` / `PHÓ BÍ THƯ` |
| Công văn, thông báo, giấy mời, biên bản, xác nhận chữ ký khi được giao | Chánh Văn phòng Đảng uỷ **[...]** | `T/L ĐẢNG UỶ` (hoặc `T/L BAN THƯỜNG VỤ`) | `CHÁNH VĂN PHÒNG` |
| Văn bản của chi bộ | Bí thư chi bộ **[...]** | `T/M CHI BỘ` | `BÍ THƯ` |

- Ô 7a in hoa, 14, đứng, **đậm**; ô 7b in hoa, 14, đứng (không đậm); họ tên in thường, 14, **đậm**.
- Không ghi học hàm, học vị, quân hàm, danh hiệu trước họ tên.
- Không ghi tên cấp uỷ kèm chức vụ người ký (trừ văn bản của ban chỉ đạo, tiểu ban, hội đồng không có dấu riêng
  và văn bản liên cơ quan).

**Cần điền:** họ tên Bí thư, Phó Bí thư, Chánh Văn phòng Đảng uỷ, Bí thư các chi bộ - thay các `[...]` ở trên.

## 4. Khối ký - bản mẫu

```
              T/M ĐẢNG UỶ
                 BÍ THƯ

             Nguyễn Văn A
```

```
           T/M BAN THƯỜNG VỤ
               PHÓ BÍ THƯ

             Nguyễn Văn B
```

```
              T/L ĐẢNG UỶ
            CHÁNH VĂN PHÒNG

             Nguyễn Văn C
```

```
               T/M CHI BỘ
                 BÍ THƯ

             Nguyễn Văn D
```

- Khoảng trống giữa chức vụ và họ tên: 2-3 dòng để ký; dấu đỏ trùm 1/3 chữ ký về bên trái.
- Không dùng `TM.`, `TL.`, `KT.` (có dấu chấm) - đó là cách ghi của văn bản nhà nước.

## 5. Nơi nhận mặc định

```
Nơi nhận:
- Các đồng chí Đảng uỷ viên;
- Các chi bộ trực thuộc Đảng uỷ;
- Lưu Văn phòng Đảng uỷ.
```

- Công văn có `Kính gửi:`, tờ trình có `Kính trình:` → thêm dòng đầu `- Như trên;`
- Văn bản gửi cấp trên: `- Đảng uỷ cấp trên (để báo cáo);` trước dòng `Lưu ...`
- Văn bản gửi các chi bộ: `- Các chi bộ trực thuộc (để thực hiện);`

## 6. Câu mặc định

- `Đảng uỷ xã Lộc Hưng ban hành Nghị quyết về ...`
- `Ban Thường vụ Đảng uỷ xã Lộc Hưng kết luận: ...`
- `Đảng uỷ xã giao Ban Thường vụ, các chi bộ trực thuộc tổ chức thực hiện ...`
- `Giao Văn phòng Đảng uỷ theo dõi, đôn đốc, kiểm tra việc thực hiện và báo cáo Ban Thường vụ trước ngày ...`
- Kết thúc nội dung bằng dấu chấm `.` (không dùng `./.`)

## 7. Khi làm văn bản cho đơn vị khác

Sao file này thành bản riêng, sửa mục 1-6, hoặc nói rõ "lần này viết cho Đảng uỷ xã X" - skill sẽ tạm bỏ cấu hình
mặc định và dùng thông tin người dùng cung cấp.
