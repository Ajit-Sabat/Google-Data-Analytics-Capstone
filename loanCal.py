from amortization.schedule import amortization_schedule
from tabulate import tabulate
import numpy_financial as npf

principle=int(input("Enter Principle: "))
interest_rate=int(input("Enter interest: "))
tenor=int(input("Enter tenor: "))
int_rate=interest_rate/100

monthly_installment =(int_rate/12) * (1/(1-(1+int_rate/12)**(-tenor)))*principle
print("Monthly Installment is : {}.".format(monthly_installment))

table = (x for x in amortization_schedule(principle, int_rate, tenor))
print(
    tabulate(
        table,
        headers=["Number", "Amount", "Interest", "Principal", "Balance"],
        floatfmt=",.2f",
        numalign="right"
    )
)