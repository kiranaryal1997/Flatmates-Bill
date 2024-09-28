import webbrowser
import os

from fpdf import FPDF

class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such
    as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        #Add Icon
        pdf.image(name="files/home.png", w=60, h=60)

        #Adding the title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.set_font(family="Times", size=14, style="B")
        #Insert period label and the value
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=100, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Times", size=14)
        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=40, txt=flatmate1_pay, border=0, ln=1)

        # # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=40, txt=flatmate2_pay, border=0)

        os.chdir("files") #changing the directory to files from Flatemates_Bill
        # pdf.output(f"files/{self.filename}")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
