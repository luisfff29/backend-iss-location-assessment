#!/usr/bin/env python3
import sys
import requests


__author__ = 'luisfff29 with help from Joseph'


if sys.version_info[0] < 3:
    raise RuntimeError('This program should be run in Python 3')


def part_A():
    r = requests.get('http://api.open-notify.org/astros.json')
    d = r.json()
    print('People in Space: {}'.format(d['number']))
    for p in d['people']:
        print(' - {} in {}'.format(p['name'], p['craft']))


def part_B():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    d = r.json()
    print('Geographic location:')
    for l, num in d['iss_position'].items():
        print('    {}: {}'.format(l, num))
    print('Timestamp: {}'.format(d['timestamp']))


def main(args):
    if args[0] == 'part_A':
        part_A()
    elif args[0] == 'part_B':
        part_B()


if __name__ == '__main__':
    main(sys.argv[1:])
