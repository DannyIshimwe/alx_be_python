def get_user_input(prompt):
    """ Helper function to get user input and convert it to a float """
    return float(input(prompt))

def calculate_monthly_savings(income, expenses):
    """ Calculate monthly savings by subtracting expenses from income """
    monthly_savings = income - expenses
    return monthly_savings

def project_annual_savings(monthly_savings, interest_rate=0.05):
    """ Calculate projected annual savings with compound interest """
    annual_savings = monthly_savings * 12
    projected_savings = annual_savings + (annual_savings * interest_rate)
    return projected_savings

def main():
    # Get user input for financial details
    monthly_income = get_user_input("Enter your monthly income:5000")
    monthly_expenses = get_user_input("Enter your total monthly expenses:4000")

    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Project annual savings with a fixed interest rate
    projected_savings = project_annual_savings(monthly_savings)

    # Output results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

if __name__ == "__main__":
    main()
