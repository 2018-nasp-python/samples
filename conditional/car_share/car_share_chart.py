#! /usr/bin/env python3
"""Demonstrate the use of imports and print a chart of car share costs

This module demonstrates the importing of another module and its use.  It
houses a function to print out out the yearly car share plan costs for each of
the plan types for each of the intervals.
"""

import car_share


def plan_chart(start=0, end=2001, interval=25):
    """Prints a chart of all of plan costs for a range of driving distances

    This outputs the yearly cost of all driving plans for distances between
    the start and end parameters kilometers in increments of increment
    kilometers. It displays at which distance each plan becomes most cost
    effective


    Args:
        start (int, optional): Defaults to 0. Starting distance for plan cost
                               calculation

        end (int, optional): Defaults to 2001. Ending distance for plan cost
                             calculation

        interval (int, optional): Defaults to 25. The interval in kilometers
                                  to add to before performing cost calculation
    """

    last_cheapest = ""

    for distance in range(start, end, interval):

        pc = car_share.plan_cost("platinum", distance)
        sc = car_share.plan_cost("silver", distance)
        bc = car_share.plan_cost("bronze", distance)

        if pc <= sc and pc <= bc:
            cheapest = "platinum"
        elif sc <= pc and sc <= bc:
            cheapest = "silver"
        else:
            cheapest = "bronze"

        if last_cheapest != cheapest:
            plan_trans = cheapest
        print("Distance {} -> Pla:${:6.2f}  Sil:${:6.2f}  Bro:$ {:6.2f} {}".format(
            distance, pc, sc, bc, plan_trans
        ))

        last_cheapest = cheapest
        plan_trans = ""


if __name__ == "__main__":
    plan_chart()
