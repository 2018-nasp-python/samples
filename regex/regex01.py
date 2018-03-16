import pprint
import re

contact_info = '''
555 Seymour Street
Vancouver, British Columbia
V6B 3H6 , Canada

Main Switchboard Phone: 604-434-5734
Toll-free: 1-866-434-1610
Fax: 604-687-2488
Security Non-emergency: 604-412-7600
Security Emergency: 604-412-7602
'''

# Use re.search with regex and text to search 
# note use of re.IGNORECASE flag
postal_code_match = re.search(r'[A-Z]\d[A-Z] \d[A-Z]\d', contact_info, re.IGNORECASE)
if postal_code_match:
    print(postal_code_match.group())

# Create a regex object and use it to search 
# note use of re.IGNORECASE flag
province_string = r'Alberta|British Columbia|Manitoba|New Brunswick|Newfoundland (and Labrador)?|Nova Scotia|Ontario|Prince Edward Island|Quebec|Saskatchewan|Northwest Territories|Yukon|Nunavut'
province_re = re.compile(province_string, re.IGNORECASE)
province_match = province_re.search(contact_info)
if province_match:
    print(province_match.group())

# Loop over contact info one line at a time
# Create a regex object and use it to find first matching string 
phone_string = r'(?:\d-)?\d{3}-\d{3}-\d{4}'
phone_re = re.compile(phone_string)
contact_lines = contact_info.splitlines()
for line in contact_lines:
    phone_num = phone_re.search(line)
    if phone_num:
        print(phone_num.group())

       
# Create a regex object and use it to find all matching strings
phone_nums = phone_re.findall(contact_info)
if phone_nums:
    print(phone_nums)

# Create a regex object and use it to find all matches 
# loop over these matches
phone_iter = phone_re.finditer(contact_info)
if phone_iter:
    for phone in phone_iter:
       print("{} location: {} - {}".format(phone.group(), phone.start(), phone.end()))

# Use named groups to create dictionary in match
phone_info_string = r'(?P<desc>[a-zA-Z -]+):\s+(?P<num>(?:\d-)?\d{3}-\d{3}-\d{4})'
phone_info_iter = re.finditer(phone_info_string, contact_info)
for phone_info in phone_info_iter:
    print("{}: {}".format(phone_info.groupdict()['num'],
                                 phone_info.groupdict()['desc']))


# show broken regex with exception handling
phone_string_broken = r'(?:\d-?\d{3}-\d{3}-\d{4}'
try:
    phone_string_broken_re = re.compile(phone_string_broken)

except re.error as error:
    print(error.args)
