#!/usr/bin/env python3
import sys
import requests
import turtle
import time


__author__ = 'luisfff29 with help from Joseph and Daniel'

# Making sure this code is running in python3
if sys.version_info[0] < 3:
    raise RuntimeError('This program should be run in Python 3')

astronauts_api = 'http://api.open-notify.org/astros.json'
coordinates_api = 'http://api.open-notify.org/iss-now.json'
indianapolis_api = 'http://api.open-notify.org/iss-pass.json'
IN_LAT, IN_LON = 39.791000, -86.148003


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


# Create turtle with map as background
def turtle_python():
    s = turtle.Screen()
    s.setup(width=720, height=360)
    s.bgpic('map.gif')
    s.title('ISS Location')
    s.setworldcoordinates(-180, -90, 180, 90)


def part_C():
    turtle_python()
    t = turtle.Turtle()
    t.penup()
    turtle.Screen().addshape('iss.gif')
    t.shape('iss.gif')

    # Infinite loop to track the ISS
    while True:
        r = requests.get(coordinates_api).json()
        LON = r['iss_position']['longitude']
        LAT = r['iss_position']['latitude']
        lon, lat = LON, LAT
        t.goto(float(lon), float(lat))

    turtle.done()


def part_D():
    url = '{}?lat={}&lon={}'.format(indianapolis_api, IN_LAT, IN_LON)
    r = requests.get(url)
    d = r.json()
    # Timestamp resutl after a successful call
    timestamp = d['response'][0]['risetime']
    print('The next time the ISS will be overhead '
          'of Indianapolis IN will be on:')
    rise_time = time.ctime(timestamp)
    print('\t' + rise_time)
    # Show map with yellow dot of the location
    turtle_python()
    t = turtle.Turtle()
    t.penup()
    t.color('yellow')
    t.goto(IN_LON, IN_LAT)
    t.dot(5)
    t.hideturtle()
    t.write(rise_time, align="center", font=("Arial", 12, "normal"))
    turtle.done()


def main(args):
    if args[0] == 'part_A':
        part_A()
    elif args[0] == 'part_B':
        part_B()
    elif args[0] == 'part_C':
        part_C()
    elif args[0] == 'part_D':
        part_D()


if __name__ == '__main__':
    main(sys.argv[1:])
