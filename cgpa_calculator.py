from fpdf import FPDF
import os


def gpa_calculate(marks):
    marks = int(marks)
    if marks >= 85:
        return "4.00"
    elif marks >= 80 and marks <= 84:
        return "3.70"
    elif marks >= 75 and marks <= 79:
        return "3.30"
    elif marks >= 70 and marks <= 74:
        return "3.00"
    elif marks >= 65 and marks <= 69:
        return "2.70"
    elif marks >= 61 and marks <= 64:
        return "2.30"
    elif marks >= 58 and marks <= 60:
        return "2.00"
    elif marks >= 55 and marks <= 57:
        return "1.70"
    elif marks >= 50 and marks <= 54:
        return "1.00"
    elif marks < 50:
        return "0.00"
    
def take_data():
    n = int(input("Enter count of your subjects: "))
    data = []
    for i in range(n):
        sub = input(f"Enter your subject {i+1} name: ")
        gpa = input(f"Enter your subject {i+1} marks : ")
        cr = float(input(f"Enter your subject {i+1} credit hours: "))
        gpa = float(gpa_calculate(gpa))
        d = list((sub, cr, gpa))
        data.append(d)
    return data
def total_credit(data):
    sum = 0
    for i in data:
        sum += float(i[1])
    return sum

def Gpa(data):
    sum = 0
    for i in data:
        sum += float(i[1])*float(i[2])
    return sum
def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier","B", size=30)
    pdf.cell(200, 10, txt = "Result Card", ln=1, align="C")
    pdf.set_font("times","B", size = 14)
    pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
    name = input("Enter your name:")
    pdf.cell(100, 10, txt=("Name:                   "+name), ln=1, align="L")
    pdf.cell(100, 10, txt=("Roll No:                "+input("Enter your Roll Number:")), ln=1, align="L")
    sem = input("Enter your semester:")
    pdf.cell(100, 10, txt=("Semester:              "+sem), ln=1, align="L")
    pdf.cell(100, 10, txt=("Department:         "+input("Enter your department name:")), ln=1, align="L")
    pdf.cell(100, 10, txt="", ln=1, align="L")
    pdf.cell(100, 10, txt="", ln=1, align="L")

    headers = ["Subject", "Credit Hrs", "Gpa"]
    data = take_data()

    cell_width = 190 / 3
    cell_height = 10
    font_size = 12
    pdf.set_font('Arial', size=font_size, style='')
    pdf.cell(cell_width, cell_height, txt=headers[0], border=1)
    pdf.cell(cell_width, cell_height, txt=headers[1], border=1)
    pdf.cell(cell_width, cell_height, txt=headers[2], border=1)
    pdf.ln(cell_height)
    pdf.set_font('Arial', size=font_size)
    for row in data:
        for col in row:
            pdf.cell(cell_width, cell_height, txt=str(col), border=1)
        pdf.ln(cell_height)
    if sem == "1":
        gpa = round(Gpa(data)/total_credit(data), 3)
        gpa = str(gpa)[:4]
        cgpa = gpa
    else:
        gpa = round(Gpa(data)/total_credit(data), 3)
        gpa = float(str(gpa)[:4])
        sum = gpa
        for i in range(int(sem)-1):
            sum += float(input(f"Enter your semester {i+1} gpa: "))
        cgpa = round(sum/int(sem), 3)
        cgpa = str(cgpa)[:4]

    pdf.set_font("Courier","I", size=18)
    pdf.cell(100, 10, txt="", ln=1, align="L")
    pdf.cell(100, 10, txt="", ln=1, align="L")

    pdf.cell(100, 10, txt=f"Your Gpa in semester {sem} is {gpa}", ln=1, align="L") 
    pdf.cell(100, 10, txt=f"Your current Cgpa  is {cgpa}", ln=1, align="L")
    name = name+".pdf"
    current_path = os.path.dirname(os.path.abspath(__file__))
    pdf.output(os.path.join(current_path, name))
main()
