allowance = 11850

tax_band_1 = 0.20       # Between £0 and £34,500 of the taxable salary you pay 20% income tax
tax_band_2 = 0.40       # Between £34,501 and £150,000 you pay 40% income tax
tax_band_3 = 0.45       # Over £150,000 you pay 45% income tax

# National Insurance Contributions ---  between £680/month(£8,160/year) - £3,750/month(£45,000/year) you pay 12% ---- Above £3,750/month(£45,000) you pay 2%

national_insurance_band_1 = 0.00        # Less than £8,160/year you pay 0% National Insurance
national_insurance_band_2 = 0.12        # Between £8,161/year and £45,000/year you pay 12% National Insurance
national_insurance_band_3 = 0.02        # Above £45,000/year you pay 2% National Insurance

#user_salary = float(input('Please enter your yearly salary to get your tax details and Net take home salary(i.e. 12000): '))
#loan_choice = int(input('Please enter your Repayment plan number (i.e. 1 or 2) : '))


def salary_checker():

    while True:
        try:
            user_salary = int(input('Please enter your yearly salary to get your tax details and Net take home salary(i.e. 12000): '))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_salary
            break

def loan_choice_checker():
    while True:
        try:
            loan_choice = int(input('Choose a student loan repayment plan. Choose 1 for Plan 1, choose 2 for Plan 2, or choose 3 if you don\'t have a loan (i.e. 1 , 2 or 3) : '))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if not 1 <= loan_choice <= 3:
                print("Not a valid choice! Please type 1, 2 or 3.")
                continue
            else:
                return loan_choice
                break

user_salary= salary_checker()
loan_choice = loan_choice_checker()


#Student loan repayment plan 1 up to £17,775 per year you pay nothing abobe £17,750 you pay 9%

student_loan_band_1 = 0.00              # Below £17,775 you pay 0% repayment on your student loan
student_loan_band_2 = 0.09              # £17,776 and above you pay 9% back on your student loan repayment
student_payment_threshold = 0

if loan_choice == 1:
    student_payment_threshold += 17775
elif loan_choice == 2:
    student_payment_threshold += 21000




taxable_salary = user_salary - allowance

def calculate_NI():
    national_insurance = 0

    if user_salary <= 8160:
        national_insurance += national_insurance_band_1 * user_salary
    elif 8161 <= user_salary <= 45000:
        national_insurance += (national_insurance_band_2 * (user_salary - 8160))
    elif user_salary >= 45001:
        national_insurance += (national_insurance_band_2 * (45000 - 8160)) + ((user_salary - 45000) * national_insurance_band_3)
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

student_loan_print_statement = ''
if loan_choice != 3:
    student_loan_print_statement += ' \n\n\nYearly Student Loan Repayment -->  %.2f    Monthly Student Loan Repayment -->  %.2f' % (yearly_SL,monthly_SL)

print("""Your Income details are as follows:\n\n Net Yearly Income -->  %.2f    Net Monthly Income -->  %.2f\n\n\nYearly Income Tax -->  %.2f    Monthly Income Tax -->  %.2f\n\n\n
Yearly NI Contributions -->  %.2f    Monthly NI Contributions -->  %.2f
""" % (net_income_yearly,net_income_monthly,yearly_tax,monthly_tax,yearly_NI,monthly_NI) + student_loan_print_statement)
