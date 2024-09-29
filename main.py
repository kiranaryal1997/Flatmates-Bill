from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

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

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())








