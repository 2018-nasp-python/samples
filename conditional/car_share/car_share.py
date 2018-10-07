#! /usr/bin/env python3
"""This module contains functions for calculating the cheapest care share plan

The plan is chosen based on estimated driving distance.

The care share plans are as follows:
    Platinum: 500 fee, 200 free km then $0.25 / KM
    Silver: 200 fee, 50 free km then $0.50 / KM
    Bronze: 100 fee, no free km and $0.70 / KM
"""


def calc_cost(plan_fee, free_km, rate_km, drive_dist):
    """Calculates the yearly cost of a car share plan

    Based on the plan specifications and the driving distance return the yearly
    cost of the plan

    Args:
        plan_fee (float):  the yearly fee of the car share plan in dollars

        free_km (float): the number of free yearly kilometers included in the
                         plan

        rate_km (float): the rate charged for all kilometers driven beyond the
                         included free kilometers. This is measured in dollars
                         per kilometer.

        drive_dist (float): the estimated distance in kilometers to be driven
                            in a year

    Returns:
        float: the total yearly cost of the plan in dollars
    """

    if (drive_dist - free_km) <= 0:
        drive_dist = free_km

    cost = plan_fee + (drive_dist - free_km) * rate_km

    return cost


def plan_cost(plan_type, dist):
    """Calculates the yearly cost of a car share plan based on plan name

    This functions populates the car share plan specifications and invokes
    calc_cost to calculate the yearly cost of the car share plan.

    Args:
        plan_type (str): The name of the car share plan
        dist (float): Estimated yearly driving distance in kilometers

    Returns:
        float: The yearly car share plan cost in dollars
    """

    if plan_type == "platinum":
        cost = calc_cost(plan_fee=500, free_km=200,
                         rate_km=.25, drive_dist=dist)
    elif plan_type == "silver":
        cost = calc_cost(plan_fee=200, free_km=50,
                         rate_km=.50, drive_dist=dist)
    else:  # plan_type == "bronze":
        cost = calc_cost(plan_fee=100, free_km=0, rate_km=.70, drive_dist=dist)
    return cost


def best_plan(dist):
    """Calculates the best driving plan based on driving distance

    Based on the input driving distance it invokes plan cost for each of the
    car share plans and returns to the user the cheapest one and its cost for
    their specified distance.

    Args:
        dist (float): Estimated yearly driving distance

    Returns:
        tuple [str, float]: a tuple contianing the cheapest car share name
            and the yearly cost in dollars
    """

    platinum_cost = plan_cost("platinum", dist)
    silver_cost = plan_cost("silver", dist)
    bronze_cost = plan_cost("bronze", dist)

    if platinum_cost <= silver_cost and platinum_cost <= bronze_cost:
        return "platinum", platinum_cost
    elif silver_cost <= platinum_cost and silver_cost <= bronze_cost:
        return "silver", silver_cost
    else:
        return "bronze", bronze_cost


def main():
    """Print out best car share plan for user based on their distance

    Prompt the user for their yearly driving distance and print the cheapest
    plan based on that distance
    """

    distance = int(input("Enter yearly driving distance: "))
    print("The best plan for you is {0}: ${1}".format(*best_plan(distance)))


if __name__ == "__main__":
    main()
