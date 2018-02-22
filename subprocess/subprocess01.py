#! /usr/bin/env python3

import subprocess
import re
import collections
import ipaddress
import pprint

Adapter = collections.namedtuple('Adapter', ['name', 'ip_address_state', 'mac_address'])


# see https://docs.python.org/3/library/subprocess.html#subprocess.Popen for list of arguments
#
ip_address_list = subprocess.run(
    ['ip', '-o', 'address', 'show'],
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
    universal_newlines=True
)

ip_route_list = subprocess.run(
    ['ip', 'route', 'list'],
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
    universal_newlines=True
)

adapt_info_re = re.compile(r'^(\d{1,2}): (\w+)\s+(\w+)')
ipv4_re = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
ipv4_w_sm_re = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}')
ipv6_re = re.compile(r'[0-9a-fA-F:]{2,43}\/\d{1,3}')
assign_re = re.compile(r'dynamic')
mac_re = re.compile(r'([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}')

#split the ip command output by line
ip_address_strings = ip_address_list.stdout.splitlines()



adapters = {}
for string in ip_address_strings:
    adapt_info = adapt_info_re.search(string).groups()
    if adapt_info[2] == 'inet':
        # create ipv4 addres based on parsed string
        ip_address = ipaddress.IPv4Interface(ipv4_w_sm_re.search(string).group())
    elif adapt_info[2] == 'inet6':
        # create ipv6 addres based on parsed string
        ip_address = ipaddress.IPv6Interface(ipv6_re.search(string).group())

    if ip_address != None: 

        if assign_re.search(string) == None:
            assign_method = 'static'
        else:
            assign_method = 'dynamic'

        if adapt_info[1] not in adapters:
            ip_link_list = subprocess.run(
                                ['ip', '-o', 'link', 'show', 'dev', adapt_info[1] ],
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                universal_newlines=True)
            
            mac_address = mac_re.search(ip_link_list.stdout).group()

            adapters[adapt_info[1]] = [[ip_address, assign_method ], mac_address]
        else:
            adapters[adapt_info[1]][0].append([ip_address, assign_method]) 

    ip_address = None


pprint.pprint(adapters)