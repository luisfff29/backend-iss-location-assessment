#!/usr/bin/env python3
import sys
import requests
from pprint import pprint

__author__ = 'luisfff29 with help from Joseph'

if sys.version_info[0] < 3:
    raise RuntimeError('This program should be run in Python 3')


def part_A():
    r = requests.get('http://api.open-notify.org/astros.json')
    d = r.json()
    print('People in Space: {}'.format(d['number']))
    for p in d['people']:
        print(' - {} in {}'.format(p['name'], p['craft']))


def main(args):
    if args[0] == 'part_A':
        part_A()


if __name__ == '__main__':
    main(sys.argv[1:])
