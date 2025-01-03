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

def get_tax_rate_by_state():
    # Dictionary containing tax rates for each state, Washington D.C., and Puerto Rico
    state_tax_rates = {
        "AL": 0.04, "AK": 0.0, "AZ": 0.056, "AR": 0.065,
        "CA": 0.0725, "CO": 0.029, "CT": 0.0635, "DE": 0.0,
        "DC": 0.06, "FL": 0.06, "GA": 0.04, "HI": 0.04,
        "ID": 0.06, "IL": 0.0625, "IN": 0.07, "IA": 0.06,
        "KS": 0.065, "KY": 0.06, "LA": 0.04, "ME": 0.055,
        "MD": 0.06, "MA": 0.0625, "MI": 0.06, "MN": 0.06875,
        "MS": 0.07, "MO": 0.04225, "MT": 0.0, "NE": 0.055,
        "NV": 0.0685, "NH": 0.0, "NJ": 0.06625, "NM": 0.05125,
        "NY": 0.08875, "NC": 0.0475, "ND": 0.05, "OH": 0.0575,
        "OK": 0.045, "OR": 0.0, "PA": 0.06, "RI": 0.07,
        "SC": 0.06, "SD": 0.045, "TN": 0.07, "TX": 0.0625,
        "UT": 0.0465, "VT": 0.06, "VA": 0.053, "WA": 0.065,
        "WV": 0.06, "WI": 0.05, "WY": 0.04, "PR": 0.115
    }

    state = input("Please enter the state you live in (abbreviation, e.g., 'NJ'): ").strip().upper()
    return state_tax_rates.get(state, 0.06625) #<default taxr

def main():
    print("Sales Tax Calculator!")

    tax_rate = get_tax_rate_by_state()

    item_prices = get_item_prices()
    
    clear_screen()

    total_sales_tax = calculate_sales_tax(item_prices, tax_rate)
    total_amount = calculate_total_amount(item_prices, total_sales_tax)

    print_results(total_sales_tax, total_amount)

if __name__ == "__main__":
    main()
