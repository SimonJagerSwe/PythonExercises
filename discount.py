########## DISCOUNT ##########
price = float(input('Enter the price of the product: '))
discount = float(input('Enter the discount in percent: '))
discounted_price = price - (price * (discount / 100))
print(discounted_price)