'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''
# TODO0 - Fix the total amount payable for an order exceeded bug
# TODO1 - Fix test_4 in tests.py
# TODO2 - Remove the DEBUG flag before submitting the solution

from collections import namedtuple
from decimal import Decimal

DEBUG = False
Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


def validorder(order: Order):
    net = Decimal('0.00')

    for item in order.items:
        if item.type == 'payment':
            net += Decimal(str(item.amount))
            if DEBUG:
                print("net after adding payment: ", net)
        elif item.type == 'product':
            net -= Decimal(str(item.amount)) * item.quantity
            if DEBUG:
                print("net after subtracting product: ", net)
        else:
            return "Invalid item type: %s" % item.type
        if DEBUG:
            print("net: balance: ", net)
    if net != Decimal('0.00'):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
