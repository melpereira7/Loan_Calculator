import math
import argparse

# write your code here
parser = argparse.ArgumentParser()

parser.add_argument("--type", help="Enter the type of the payment")
parser.add_argument("--payment", help="Enter the monthly payment amount")
parser.add_argument("--principal", help="Enter the loan principal")
parser.add_argument("--periods", help="Enter the number of periods")
parser.add_argument("--interest", help="Enter the loan interest")

args = parser.parse_args()

if args.type == 'annuity':
    if args.principal is None:
        if args.payment is not None and args.periods is not None and args.interest is not None:
            a = float(args.payment)
            n = int(args.periods)
            i = float(args.interest) / (12 * 100)
            loan_principal = a / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
            print("Your loan principal = ", loan_principal)
            print(f"Overpayment: {(a * n) - loan_principal}")
        else:
            print("Incorrect parameters")
    elif args.periods is None:
        if args.payment is not None and args.principal is not None and args.interest is not None:
            loan = float(args.principal)
            monthly_payment = float(args.payment)
            interest = float(args.interest)
            i = interest / (12 * 100)
            months = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan), 1 + i))
            years = months / 12
            m = months
            if years >= 1:
                months = int((years - int(years)) * 12)
            print(f"It will take ", f"{int(years)} years and " if int(years) >= 1 else "", {months}, "months" if months > 1 else "month",
                  "to repay the loan")
            print(f"Overpayment: {(monthly_payment * m) - loan}")
        else:
            print("Incorrect parameters")
    elif args.payment is None:
        if args.periods is not None and args.principal is not None and args.interest is not None:
            loan = float(args.principal)
            n = float(args.periods)
            i = float(args.interest) / (12 * 100)
            payment = loan * ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
            print(f"Your monthly payment = {math.ceil(payment)}")
            print(f"Overpayment: {(math.ceil(payment) * n) - loan}")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
elif args.type == 'diff':
    if args.payment is None:
        if args.periods is not None and args.principal is not None and args.interest is not None:
            loan = float(args.principal)
            n = int(args.periods)
            i = float(args.interest) / (12 * 100)
            total = 0
            for m in range(1, n + 1):
                d = math.ceil((loan / n) + i * (loan - (loan * (m - 1) / n)))
                total += d
                print(f"Month {m}: payment is {d}")
            print(f"Overpayment: {total - loan}")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
