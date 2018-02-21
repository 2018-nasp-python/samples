#! /usr/bin/env python3

import subprocess
import re
import collections
import ipaddress
import pprint

Passwd_Line = collections.namedtuple('Adapter', ['id', 'device', 'ip_version', 'ip_addr', 'scope', 'dynamic', 'shell', 'sup_groups'])
Group_Line = collections.namedtuple('Group_Line', ['name', 'password', 'gid', 'user_list'])

# see https://docs.python.org/3/library/subprocess.html#subprocess.Popen for list of arguments
#
ip_invocaton = subprocess.run(
    ['ip', '-o', 'address', 'show'],
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
    universal_newlines=True
)

#split the output based on 
adapter_strings = ip_invocaton.stdout.split('\n')[:-1]
ipv4_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}'
ipv6_regex = r'[0-9a-fA-F:]{2,43}\/\d{1,3}'
adapters = {}
for string in adapter_strings:
    adapt_info = re.search(r'^(\d{1,2}): (\w+)\s+(\w+)', string).groups()
    if adapt_info[1] == 'lo':
        # its a loop back adapater
        if adapt_info[2] == 'inet':
            # ip4 addres
            ip_address = ipaddress.IPv4Interface(re.search(ipv4_regex, string).group())
        elif adapt_info[2] == 'inet6':
            # ip6 address
            ip_address = ipaddress.IPv6Interface(re.search(ipv6_regex, string).group())
    elif adapt_info[2] == 'inet':
        # ip4 addres
        ip_address = ipaddress.IPv4Interface(re.search(ipv4_regex, string).group())
    elif adapt_info[2] == 'inet6':
        # ip6 address
        ip_address = ipaddress.IPv6Interface(re.search(ipv6_regex, string).group())
    if ip_address != "":
        if adapt_info[1] not in adapters:
            adapters[adapt_info[1]] = [[ip_address, ]]
        else:
            adapters[adapt_info[1]][0].append(ip_address) 
    ip_address = ""

pprint.pprint(adapters)