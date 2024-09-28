from fpdf import FPDF
class Bill:
    """
    Object that contains data about a bill such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of a bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        to_pay = bill.amount*weight
        return to_pay


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
        pdf.image(name="home.png", w=60, h=60)

        #Adding the title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Insert period label and the value
        pdf.cell(w=150, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        # # Insert name and due amount of the second flatmate
        pdf.cell(w=150, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1)

        pdf.output(self.filename)


my_bill = Bill(amount=120, period="May, 2024")
pawan = Flatmate(name="Pawan", days_in_house=20)
kiran = Flatmate(name="Kiran", days_in_house=25)

print(f"{pawan.name} pays:", pawan.pays(bill=my_bill, flatmate2=kiran))
print(f"{kiran.name} pays:", kiran.pays(bill=my_bill, flatmate2=pawan))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=pawan, flatmate2=kiran, bill=my_bill)








