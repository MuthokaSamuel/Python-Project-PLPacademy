def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price

    else:

        return price

price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print("Final price:", final_price)
else:
    print("No discount applied. Final price:", final_price)
