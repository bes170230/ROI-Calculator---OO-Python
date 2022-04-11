class ROI():
    def __init__(self):
        self.totalMonthlyIncome = 0
        self.totalMonthlyExpenses = 0
        self.totalMonthlyCashflow = 0
        self.cashoncashROI = 0

    def monthlyIncomeCalc(self):
        rent = int(input("How much is rent? "))
        otherIncome = int(input("How much other income do you receive from tenants? "))
        self.totalMonthlyIncome = rent + otherIncome
        print(f"Your total monthly income is: ${self.totalMonthlyIncome}")

    def monthlyExpensesCalc(self):
        tax = int(input("How much property tax will you have to pay? "))
        insurance = int(input("How much do you pay for insurance? "))
        vacancy = int(input("How much will you pay in case of vacancy? "))
        repairs = int(input("How much are repairs? "))
        capitalExpense = int(input("How much is capital expense? "))
        propertyMgmt = int(input("How much is property management? "))
        mortgage = int(input("What is the monthly mortgage payment? "))
        self.totalMonthlyExpenses = tax + insurance + vacancy + repairs + capitalExpense + propertyMgmt + mortgage
        print(f"Your total monthly expenses are: ${self.totalMonthlyExpenses}")

    def cashflowCalc(self):
        self.totalMonthlyCashflow = self.totalMonthlyIncome - self.totalMonthlyExpenses
        print(f"Your total monthly cash flow is: ${self.totalMonthlyCashflow}")

    def roiCalc(self):
        downPayment = int(input("What was the down payment? "))
        closingCosts = int(input("What were the closing costs? "))
        rehabBudget = int(input("What was the rehab budget? "))
        totalInvestment = downPayment + closingCosts + rehabBudget
        annualCashflow = self.totalMonthlyCashflow * 12
        self.cashoncashROI = (annualCashflow / totalInvestment) * 100
        print(f"Your cash on cash ROI is: {self.cashoncashROI}%")
    
    def summary(self):
        if self.totalMonthlyIncome == 0 or self.totalMonthlyExpenses == 0 or self.totalMonthlyCashflow == 0 or self.cashoncashROI == 0:
            print("You must complete all calculations first!")
        else:
            print(f"Your total monthly income is: ${self.totalMonthlyIncome}")
            print(f"Your total monthly expenses are: ${self.totalMonthlyExpenses}")
            print(f"Your total monthly cash flow is: ${self.totalMonthlyCashflow}")
            print(f"Your cash on cash ROI is: {self.cashoncashROI}%")

home = ROI()

def run():
    while True:
        selection = input("Calculate: 1) Total monthly income, 2) expenses, 3) cashflow, 4) ROI. 5) summary, 6) quit ")
        if selection == "1":
            home.monthlyIncomeCalc()
        elif selection == "2":
            home.monthlyExpensesCalc()
        elif selection == "3":
            home.cashflowCalc()
        elif selection == "4":
            home.roiCalc()
        elif selection == "5":
            home.summary()
        elif selection == "6":
            break
        else:
            print("Not a valid selection. Please select choice 1, 2, 3, 4, 5, or 6")

run()






    

