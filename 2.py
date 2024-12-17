import os
print("Sale Tax Calculator! - NJ")


item_prices = []

while True:
    
    user_input = input("Please enter how much your item costs (or type 'done' to finish): ")

   
    if user_input.lower() == 'done':
        break

    try:
        price = float(user_input)
        item_prices.append(price)
    except ValueError:
        print("Please enter a valid number or 'done'.")

os.system('clear')

total_sales_tax = sum(price * 0.06625 for price in item_prices)
total_amount = sum(item_prices) + total_sales_tax

print(f'The total amount of sales tax is: {round(total_sales_tax, 2)}')
print(f'Total amount for all items: {round(total_amount, 2)}')
