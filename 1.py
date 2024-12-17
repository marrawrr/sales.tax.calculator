# print("Sale Tax Calculator! - NJ ")

# price = float(input("Please enter how much your item costs: "))

# sales_tax_amount = price * 0.06625
# print(f'The amount of sales tax is: {sales_tax_amount}')

# total = round(price + sales_tax_amount, 2)

# print(f'Total: {total}')

def get_item_price():
    return float(input("Please enter how much your item costs: "))

def calculate_sales_tax(price):
    sales_tax_rate = 0.06625  
    return price * sales_tax_rate

def calculate_total(price, sales_tax_amount):
    return round(price + sales_tax_amount, 2)

def main():
    print("Sale Tax Calculator! - NJ")

    price = get_item_price()
    sales_tax_amount = calculate_sales_tax(price)
    total = calculate_total(price, sales_tax_amount)

    print(f'The amount of sales tax is: {sales_tax_amount}')
    print(f'Total: {total}')

if __name__ == "__main__":
    run()
