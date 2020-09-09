import math
import argparse


parser = argparse.ArgumentParser(usage='usege:', description='description:')
parser.add_argument('--type', type=str, help='计算方式')
parser.add_argument('--payment', type=int, help='月付')
parser.add_argument('--principal', type=int, help='本金')
parser.add_argument('--periods', type=int, help='期数')
parser.add_argument('--interest', type=float, help='利率')
args = parser.parse_args()

if args.type == 'annuity':
    if not args.periods and args.principal and args.payment and args.interest:
        P, A, i = args.principal, args.payment, args.interest / 12 / 100
        n = math.ceil(math.log(A / (A - P * i), 1 + i))  # number of payments. Usually, it’s the number of months.
        years, months = n // 12, n % 12
        if years == 0:
            print(f'You need {months} months to repay this credit!')
        elif months == 0:
            print(f'You need {years} year to repay this credit!')
        else:
            print(f'You need {years} years and {months} months to repay this credit!')
        print(f'Overpayment = {n * A - P}')
    if not args.payment and args.principal and args.periods and args.interest:
        P, n, i = args.principal, args.periods, args.interest / 12 / 100
        A = math.ceil(P * i * pow((1 + i), n) / (pow((1 + i), n) - 1))
        print(f'Your annuity payment = {A}!')
        print(f'Overpayment = {n * A - P}')
    if not args.principal and args.payment and args.periods and args.interest:
        A, n, i = args.payment, args.periods, args.interest / 12 / 100
        P = A / (i * pow((1 + i), n) / (pow((1 + i), n) - 1))
        print(f'Your credit principal = {P}!')
        print(f'Overpayment = {n * A - P}')
    else:
        print("Incorrect parameters")
elif args.type == 'diff':
    if not args.payment and args.principal and args.periods and args.interest:
        P, n, i = args.principal, args.periods, args.interest / 12 / 100
        total_payment = 0
        for m in range(n):
            Dm = math.ceil(P / n + i * (P - P * m / n))
            total_payment += Dm
            print(f'Month {m + 1}: payment is {Dm}\n')
            print(f'Overpayment = {total_payment - P}')
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
