from tkinter import *

allowance = 11850

tax_band_1 = 0.20       # Between £0 and £34,500 of the taxable salary you pay 20% income tax
tax_band_2 = 0.40       # Between £34,501 and £150,000 you pay 40% income tax
tax_band_3 = 0.45       # Over £150,000 you pay 45% income tax

# National Insurance Contributions ---  between £702/month(£8,424/year) - £3,863/month(£46,350/year) you pay 12% ---- Above £3,863/month(£46,350) you pay 2%

national_insurance_band_1 = 0.00        # Less than £8,424/year you pay 0% National Insurance
national_insurance_band_2 = 0.12        # Between £8,425/year and £46,350/year you pay 12% National Insurance
national_insurance_band_3 = 0.02        # Above £46,350/year you pay 2% National Insurance


def clear_input(event):
    user_pay.delete(0, "end")



root = Tk()

h1_tag = Label(root,text="Permanent salary tax calculator",font="Helvetica 18 bold").grid(column=0,pady=20)
Label(root,text="Yearly salary (i.e. 25000 )",font="Helvetica 12").grid(row=1,column=0,sticky=W,padx=4)
user_pay = Entry(root)
user_pay.bind('<Button-1>',clear_input)
user_pay.grid(row=1, column=1, sticky=W,pady=4)
Label(root,text="Which of the following do you fall under?",font="Helvetica 12").grid(row=9,column=0,sticky=W,padx=4,pady=4)
loan_choice_input = IntVar(value=1)
Radiobutton(root, text="Student loan Plan 1 (Course started BEFORE September 1st 2012)",font="Helvetica 10", variable=loan_choice_input, value=1).grid(row=10, column=0,sticky=W)
Radiobutton(root, text="Student loan Plan 2 (Course started AFTER September 1st 2012)",font="Helvetica 10", variable=loan_choice_input, value=2).grid(row=11, column=0,sticky=W)
Radiobutton(root, text="I do not have a student loan",font="Helvetica 10", variable=loan_choice_input, value=3).grid(row=12, column=0, sticky=W)

def main_function(event):

    def salary_checker():
        if not user_pay.get():
            user_pay.delete(0,"end")
            user_pay.insert(0,'This field is empty!')
        elif not float(user_pay.get()):
            user_pay.delete(0,"end")
            user_pay.insert(0,'This is not a valid number!')
        else:
            return int(user_pay.get())



    user_salary= salary_checker()
    loan_choice = int(loan_choice_input.get())


    #Student loan repayment plan 1 up to £18,330 per year you pay nothing abobe £18,330 you pay 9%
    #Student loan repayment plan 2 up to £25,000 per year you pay nothing abobe £25,000 you pay 9%

    student_loan_band_1 = 0.00              # Below £18,330 you pay 0% repayment on your student loan plan 1 and you on student plan 2 you pay 0% below £25,000
    student_loan_band_2 = 0.09              # Above £18,330 you pay 9% repayment on your student loan plan 1 and you on student plan 2 you pay 9% above £25,000
    student_payment_threshold = 0

    if loan_choice == 1:
        student_payment_threshold += 18330
    elif loan_choice == 2:
        student_payment_threshold += 25000




    taxable_salary = user_salary - allowance

    def calculate_NI():
        national_insurance = 0

        if user_salary <= 8424:
            national_insurance += national_insurance_band_1 * user_salary
        elif 8424 < user_salary <= 46350:
            national_insurance += (national_insurance_band_2 * (user_salary - 8424))
        elif user_salary > 46350:
            national_insurance += (national_insurance_band_2 * (46350 - 8424)) + ((user_salary - 46350) * national_insurance_band_3)
        return national_insurance


    def calculate_tax():
        income_tax = 0

        if  taxable_salary <= 34500:
            income_tax += tax_band_1 * taxable_salary
        elif 34501 <= taxable_salary <= 150000:
            income_tax += ((34500 * tax_band_1)) + ((taxable_salary - 35000) * tax_band_2)
        elif taxable_salary >= 150000:
            income_tax += (34500 * tax_band_1) + ((150000- 34500) * tax_band_2) + ((taxable_salary - 150000) * tax_band_3)
        return income_tax

    def calculate_student_loan():
        student_loan = 0
        if loan_choice == 3:
            return 0
        else:
            if user_salary <= student_payment_threshold:
                student_loan += user_salary * student_loan_band_1
            elif user_salary >= (student_payment_threshold + 1):
                student_loan += (user_salary - student_payment_threshold) * student_loan_band_2
            return student_loan

    net_income_yearly = user_salary - (calculate_NI() + calculate_tax() + calculate_student_loan())
    net_income_monthly = net_income_yearly/12

    yearly_tax = calculate_tax()
    monthly_tax = yearly_tax/12

    yearly_NI = calculate_NI()
    monthly_NI = yearly_NI/12

    yearly_SL = calculate_student_loan()
    monthly_SL = yearly_SL/12


    print_statement = ''
    if loan_choice != 3:
        print_statement += """Your Income details are as follows:\n\nNet Yearly Income -->  £%.2f    Net Monthly Income -->  £%.2f\n\n\nYearly Income Tax -->  £%.2f    Monthly Income Tax -->  £%.2f\n\n\nYearly NI Contributions -->  £%.2f    Monthly NI Contributions -->  £%.2f \n\n\nYearly Student Loan Repayment -->  £%.2f    Monthly Student Loan Repayment -->  £%.2f
        """ % (net_income_yearly,net_income_monthly,yearly_tax,monthly_tax,yearly_NI,monthly_NI,yearly_SL,monthly_SL)
    else:
        print_statement += """Your Income details are as follows:\n\nNet Yearly Income -->  £%.2f    Net Monthly Income -->  £%.2f\n\n\nYearly Income Tax -->  £%.2f    Monthly Income Tax -->  £%.2f\n\n\nYearly NI Contributions -->  £%.2f    Monthly NI Contributions -->  £%.2f
        """ % (net_income_yearly,net_income_monthly,yearly_tax,monthly_tax,yearly_NI,monthly_NI)

    def final_output():
        result_box.delete(1.0,"end")
        result_box.insert(1.0,print_statement)

    final_output()


get_salary = Button(text="Get Net Salary", fg="white",bg="purple",font="Helvetica 12")
get_salary.bind("<Button-1>",main_function)
get_salary.grid(row=14,column=1,sticky=E,padx=4)

result_box = Text(root,height=80,width=120)
result_box.grid(row=18,sticky=W)
root.mainloop()
