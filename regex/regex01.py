#! /usr/bin/env python3
"""
This is a brief demonstration of some more advanced python methods of
performing regular expression searches along with examples regular
expression patterns
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


def regex_demo():

    # Use re.search with regular expression input as a string, text to search,
    # and the re.IGNORECASE flag to make the pattern case insensitive
    postal_code_match = re.search(r'[A-Z]\d[A-Z] \d[A-Z]\d', CONTACT_INFO,
                                  re.IGNORECASE)

    # check if there is a match and use the match object group to print the
    #  postal code
    if postal_code_match:

        # print out the matched postal code using the match object
        # passing 0 or None to group() returns the entire match
        print(postal_code_match.group())

    # Specify regular expression pattern using raw string
    province_string = (r'Alberta|British Columbia|Manitoba|New Brunswick|' +
                       r'Newfoundland (and Labrador)?|Nova Scotia|Ontario|' +
                       r'Prince Edward Island|Quebec|Saskatchewan|' +
                       r'Northwest Territories|Yukon|Nunavut')

    # Create a regular expression object and use it to search
    # note use of re.IGNORECASE flag
    province_re = re.compile(province_string, re.IGNORECASE)
    province_match = province_re.search(CONTACT_INFO)

    # check if there is a match and use the match object group to print the
    #  province
    if province_match:

        # print out the matched province using the match object
        # passing 0 or None to group() returns the entire match
        print(province_match.group())

    # Create a regex object and use it to find first matching string
    phone_string = r'(?:\d-)?\d{3}-\d{3}-\d{4}'
    phone_re = re.compile(phone_string)

    # Split contact info into a list of individual lines
    contact_lines = CONTACT_INFO.splitlines()

    # Loop over contact info one line at a time
    for line in contact_lines:

        # Use the regular expression object to search each line
        phone_num = phone_re.search(line)

        # Check if there is a match
        if phone_num:
            # print out the matched phone number using the match object
            # passing 0 or None to group() returns the entire match
            print(phone_num.group())

    # Use the regular expression object to search the entire contact info
    # for phone numbers returning a list of all of the matching strings
    phone_nums = phone_re.findall(CONTACT_INFO)

    # Check if there is a match
    if phone_nums:
        # Print the entire list of matching phone number strings
        print(phone_nums)

    # Use the regular expression object to search the entire contact info
    # for phone numbers returning a list of match objects
    phone_iter = phone_re.finditer(CONTACT_INFO)

    # loop over all of the match objects
    for phone in phone_iter:

        # Using each match object print out the matching phone number
        # it's starting and ending position in the input string
        print("{} location: {} - {}".format(phone.group(), phone.start(),
                                            phone.end()))

    # Use named groups to create dictionary when matching phone numbers
    phone_info_string = (r'(?P<desc>[a-zA-Z -]+):\s+' +
                         r'(?P<num>(?:\d-)?\d{3}-\d{3}-\d{4})')

    # Use the regular expression object to search the entire contact info
    # for phone numbers returning a list of match objects
    phone_info_iter = re.finditer(phone_info_string, CONTACT_INFO)

    # loop over all of the match objects
    for phone_info in phone_info_iter:

        # Using each match object print out the matching phone number based
        # on the named groups contained in the regular expression
        print("{}: {}".format(phone_info.groupdict()['num'],
                              phone_info.groupdict()['desc']))

    # show broken regex with example exception handling
    phone_string_broken = r'(?:\d-?\d{3}-\d{3}-\d{4}'
    try:
        phone_string_broken_re = re.compile(phone_string_broken)

    except re.error as error:
        print(error.args)


if __name__ == "__main__":
    regex_demo()
