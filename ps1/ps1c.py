# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:34:07 2020

@author: Bilin C

MIT OCW
6.0001 Introduction to Computer Science and Programming in Python

Problem Set 1c
Find the portion saved so that you can pay the down payment after 36 max_months.
"""


portion_down_payment = 0.25     # 25% is the down payment
                       # 4% investment return rate
# The total cost of a house
total_cost = 1E6 #float(input("What is the total cost of your dream house: "))
# The annual salary
annual_salary = 150000.0 #float(input("What is your annual salary: "))
# The raise rate every 6 month
semi_annual_raise = 1.07 #float(input("Enter your semi annual raise, as a decimal: "))
# Savings should be within 100 dollars
epsilon = 100.0

down_payment = portion_down_payment * total_cost

print(f"Your house costs: ${int(total_cost)}")
print(f"The down payment is: ${int(down_payment)}")
print(f'Your starting annual salary: ${int(annual_salary)}')
# Calculate the savings after 36 month with a certain save rate
def buyHouse(max_months, totalCost, downPayment, annualSalary, semiAnnualRaise, portionSaved):
    # Either use global variables, or send the variables into the function as arguments
    
    current_savings = 0
    r = 0.04
    months = 1
#    print("Let's see how many months you have to save...\n")
    while abs(current_savings - downPayment) >= epsilon and months <= max_months:
        
        current_savings += (portionSaved/10000 * annualSalary + current_savings * r)/12
        
#         print(f"Month {months}. Your current savings are: ${current_savings:.2f} \n-------------")
        
        months += 1
        
        if months%6 == 1 and not(months == 1):
            annualSalary *= semiAnnualRaise
            
    return current_savings, months

# Find a save rate with bisection search
def bisection_housing():
    max_months = 36
    high = 10000
    low = 0
    portion_saved = int((high + low)/2)
    bisection_steps = 1
    print('---------------------------')
    print('Bisection Search')
    # Call the function with calculates the total savings after 36 months with a new save rate
    total_savings = buyHouse(max_months, total_cost, down_payment, annual_salary, semi_annual_raise, portion_saved)
    
    # Check if the total savings are within the boundary
    while total_savings[0] < (down_payment - 100) or total_savings[0] > (down_payment + 100):
        bisection_steps += 1
        
        # Calculate new save rate based on the total savings
        print('low = ', low, 'high = ', high, 'save rate = ', portion_saved)
        if abs(total_savings[0] - down_payment) >= epsilon and total_savings[0] < down_payment:
            low = portion_saved
        elif abs(total_savings[0] - down_payment) >= epsilon and total_savings[0] > down_payment:
            high = portion_saved
    
        portion_saved = int((high + low)/2)
        
        # If the save rate is 100% and the savings amount is still less than the down payment it is not possible to buy the house
        if portion_saved == 9999 and total_savings[0] < down_payment:
            return portion_saved, bisection_steps, total_savings[0], False
        else:
            total_savings = buyHouse(max_months, total_cost, down_payment, annual_salary, semi_annual_raise, portion_saved)
        
    return portion_saved, bisection_steps, total_savings[0], True

# Print messages depending on if the down payment can be achieved wihin 36 months with a certain save rate
save_amount = bisection_housing()

if save_amount[3]:
    print('The best savings rate is: ', round(save_amount[0]/10000, 4))
    print('Steps in bisection search: ', save_amount[1])
    print('Total savings', save_amount[2])
else:
    print('It is not possible to pay the down payment in three years with the current salary.')


