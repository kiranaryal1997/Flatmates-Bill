import webbrowser
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

        pdf.output(self.filename)
        webbrowser.open(self.filename)

bill_amount = float(input("Hey User, Enter the total bill amount: "))
bill_period = input("Enter the period of the bill: ")
my_bill = Bill(amount=bill_amount, period=bill_period)
fname_flatmate = input("Enter the first flatmate name: ")
fdays_inhouse = int(input(f"Enter the number of days {fname_flatmate} stayed in the house: "))
sname_flatmate = input("Enter the second flatmate name: ")
sdays_inhouse = int(input(f"Enter the number of days {sname_flatmate} stayed in the house: "))

first_flatemate = Flatmate(name=fname_flatmate, days_in_house=fdays_inhouse)
second_flatemate = Flatmate(name=sname_flatmate, days_in_house=sdays_inhouse)

print(f"{first_flatemate.name} pays:", first_flatemate.pays(bill=my_bill, flatmate2=second_flatemate))
print(f"{second_flatemate.name} pays:", second_flatemate.pays(bill=my_bill, flatmate2=first_flatemate))

pdf_report = PdfReport(filename=f"{my_bill.period}.pdf")
pdf_report.generate(flatmate1=first_flatemate, flatmate2=second_flatemate, bill=my_bill)








