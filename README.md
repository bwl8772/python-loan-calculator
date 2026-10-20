# Python Loan Calculator

A command-line Python learning project completed through [Hyperskill's Loan Calculator project](https://hyperskill.org/projects/90). This is the accepted final-stage implementation.

## Requirements

Python 3.6 or newer. Uses only the standard library; no packages to install.

## Run

```bash
python3 loan_calculator.py --help
```

Choose `--type=annuity` or `--type=diff`. Always supply a **positive annual interest rate** as a percentage (for example, `--interest=10` means 10% per year).

- `--principal`: loan amount.
- `--payment`: monthly payment.
- `--periods`: positive integer number of months.
- `--interest`: positive annual percentage rate.

For annuity mode, provide exactly two of principal, payment, and periods; the missing value is calculated. For differentiated mode, provide principal and periods, and omit payment.

### Calculate an annuity payment

```bash
python3 loan_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10
```

```text
Your annuity payment = 21248!
Overpayment = 274880
```

### Calculate the principal

```bash
python3 loan_calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```

```text
Your loan principal = 800019!
Overpayment = 246621
```

### Calculate the repayment time

```bash
python3 loan_calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
```

```text
It will take 2 years to repay this loan!
Overpayment = 52000
```

### Calculate differentiated payments

```bash
python3 loan_calculator.py --type=diff --principal=1000000 --periods=10 --interest=10
```

Prints each month's payment (108334 for month 1, decreasing to 100834 for month 10), followed by `Overpayment = 45837`.

## Validation and rounding

Invalid or unsupported arguments print `Incorrect parameters`. Inputs must be positive and finite; zero-interest loans are not supported. In annuity mode, a supplied payment must exceed the monthly interest charge.

The program uses annual interest divided by 12 to obtain a monthly rate. Calculated monthly payments and repayment periods are rounded up; calculated principal and overpayment use Python's rounding. Overpayment follows the project's simplified formulas.

## Learning scope

This project practices argument parsing, branching, mathematical formulas, and input validation. It is an educational calculator, not a lender quote or financial advice. It does not model fees, changing rates, or an adjusted final payment.
