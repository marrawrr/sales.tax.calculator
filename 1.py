print("Sale Tax Calculator! - NJ ")

price = float(input("Please enter how much your item costs: "))

sales_tax_amount = price * 0.06625
print(f'The amount of sales tax is: {sales_tax_amount}')

total = round(price + sales_tax_amount, 2)

print(f'Total: {total}')

