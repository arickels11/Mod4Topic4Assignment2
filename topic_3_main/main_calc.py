"""CIS 189
Author: Alex Rickels
Module 4 Topic 3 Assignment"""


# You may apply one $5 or $10 cash off per order.
# The second is percent discount coupons for 10%, 15%, or 20% off.
# If you have cash-off coupons, those must be applied first, then apply the percent discount coupons on the pre-tax
#  Then you add tax at 6% and shipping according to these guidelines:
#
# up to $10 dollars, shipping is $5.95
# $10 and up to $30 dollars, shipping is $7.95
# $30 and up to $50 dollars, shipping is $11.95
# Shipping is free for $50 and over


def calculate_order(price, cash_coupon, percent_coupon):
    if price < 10.00:
        if (price - cash_coupon)*(1 - (percent_coupon / 100)) < 0:
            return 5.95  # if coupons get price to under zero, customer only pays shipping costs
        else:
            return round((((price - cash_coupon)*(1 - (percent_coupon / 100)))*1.06) + 5.95, 2)
    else:
        pass


if __name__ == '__main__':

    initial_price = float(input("What is the price?"))
    cash = float(input("What is the cash discount, $5 or $10?"))
    percent = float(input("What is the percent discount, 10%, 15%, or 20%?"))
    final_price = float(calculate_order(initial_price, cash, percent))
    print(final_price)
