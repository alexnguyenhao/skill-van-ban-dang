#!/usr/bin/env python3
"""
Sinh file .docx văn bản của Đảng đúng thể thức Hướng dẫn 05-HD/VPTW ngày 27/5/2026.

Cài đặt (một lần):
    pip install python-docx

Dùng:
    python tao_docx.py nghi-quyet.json -o "Nghi-quyet-05.docx"
    python tao_docx.py nghi-quyet.json -o out.docx --co-chu 15 --dan-dong 22

Cấu trúc JSON (khoá không bắt buộc có thể bỏ):
{
  "co_quan_cap_tren": "ĐẢNG BỘ TỈNH [...]",   // ô 2, dòng trên (bỏ nếu không có)
  "co_quan": "ĐẢNG UỶ XÃ LỘC HƯNG",            // ô 2, dòng dưới (bắt buộc)
  "so_ky_hieu": "05-NQ/ĐU",                     // ô 3 (bắt buộc), KHÔNG có dấu hai chấm
  "dia_danh": "Lộc Hưng",                       // ô 4
  "ngay": "12", "thang": "01", "nam": "2026",
  "ten_loai": "NGHỊ QUYẾT",                     // ô 5a, bỏ trống nếu là công văn
  "trich_yeu": "về phương hướng, nhiệm vụ năm 2026",
  "cong_van": false,                            // true: trích yếu 12 nghiêng dưới số
  "blocks": [ ... ],                            // ô 6
  "ky": { "quyen_han": "T/M ĐẢNG UỶ", "chuc_vu": "BÍ THƯ", "ho_ten": "Nguyễn Văn A" },
  "noi_nhan": ["Các đồng chí Đảng uỷ viên", "Các chi bộ trực thuộc Đảng uỷ",
               "Lưu Văn phòng Đảng uỷ."],
  "dia_chi": "Địa chỉ: ... - Điện thoại: ... - Email: ..."
}

Các loại block trong "blocks":
  {"t": "p", "text": "...", "align": "justify|center|left|right", "bold": true, "italic": true,
   "indent": 1.0, "size": 14, "space_after": 6, "upper": true}
  {"t": "can-cu", "text": "Căn cứ Điều lệ Đảng;"}      // dòng căn cứ, có gạch đầu dòng tự thêm
  {"t": "heading", "text": "I. MỤC TIÊU, CHỈ TIÊU"}    // in hoa, đậm, canh giữa
  {"t": "muc", "text": "1. Về công tác xây dựng Đảng"} // đậm, canh trái
  {"t": "dieu", "text": "Điều 1. Phạm vi điều chỉnh"}  // đậm, canh trái
  {"t": "chuong", "text": "Chương I\nQUY ĐỊNH CHUNG"}  // canh giữa, đậm
  {"t": "table", "header": true, "widths": [1.5, 6, 4, 3], "rows": [["A","B"], ...]}
  {"t": "pagebreak"}
  "Chuỗi thuần" cũng được hiểu là một đoạn văn căn đều.
"""

from __future__ import annotations

import argparse
import json
import sys

try:
    from docx import Document
    from docx.enum.table import WD_ALIGN_VERTICAL
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Mm, Pt
except ImportError:  # pragma: no cover
    sys.exit("Thiếu thư viện python-docx. Cài bằng: pip install python-docx")

ALIGN = {
    "left": WD_ALIGN_PARAGRAPH.LEFT,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "right": WD_ALIGN_PARAGRAPH.RIGHT,
    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
}


def set_run(run, size, bold=False, italic=False, underline=False):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.underline = underline
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), "Times New Roman")
    return run


def para(container, text="", align="justify", size=14, bold=False, italic=False,
         indent=0.0, space_after=6, space_before=0, underline=False,
         line=20.0, keep_next=False, left_indent=0.0, right_indent=0.0):
    """Đoạn văn. `line` tính bằng pt (dãn dòng Exactly 18-22 pt theo HD 05)."""
    p = container.add_paragraph()
    p.alignment = ALIGN[align]
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = Pt(line)
    if indent:
        pf.first_line_indent = Cm(indent)
    if left_indent:
        pf.left_indent = Cm(left_indent)
    if right_indent:
        pf.right_indent = Cm(right_indent)
    if keep_next:
        pf.keep_with_next = True
    if text:
        set_run(p.add_run(text), size, bold, italic, underline)
    return p


