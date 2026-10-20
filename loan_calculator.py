import argparse
import math


class LoanParser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)


def duration(periods):
    years, months = divmod(periods, 12)
    parts = []
    if years:
        parts.append(f'{years} year' + ('s' if years != 1 else ''))
    if months:
        parts.append(f'{months} month' + ('s' if months != 1 else ''))
    return ' and '.join(parts)


def main():
    parser = LoanParser()
    parser.add_argument('--type', choices=['annuity', 'diff'], required=True)
    parser.add_argument('--principal', type=float)
    parser.add_argument('--payment', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float, required=True)
    try:
        args = parser.parse_args()
        values = [args.principal, args.payment, args.periods]
        if sum(value is not None for value in values) != 2:
            raise ValueError()
        if any(value is not None and
               (not math.isfinite(value) or value <= 0)
               for value in values + [args.interest]):
            raise ValueError()
        principal, payment, periods = values
        i = args.interest / 1200
        if args.type == 'diff':
            if payment is not None or principal is None or periods is None:
                raise ValueError()
            total = 0
            for month in range(1, periods + 1):
                amount = math.ceil(
                    principal / periods
                    + i * (principal - principal * (month - 1) / periods)
                )
                total += amount
                print(f'Month {month}: payment is {amount}')
        else:
            if payment is None:
                factor = (1 + i) ** periods
                payment = math.ceil(
                    principal * i * factor / (factor - 1)
                )
                print(f'Your annuity payment = {payment}!')
            elif principal is None:
                factor = (1 + i) ** periods
                principal = round(
                    payment * (factor - 1) / (i * factor)
                )
                print(f'Your loan principal = {principal}!')
            else:
                if payment <= i * principal:
                    raise ValueError()
                periods = math.ceil(
                    math.log(payment / (payment - i * principal), 1 + i)
                )
                print(f'It will take {duration(periods)} to repay this loan!')
            total = payment * periods
        print(f'Overpayment = {round(total - principal)}')
    except (ValueError, OverflowError, ZeroDivisionError):
        print('Incorrect parameters')


if __name__ == '__main__':
    main()
