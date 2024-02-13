def compute_monthly_payment(loan_amount, num_of_years, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    num_of_payments = num_of_years * 12
    
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_of_payments)
    
    return monthly_payment

def main():
    loan_amount = float(input("Enter the loan amount: "))
    num_of_years = int(input("Enter the number of years: "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    

    monthly_payment = compute_monthly_payment(loan_amount, num_of_years, annual_interest_rate)
    
    print("Monthly Payment: $", round(monthly_payment, 2))

if __name__ == "__main__":
    main()
