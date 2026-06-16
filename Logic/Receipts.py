from fpdf import FPDF

class Receipt:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.write_header()
        self.pdf.output("Receipts/test.pdf")

    def write_header(self):
        self.pdf.set_font("Helvetica", "B", 16)
        self.pdf.cell(0, 10, "Crossroads Community Baptist Church", align="C", new_x="LMARGIN", new_y="NEXT")
        self.pdf.set_font("Helvetica", "", 12)
        self.pdf.cell(0, 6, "", new_x="LMARGIN", new_y="NEXT")
        self.pdf.cell(0, 6, "2580 Packard Road, Ann Arbor, MI 48108", new_x="LMARGIN", new_y="NEXT")
        self.pdf.cell(0, 6, "+1 (734) 971-0773", new_x="LMARGIN", new_y="NEXT")

test = Receipt()

