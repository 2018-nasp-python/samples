#! /usr/bin/env python3
"""
This module builds a restuarant order from a menu. Based on this order it
calculates the total bill including tax and tip.

The Menu is:
    eggs - $6.00,
    sausage and eggs - $8.00,
    bacon and eggs - $7.50,
    pancakes - $7.00,
    cereal - $5.50,
    coffee - $2.00,
    tea - $1.50,
    juice - $3.50
"""
from typing import Dict, List

menu: Dict[str, float] = {
    "eggs": 6.00,
    "sausage and eggs": 8.00,
    "bacon and eggs": 7.50,
    "pancakes": 7.00,
    "cereal": 5.50,
    "coffee": 2.00,
    "tea": 1.50,
    "juice": 3.50
}
"""Menu items
"""

PST_RATE: float = 0.07
"""Constant for PST tax rate
"""

GST_RATE: float = 0.05
"""Constant for GST tax rate
"""

TIP_RATE: float = 0.15
"""Constant for tip rate
"""


def item_charge(item: str) -> float:
    """
    Calculates charge for individual item based on menu price

    Args:
        item (str): the name of the item as it appears in the menu

    Returns:
        float: the price of the item from the menu
    """

    return menu[item]


def calculate_bill(order: List[str]) -> float:
    """
    Calculates the total bill for all the items in the menu

    This bill includes the following taxes:
        PST: 7% 
        GST: 5% 

    The bill also includes a tip of 15% 

    The additional charges are only applied to the bill itself
    I.E. 

        PST = item total * PST Rate
        GST = item total * GST Rate
        Tip = item total * Tip Rate

        Bill = item total + PST + GST + TIP

    Args:
        order (List[str]): a list of menu items

    Returns:
        float: total bill
    """

    total = 0.0
    for item in order:
        total += item_charge(item)

    total *= (1 + PST_RATE + GST_RATE + TIP_RATE)

    return total


def build_order() -> List[str]:
    """
    Prompt the user for items that they want and add them to
    their order.

    If the item is not on the menu inform them by printing:
        "Sorry, we don't have $item_input"

    Where $item_input is the menu item they entered at the prompt. 

    After a failed input attempt the user will be prompted to input another
    menu item . 

    The user will continue to select menu items until they enter 'done' to 
    indicate that have finished adding items.

    Returns:
        List[str]:  their order as a list of all of their items
    """

    item = ""
    order = []

    while item != "done":
        item = input(
            "What would you like to order - enter 'done' when finished: ")
        if item == "done":
            break
        elif item not in menu:
            print("Sorry, we don't have {}".format(item))
            continue
        order.append(item)

    return order


def main():
    """
    Build the customer order, calculate the bill, print the order and total cost
    """

    order = build_order()
    total = calculate_bill(order)
    print("Your order was: {}".format(order))
    print("Your bill will be: ${:2.2f}".format(total))


if __name__ == "__main__":
    main()
