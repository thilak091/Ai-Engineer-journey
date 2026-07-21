def month_of(num):#easiest is to put everything in a list and access it by num but it will lead to errors 
    if num==0:
        return 'January'
    elif num==1:
        return 'February'
    elif num==2:
        return 'March'
    elif num==3:
        return 'April'
    elif num==4:
        return 'May'
    elif num==5:
        return 'June'
    
def branch_of(num):
    if num==0:
        return "Chennai"
    elif num==1:
        return "Bangalore"
    elif num==2:
        return "hyderabad"
    elif num==3:
        return "Mumbai"
    elif num==4:
        return "Delhi"

    
import numpy as np

#Section 1:Heading
print('====================================================')
print('               COMPANY SALES DASHBOARD')
print('====================================================\n')

import numpy as np

branches = np.array([
    "Chennai",
    "Bangalore",
    "hyderabad",
    "Mumbai",
    "Delhi"
])

months = np.array([
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
])

sales = np.array([
    [120000, 135000, 142000, 150000, 148000, 160000],
    [115000, 128000, 131000, 145000, 149000, 155000],
    [98000, 110000, 120000, 129000, 138000, 147000],
    [140000, 145000, 150000, 160000, 170000, 182000],
    [108000, 116000, 124000, 132000, 141000, 150000]
])

#Section 2:Dataset Information
print('Dataset Loaded Successfully\n')

print(f'Total Branches: {branches.size}')
print(f'Total Months: {months.size}\n')

print('----------------------------------------------------\n')

#Section 3:Overall Statistics
print('OVERALL STATISTICS\n')
print(f'Total Revenue :{sales.sum()}')
print(f'Average Revenue :{sales.mean()}')
print(f'Highest Single Sale:{sales.max()}')
print(f'Lowest Single Sale:{sales.min()}\n')

print('----------------------------------------------------\n')

#Section 4:BEST PERFORMERS
print('Best Performers\n')

sales_month=sales.sum(axis=0)
sales_branch=sales.sum(axis=1)

print(f'Best Performing Branch:{branch_of(sales_branch.argmax())}')
print(f'Branch Revenue:{sales_branch[sales_branch.argmax()]}\n')

print(f'Best Performing Month:{month_of(sales_month.argmax())}')
print(f'Month Revenue:{sales_month[sales_month.argmax()]}\n')

print('----------------------------------------------------\n')
#Section 5:MONTHLY SALES
print('Monthly Sales\n')

for i in range(months.size):
    print(f'{month_of(i)}: {sales_month[i]}\n')
print()
print('----------------------------------------------------\n')

#Section 6:BRANCH SALES
print('BRANCH SALES\n')

for i in range(branches.size):
    print(f'{branch_of(i)}: {sales_branch[i]}\n')
print()
print('----------------------------------------------------\n')

#Section 7:top Branch
print('Top Branch\n')
avg_branch=sales.mean(axis=1)
print(f'Top Branch Name:{branch_of(avg_branch.argmax())}')
print(f'Top Branch Average Sales: {avg_branch.argmax():.2f}')

print('----------------------------------------------------\n')

#Bonus: 10 percent Sales Projection
print('10 percent Sales Projection\n')
after_sales=sales * 1.1
print(f'New Total Revenue: {after_sales.max()}\n')
print('Projected Monthly Revenue :\n')
for i in range(months.size):
    print(f'{month_of(i)}: {after_sales.sum(axis=0)[i]}\n')
print()
print('Projected BranchWise Revenue:\n')
for i in range(branches.size):
    print(f'{branch_of(i)}: {after_sales.sum(axis=1)[i]}\n')
print()

print('====================================================')
print('               Report generated Successfully')
print('====================================================\n')