#!/usr/bin/env python3
import sys
import requests
import turtle


__author__ = 'luisfff29 with help from Joseph'


if sys.version_info[0] < 3:
    raise RuntimeError('This program should be run in Python 3')

astronauts_api = 'http://api.open-notify.org/astros.json'
coordinates_api = 'http://api.open-notify.org/iss-now.json'


def part_A():
    r = requests.get(astronauts_api)
    d = r.json()
    print('People in Space: {}'.format(d['number']))
    for p in d['people']:
        print(' - {} in {}'.format(p['name'], p['craft']))


def part_B():
    r = requests.get(coordinates_api)
    d = r.json()
    print('Geographic location:')
    for l, num in d['iss_position'].items():
        print('    {}: {}'.format(l, num))
    print('Timestamp: {}'.format(d['timestamp']))


def part_C():
    s = turtle.Screen()
    t = turtle.Turtle()

    s.setup(width=720, height=360)
    s.bgpic('map.gif')
    s.title('ISS Location')
    s.addshape('iss.gif')
    s.setworldcoordinates(-180, -90, 180, 90)

    t.penup()
    t.shape('iss.gif')
    while True:
        r = requests.get(coordinates_api).json()
        LON = r['iss_position']['longitude']
        LAT = r['iss_position']['latitude']
        lon, lat = LON, LAT
        t.goto(float(lon), float(lat))

    turtle.done()


def part_D():
    pass


def main(args):
    if args[0] == 'part_A':
        part_A()
    elif args[0] == 'part_B':
        part_B()
    elif args[0] == 'part_C':
        part_C()
    elif args[0] == 'part_D':
        part_D()
    else:
        part_A()
        part_B()
        part_C()
        part_D()


if __name__ == '__main__':
    main(sys.argv[1:])
