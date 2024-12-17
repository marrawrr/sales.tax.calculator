import os

def clear_screen():
    os.system('clear')

def get_item_prices():
    item_prices = []
    while True:
        user_input = input("Please enter how much your item costs (and when finished type 'done'): ")

        if user_input.lower() == 'done':
            break

        
        price = float(user_input)
        item_prices.append(price)

    return item_prices

def calculate_sales_tax(item_prices, tax_rate=0.06625):
    total_sales_tax = sum(price * tax_rate for price in item_prices)
    return total_sales_tax

def calculate_total_amount(item_prices, total_sales_tax):
    return sum(item_prices) + total_sales_tax

def print_results(total_sales_tax, total_amount):
    print(f'The total amount of sales tax is: {round(total_sales_tax, 2)}')
    print(f'Total amount for all items: {round(total_amount, 2)}')

def main():
    print("Sale Tax Calculator! - NJ")

    
    item_prices = get_item_prices()

    
    clear_screen()

    
    total_sales_tax = calculate_sales_tax(item_prices)
    total_amount = calculate_total_amount(item_prices, total_sales_tax)

    print_results(total_sales_tax, total_amount)

if __name__ == "__main__":
    main()
