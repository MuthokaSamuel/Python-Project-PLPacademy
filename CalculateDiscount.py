def calculate_discount(price, discount_percent):


    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price

    else:

        return price
