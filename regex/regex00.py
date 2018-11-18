#! /usr/bin/env python3
"""
This is a brief demonstration of common python methods of performing regular
expression searches.
"""

import re

CONTACT_INFO = '''
555 Seymour Street
Vancouver, British Columbia
V6B 3H6 , Canada

Main Switchboard Phone: 604-434-5734
Toll-free: 1-866-434-1610
Fax: 604-687-2488
Security Non-emergency: 604-412-7600
Security Emergency: 604-412-7602
'''


def main():

    # Create phone numbers pattern object
    phone_numbers_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

    # Demonstrate pattern.search()
    print("Printing Phone Numbers with Repeated Search")

    # This invocation of Pattern.search() Leaves out starting search position:
    # it defaults to 0
    phone_numbers_match = phone_numbers_pattern.search(CONTACT_INFO)

    # While the search returned a match
    while phone_numbers_match:

        match_start_pos = phone_numbers_match.start()
        match_end_pos = phone_numbers_match.end()

        print("Phone Number at Position: {} - {}".format(
            match_start_pos, CONTACT_INFO[match_start_pos:match_end_pos]))

        phone_numbers_match = phone_numbers_pattern.search(
            CONTACT_INFO, match_end_pos)

    # Demonstrate pattern.findall()
    print("\nPrinting Phone Numbers with pattern findall")

    # Use Pattern.findall() rather than search.
    # This returns a list of matching strings rather than a match object.
    phone_numbers = phone_numbers_pattern.findall(CONTACT_INFO)

    # Check if there was a match
    if phone_numbers:
        # Loop over all of the matching strings
        for number in phone_numbers:
            print(number)

    # Demonstrate re.findall()
    print("\nPrinting Phone Numbers with re findall")

    # Uses re.findall() and passes the regular expression as a raw string
    # rather than a precompiled pattern object as in the above example
    phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', CONTACT_INFO)

    # Check if there was a match
    if phone_numbers:
        # Loop over all of the matching strings
        for number in phone_numbers:
            print(number)

    # Demonstrate re.finditer()
    print("\nPrinting Phone Numbers with finditer")

    # Uses re.finditer() and passes the regular expression as a raw string
    phone_numbers_iter = re.finditer(r'\d{3}-\d{3}-\d{4}', CONTACT_INFO)

    # Loop over all of the match objects returned by finditer
    for number_match in phone_numbers_iter:
        print("Phone Number at Position: {} - {}".format(
            number_match.start(),
            CONTACT_INFO[number_match.start():number_match.end()]))


if __name__ == "__main__":
    main()
