# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:34:07 2020

@author: Bilin C

MIT OCW
6.0001 Introduction to Computer Science and Programming in Python

Problem Set 1a
"""

months = 0
portion_down_payment = 0.25     # 25% is the down payment

current_savings = 0
r = 0.04                        # 4% investment return rate
#portion_saved = 0.2             # 10% of salary saved each month

total_cost = float(input("What is the total cost of your dream house: "))
while type(total_cost) != float:
    print("Please type a number")
    total_cost = float(input("What is the total cost of your dream house: "))

annual_salary = float(input("What is your annual salary: "))
while type(annual_salary) != float:
    print("Please type a number")
    annual_salary = float(input("What is your annual salary: "))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
while type(annual_salary) != float:
    print("Please type a number")
    annual_salary = float(input("What is your annual salary: "))
    
down_payment = portion_down_payment * total_cost

def buyHouse(totalCost, downPayment, annualSalary):
    # Either use global variables, or send the variables into the function as arguments
    global current_savings, months
    
    print("Let's see how many months you have to save...\n")
    while current_savings < (downPayment):
        
        print(f"Month {months}. Your current savings are: ${current_savings:.2f} \n-------------")
        current_savings += (portion_saved * annualSalary + current_savings * r)/12
        months += 1
    
    print(f"Month {months}. Your current savings are: ${current_savings:.2f} \n-------------")
    return months

print(f"Your house costs: ${total_cost}")
print(f"The down payment is: ${down_payment}")

total_months = buyHouse(total_cost, down_payment, annual_salary)
print(f"It will take you {total_months} months to buy your dream house!")
print(f"Or {(total_months/12):.2f} years.")


