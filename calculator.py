#!/usr/bin/env python3
import sys

salary = sys.argv[1]
tax = 0
try:
    ex_salary = int(salary) - 5000
    if ex_salary <3000:
        tax = ex_salary * 0.03
    elif ex_salary < 12000:
        tax = (ex_salary-3000) * 0.10 + 3000*0.03
    elif ex_salary < 25000:
        tax = (ex_salary-12000) * 0.20 + 3000*0.03 + 9000*0.1
    elif ex_salary < 35000:
        tax = (ex_salary-25000) * 0.25 + 3000*0.03 + 9000*0.1 + 13000*0.2
    elif ex_salary < 55000:
        tax = (ex_salary-35000) * 0.35 + 3000*0.03 + 9000*0.1 + 130000*0.2 +10000*0.25 
    elif ex_salary <80000:
        tax = (ex_salary-55000) * 0.45 + 3000*0.03 + 9000*0.1 + 13000*0.2 + 10000*0.25 + 20000*0.35
    else:
        tax = (ex_salary-80000) * 0.45 + 3000*0.03 + 9000*0.1 + 13000*0.2 + 10000*0.25 + 20000*0.35 + 25000 * 0.45
    print('{:.2f}'.format(tax))
except:
    print("Parameter Error")