def no_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        el.set(qn("w:sz"), "0")
        borders.append(el)
    tbl_pr.append(borders)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tbl_pr.append(layout)


def zero_cell_margins(table):
    tbl_pr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "0")
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tbl_pr.append(mar)


def set_widths(table, widths_cm):
    table.autofit = False
    for row in table.rows:
        for cell, w in zip(row.cells, widths_cm):
            cell.width = Cm(w)


def cell_para(cell, text="", align="center", size=14, bold=False, italic=False,
              space_after=0, space_before=0, underline=False, first=False, line=16.0):
    p = cell.paragraphs[0] if first and not cell.paragraphs[0].text else cell.add_paragraph()
    p.alignment = ALIGN[align]
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = Pt(line)
    if text:
        set_run(p.add_run(text), size, bold, italic, underline)
    return p


def underline_rule(container, width_cm, cell_width_cm, space_before=0, space_after=0):
    """Đường kẻ nét liền dài đúng `width_cm`, canh giữa trong ô rộng `cell_width_cm`."""
    p = container.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = Pt(1)
    side = max((cell_width_cm - width_cm) / 2, 0)
    pf.left_indent = Cm(side)
    pf.right_indent = Cm(side)
    p_pr = p._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    p_bdr.append(bottom)
    p_pr.append(p_bdr)
    return p


def horizontal_line(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p_pr = p._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    p_bdr.append(bottom)
    p_pr.append(p_bdr)
    return p


def add_page_number(section, size=14):
    """Số trang: giữa trang, cách mép trên 10 mm, không hiện trang 1."""
    section.different_first_page_header_footer = True
    section.header_distance = Mm(7)
    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    set_run(run, size)
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_end)


