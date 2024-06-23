def get_user_input(prompt):
    """ Helper function to get user input and convert it to a float """
    return float(input(prompt))

def calculate_monthly_savings(income, expenses):
    """ Calculate monthly savings by subtracting expenses from income """
    return income - expenses

def project_annual_savings(monthly_savings, interest_rate=0.05):
    """ Calculate projected annual savings with compound interest """
    annual_savings = monthly_savings * 12
    projected_savings = annual_savings + (annual_savings * interest_rate)
    return projected_savings
def main():
    monthly_income = get_user_input("Enter your monthly income: ")
    monthly_expenses = get_user_input("Enter your total monthly expenses: ")

    monthly_savings = calculate_monthly_savings(monthly_income, monthly_expenses)
    projected_savings = project_annual_savings(monthly_savings)
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

if __name__ == "__main__":
    main()
