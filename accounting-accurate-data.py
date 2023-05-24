'''
create a function that parses through the text file
convert number str to int s and floats
split name to first and last
calculated expected price, cost * qnty
print what customer paid and expected payment
use comparison , <> to print that customer overpaid or underpaid 
remember to close your file using .close()
parse in the txt file during the function call
include comments
'''
from decimal import Decimal

COST_OF_MELON = Decimal("1.00")

def customer_payment(customer_orders):
    """Calculate which customer underpaid based on data provided"""

    # open file
    payment_file = open(customer_orders)

    # iterate through each line in the file
    for line in payment_file:
        # split using "|" to obtain list of string
        orders = line.split("|")

        # unpack the split list of strings
        order_id, full_name, quantity, amount_paid = orders 

        # convert quantity and paid to int and float
        quantity = int(quantity)
        amount_paid = Decimal(amount_paid)

        # unpack full_name to get a list of first and last name

        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[1]

        # what customer is expected to pay based on number of melons
        expected_pay = COST_OF_MELON * quantity

        # what customer owe
        difference = expected_pay - amount_paid


        # print what customer paid vs expected pay
        print(f"{full_name} paid ${amount_paid}, and expected payment is ${expected_pay}")

        # make  comparison to determine if customer overpaid or underpaid
        if amount_paid < expected_pay:
            print(f"{first_name} underpaid. Incomplete payment, you owe ${difference}")
        elif amount_paid > expected_pay:
            print(f"{first_name} overpaid. Your change is ${difference}.")
        else:
            print(f"Thank you {first_name} for you purchase.")
        
    # close the txt file
    payment_file.close()

# call the function
customer_payment("customer-orders.txt")