def build(data, out, co_chu=14, dan_dong=20.0, le_tren=20, le_duoi=20, le_trai=30, le_phai=15):
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(co_chu)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(le_tren)
    section.bottom_margin = Mm(le_duoi)
    section.left_margin = Mm(le_trai)
    section.right_margin = Mm(le_phai)
    add_page_number(section, co_chu)

    text_width_cm = (210 - le_trai - le_phai) / 10
    left_w = round(text_width_cm * 0.53, 2)
    right_w = round(text_width_cm - left_w, 2)

    # ---- Ô 1, 2 ------------------------------------------------------
    head = doc.add_table(rows=1, cols=2)
    no_borders(head)
    zero_cell_margins(head)
    set_widths(head, [left_w, right_w])

    left0, right0 = head.cell(0, 0), head.cell(0, 1)

    # Ô 2: tên cơ quan cấp trên trực tiếp + tên cơ quan ban hành + dấu *
    if data.get("co_quan_cap_tren"):
        cell_para(left0, data["co_quan_cap_tren"].upper(), size=co_chu, first=True)
    cell_para(left0, data["co_quan"].upper(), size=co_chu, bold=True,
              first=not data.get("co_quan_cap_tren"))
    cell_para(left0, "*", size=co_chu, space_after=0)

    # Ô 1: ĐẢNG CỘNG SẢN VIỆT NAM + đường kẻ ngang dài bằng tiêu đề
    cell_para(right0, "ĐẢNG CỘNG SẢN VIỆT NAM", size=15, bold=True, first=True, space_before=2)
    underline_rule(right0, min(7.25, right_w), right_w)
    left0.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    right0.vertical_alignment = WD_ALIGN_VERTICAL.TOP

    # ---- Ô 3 + Ô 4: một dòng, số canh giữa dưới tên cơ quan, ngày canh phải --
    ngay = (f"{data.get('dia_danh', '')}, ngày {data.get('ngay', '')} "
            f"tháng {data.get('thang', '')} năm {data.get('nam', '')}")
    p_so = doc.add_paragraph()
    p_so.paragraph_format.space_before = Pt(6)
    p_so.paragraph_format.space_after = Pt(0)
    p_so.paragraph_format.line_spacing = Pt(18)
    p_so.paragraph_format.tab_stops.add_tab_stop(Cm(left_w / 2), WD_TAB_ALIGNMENT.CENTER)
    p_so.paragraph_format.tab_stops.add_tab_stop(Cm(text_width_cm), WD_TAB_ALIGNMENT.RIGHT)
    set_run(p_so.add_run("\tSố " + data["so_ky_hieu"]), co_chu)
    set_run(p_so.add_run("\t" + ngay), co_chu, italic=True)

    if data.get("cong_van") and data.get("trich_yeu"):
        para(doc, data["trich_yeu"], align="center", size=12, italic=True,
             right_indent=max(text_width_cm - (left_w + 2.5), 0),
             space_before=2, space_after=0, line=16)

    # ---- Ô 5a --------------------------------------------------------
    if data.get("ten_loai"):
        para(doc, data["ten_loai"].upper(), align="center", size=16, bold=True,
             space_before=14, space_after=0, line=dan_dong, keep_next=True)
        if data.get("trich_yeu"):
            para(doc, data["trich_yeu"], align="center", size=15, bold=True,
                 space_after=0, line=dan_dong, keep_next=True)
        para(doc, "-----", align="center", size=14, space_after=10, line=dan_dong)

    # ---- Ô 6 ---------------------------------------------------------
    for block in data.get("blocks", []):
        if isinstance(block, str):
            block = {"t": "p", "text": block}
        kind = block.get("t", "p")
        if kind == "p":
            para(doc, block.get("text", ""),
                 align=block.get("align", "justify"),
                 size=block.get("size", co_chu),
                 bold=block.get("bold", False), italic=block.get("italic", False),
                 indent=block.get("indent", 1.0),
                 space_after=block.get("space_after", 6),
                 space_before=block.get("space_before", 0),
                 line=block.get("line", dan_dong))
        elif kind == "can-cu":
            text = block.get("text", "").lstrip("-").strip()
            para(doc, "- " + text, align="justify", size=co_chu, indent=0.0,
                 space_after=0, line=dan_dong, left_indent=0.0)
        elif kind == "kinh-gui":
            # Khối "Kính gửi:"/"Kính trình:" canh giữa trang, các đơn vị thẳng hàng trái
            items = block.get("items") or []
            label = block.get("label", "Kính gửi:")
            est = max([len(i) for i in items] + [len(label)]) * 0.247
            left = max((text_width_cm - est) / 2, 1.0)
            para(doc, label, align="left", size=co_chu, italic=True, indent=0,
                 left_indent=left, space_after=0, line=dan_dong, keep_next=True)
            for i, item in enumerate(items):
                para(doc, "- " + item, align="left", size=co_chu, indent=0,
                     left_indent=left, line=dan_dong,
                     space_after=6 if i == len(items) - 1 else 0)
        elif kind == "heading":
            para(doc, block["text"].upper(), align="center", size=co_chu, bold=True,
                 space_before=10, space_after=6, line=dan_dong, keep_next=True)
        elif kind == "muc":
            para(doc, block["text"], align="justify", size=co_chu, bold=True,
                 indent=1.0, space_before=4, space_after=4, line=dan_dong, keep_next=True)
        elif kind == "dieu":
            para(doc, block["text"], align="justify", size=co_chu, bold=True,
                 indent=1.0, space_before=6, space_after=4, line=dan_dong, keep_next=True)
        elif kind == "chuong":
            lines = block["text"].split("\n")
            para(doc, lines[0], align="center", size=co_chu, bold=True,
                 space_before=10, space_after=0, line=dan_dong, keep_next=True)
            if len(lines) > 1:
                para(doc, lines[1].upper(), align="center", size=co_chu, bold=True,
                     space_after=8, line=dan_dong, keep_next=True)
        elif kind == "table":
            widths = block.get("widths")
            rows = block["rows"]
            table = doc.add_table(rows=len(rows), cols=len(rows[0]))
            table.style = "Table Grid"
            if widths:
                set_widths(table, widths)
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    cell = table.cell(r, c)
                    p = cell.paragraphs[0]
                    p.alignment = ALIGN["left"] if c == 0 else ALIGN["center"]
                    p.paragraph_format.space_after = Pt(0)
                    p.paragraph_format.line_spacing = Pt(16)
                    set_run(p.add_run(str(value)), co_chu - 1,
                            bold=(r == 0 and block.get("header", True)))
            para(doc, "", space_after=6, line=dan_dong)
        elif kind == "pagebreak":
            doc.add_page_break()

    # ---- Ô 7, 9 ------------------------------------------------------
    para(doc, "", space_after=0, line=dan_dong)

    ky = data.get("ky", {})
    noi_nhan = data.get("noi_nhan") or []
    tail = doc.add_table(rows=1, cols=2)
    no_borders(tail)
    zero_cell_margins(tail)
    set_widths(tail, [round(text_width_cm * 0.54, 2), round(text_width_cm * 0.46, 2)])
    left_cell, right_cell = tail.cell(0, 0), tail.cell(0, 1)
    left_cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    right_cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP

    if noi_nhan:
        cell_para(left_cell, "Nơi nhận:", align="left", size=co_chu, underline=True, first=True)
        for item in noi_nhan:
            cell_para(left_cell, "- " + item, align="left", size=12, space_after=0, line=16)
    else:
        cell_para(left_cell, "", size=12, first=True)

    if ky.get("quyen_han"):
        cell_para(right_cell, ky["quyen_han"], size=co_chu, bold=True, first=True)
    if ky.get("chuc_vu"):
        cell_para(right_cell, ky["chuc_vu"], size=co_chu,
                  first=not ky.get("quyen_han"))
    for _ in range(3):
        cell_para(right_cell, "", size=co_chu, line=dan_dong)
    cell_para(right_cell, ky.get("ho_ten", ""), size=co_chu, bold=True)

    # ---- Ô 13 --------------------------------------------------------
    if data.get("dia_chi"):
        horizontal_line(doc)
        para(doc, data["dia_chi"], align="left", size=10, indent=0, space_after=0, line=14)
    if data.get("so_ban") or data.get("nguoi_soan"):
        para(doc, data.get("so_ban", ""), align="left", size=11, indent=0,
             space_after=0, line=14)

    doc.core_properties.title = data.get("trich_yeu", "") or data["so_ky_hieu"]
    doc.core_properties.author = data.get("co_quan", "")
    doc.save(out)
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Sinh .docx văn bản của Đảng theo Hướng dẫn 05-HD/VPTW")
    ap.add_argument("json_file")
    ap.add_argument("-o", "--out", default="van-ban-dang.docx")
    ap.add_argument("--co-chu", type=float, default=14, help="cỡ chữ nội dung (14 hoặc 15)")
    ap.add_argument("--dan-dong", type=float, default=20, help="dãn dòng Exactly, pt (18-22)")
    ap.add_argument("--le-tren", type=float, default=20, help="lề trên, mm")
    ap.add_argument("--le-duoi", type=float, default=20, help="lề dưới, mm")
    ap.add_argument("--le-trai", type=float, default=30, help="lề trái, mm")
    ap.add_argument("--le-phai", type=float, default=15, help="lề phải, mm")
    args = ap.parse_args()

    with open(args.json_file, encoding="utf-8") as fh:
        data = json.load(fh)
    if not data.get("co_quan") or not data.get("so_ky_hieu"):
        sys.exit("JSON phải có 'co_quan' và 'so_ky_hieu'")
    if ":" in data["so_ky_hieu"].split("/")[0]:
        sys.exit("Ô 3 của văn bản Đảng KHÔNG có dấu hai chấm: dùng '05-NQ/ĐU', không dùng 'Số: 05-NQ/ĐU'")

    out = build(data, args.out, args.co_chu, args.dan_dong,
                args.le_tren, args.le_duoi, args.le_trai, args.le_phai)
    print(f"Đã tạo: {out}")


if __name__ == "__main__":
    main()
