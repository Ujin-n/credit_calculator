import math
import argparse

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", help="Type of payments")
parser.add_argument("--payment", type=int, help="Monthly payment")
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int, help="The number of months and/or years needed to repay the credit")
parser.add_argument("--interest", type=float)
args = parser.parse_args()

args_num = 0
if args.payment is not None and args.payment > 0:
    args_num += 1
if args.principal is not None and args.principal > 0:
    args_num += 1
if args.periods is not None and args.periods > 0:
    args_num += 1
if args.interest is not None and args.interest > 0:
    args_num += 1

if args_num < 3:
    print("Incorrect parameters")
    exit()

if args.interest is None:
    print("Incorrect parameters")
    exit()

if args.type == "annuity":
    if args.periods is None:
        nom_interest = args.interest / (12 * 100)
        periods_count = math.ceil(
            math.log(args.payment / (args.payment - nom_interest * args.principal), 1 + nom_interest))

        years = periods_count // 12
        months = periods_count % 12

        overpayment = args.payment * periods_count - args.principal

        print((
                  f'You need {years} {"year" if years == 1 else "years"}{" and " if months > 0 else ""}' if years > 0 else '')
              + (f'{months} {"month" if months == 1 else "months"}' if months > 0 else '') + ' to repay this credit!')

        print(f'Overpayment = {overpayment}')

    elif args.payment is None:
        nom_interest = 1 / 12 * args.interest / 100
        annuity_pay = math.ceil(args.principal * ((nom_interest * (1 + nom_interest) ** args.periods) /
                                                  ((1 + nom_interest) ** args.periods - 1)))

        overpayment = annuity_pay * args.periods - args.principal

        print(f'Your annuity payment = {annuity_pay}!')
        print(f'Overpayment = {overpayment}')
    else:
        nom_interest = 1 / 12 * args.interest / 100

        credit_principal = round(args.payment / ((nom_interest * (1 + nom_interest) ** args.periods) /
                                                 ((1 + nom_interest) ** args.periods - 1)))

        overpayment = args.payment * args.periods - credit_principal

        print(f'Your credit principal = {credit_principal}!')
        print(f'Overpayment = {overpayment}')

elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
        exit()

    P = args.principal  # Principal
    n = args.periods  # Number of periods
    interest = args.interest

    i = interest / (12 * 100)  # Nominal interest

    total_payments = 0
    for m in range(1, n + 1):
        D = math.ceil((P / n) + i * (P - (P * (m - 1)) / n))

        print("Month {}: paid out {}".format(m, D))
        total_payments += D

    overpayment = total_payments - P

    print()
    print("Overpayment = {}".format(overpayment))

else:
    print("Incorrect parameters")
    exit()
