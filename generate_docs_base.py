# -*- coding: utf-8 -*-
"""
Generate complete professional Word documentation for NagrikSetu Skill Development Service (SDS)
following exact formatting and quality of NagrikSetu SWD documentation.
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

OUT_DIR = r"C:\Users\karth\Downloads"

COLOR_NAVY = RGBColor(15, 36, 68)        # #0F2444
COLOR_STEEL = RGBColor(71, 85, 105)      # #475569
COLOR_BODY = RGBColor(30, 41, 59)        # #1E293B
COLOR_MUTED = RGBColor(100, 116, 139)    # #64748B
COLOR_ORANGE = RGBColor(234, 88, 12)     # #EA580C
COLOR_BORDER = "CBD5E1"
COLOR_BG_HEADER = "0F2444"
COLOR_BG_ALT = "F8FAFC"

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_table_borders(table, color="CBD5E1"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def setup_page(doc, title_text):
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)
        sec.page_width = Inches(8.27)
        sec.page_height = Inches(11.69)
        
        # Header
        header = sec.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run(f"NagrikSetu Skill Development Service (SDS) | {title_text}")
        hrun.font.name = "Arial"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = COLOR_MUTED
        
        # Footer
        footer = sec.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        frun1 = fp.add_run("Directorate of Skill Development, Government of Karnataka\t\tPage ")
        frun1.font.name = "Arial"
        frun1.font.size = Pt(8.5)
        frun1.font.color.rgb = COLOR_MUTED
        
        fld_page = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
        fp._p.append(fld_page)
        
        frun2 = fp.add_run(" of ")
        frun2.font.name = "Arial"
        frun2.font.size = Pt(8.5)
        frun2.font.color.rgb = COLOR_MUTED
        
        fld_numpages = parse_xml(r'<w:fldSimple %s w:instr="NUMPAGES"/>' % nsdecls('w'))
        fp._p.append(fld_numpages)

def create_title_page(doc, doc_title, subtitle, doc_ref):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(12)
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_emblem = p_title.add_run("NAGRIKSETU — SKILL DEVELOPMENT SERVICE (SDS)\n")
    run_emblem.font.name = "Arial"
    run_emblem.font.size = Pt(13)
    run_emblem.font.bold = True
    run_emblem.font.color.rgb = COLOR_ORANGE
    
    run_title = p_title.add_run(f"PROJECT REPORT: {doc_title.upper()}\n")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(21)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_NAVY
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(28)
    run_sub = p_sub.add_run(subtitle)
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(11)
    run_sub.font.color.rgb = COLOR_STEEL
    
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(24)
    r_meta = p_meta.add_run(
        "Academic Project Report\n"
        "B.Tech in Computer Science & Engineering / Information Science\n"
        "Second Year Capstone / Systems Engineering Project\n\n"
        "Directorate of Skill Development, Entrepreneurship and Livelihood\n"
        "Government of Karnataka\n"
        "Academic Year: 2025 – 2026\n"
        f"Document Reference: {doc_ref}\n"
        "Submission Status: Verified Final Submission"
    )
    r_meta.font.name = "Arial"
    r_meta.font.size = Pt(10)
    r_meta.font.color.rgb = COLOR_MUTED
    
    doc.add_page_break()

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = COLOR_STEEL
    return p

def add_p(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10)
    run.font.color.rgb = COLOR_BODY
    return p

def add_bullet(doc, title, text=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    run1 = p.add_run(title)
    run1.font.name = "Arial"
    run1.font.size = Pt(10)
    run1.font.bold = True
    run1.font.color.rgb = COLOR_BODY
    if text:
        run2 = p.add_run(f" {text}")
        run2.font.name = "Arial"
        run2.font.size = Pt(10)
        run2.font.color.rgb = COLOR_BODY
    return p

def build_table(doc, headers, data, col_widths=None):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    # Header row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        cell = hdr_cells[i]
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        set_cell_shading(cell, COLOR_BG_HEADER)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(title)
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
    
    # Data rows
    for r_idx, row_data in enumerate(data):
        row = table.rows[r_idx + 1]
        bg_col = COLOR_BG_ALT if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            set_cell_shading(cell, bg_col)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            run = p.add_run(str(val))
            run.font.name = "Arial"
            run.font.size = Pt(9)
            run.font.color.rgb = COLOR_BODY
            
    if col_widths:
        for row in table.rows:
            for idx, w in enumerate(col_widths):
                row.cells[idx].width = Inches(w)
                
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(6)
    return table

print("Generator helper base ready.")
