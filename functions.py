def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(price, discount_percent)
        
        print("Final price after discount:", final_price)
    except ValueError:
        print("Please enter valid numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()