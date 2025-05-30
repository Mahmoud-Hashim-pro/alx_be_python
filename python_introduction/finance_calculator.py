# Prompt user for financial input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings with 5% annual interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Output results
print("Your monthly savings are $", monthly_savings, ".")
print("Projected savings after one year, with interest, is: $", projected_savings, ".")
