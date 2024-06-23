monthly_income = input("Enter your monthly income: ")
monthly_income = 5000

monthly_expenses = input("Enter your total monthly expenses: ")
monthly_expenses = 4000


monthly_savings = monthly_income - monthly_expenses


interest_rate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)
