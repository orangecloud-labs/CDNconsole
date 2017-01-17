#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system
from maxcdn import MaxCDN
import sys
import os
import curses
import atexit
import time


# Get input from console

def get_param(prompt_string):
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input


# Execution and displaying of terminal commands


def execute_cmd(cmd_string):
    system('clear')
    a = system(cmd_string)
    print ('')
    if a == 0:
        print ('Command executed correctly')
    else:
        print ('Command terminated with error')
    raw_input('Press enter')
    print ('')


# Zone management

def cdn_zones(api):
    y = 0
    while y != ord('4'):
        screen.clear()
        screen.border(0)
        screen.addstr(2, 2, 'Please enter a number...')
        screen.addstr(4, 4, '1 - Pull Zone')
        screen.addstr(5, 4, '2 - Push Zone')
        screen.addstr(6, 4, '3 - VOD Zone')
        screen.addstr(7, 4, '4 - Back')
        screen.refresh()
        y = screen.getch()

        # Pull zone

        if y == ord('1'):
            z = 0
            while z != ord('7'):
                screen.clear()
                screen.border(0)
                screen.addstr(1, 2, 'Pull Zone')
                screen.addstr(2, 2, 'Please enter a number...')
                screen.addstr(4, 4, '1 - Create')
                screen.addstr(5, 4, '2 - Modify')
                screen.addstr(6, 4, '3 - Delete')
                screen.addstr(7, 4, '4 - Purge Files')
                screen.addstr(8, 4, '5 - Purge Zones')
                screen.addstr(9, 4, '6 - View Zones')
                screen.addstr(10, 4, '7 - Back')
                screen.refresh()
                z = screen.getch()
                try:

                    # Create Pull Zone

                    if z == ord('1'):
                        zone_name = get_param('Enter the Zone name')
                        zone_origin = \
                            get_param('Enter the Origin Server url')
                        params = {'name': zone_name, 'url': zone_origin}
                        jtxt = api.post('/zones/pull.json', data=params)

                        # json_print(jtxt)
                        # display JSON params

                        screen.addstr(11, 7, 'Created zone with ID: '
                                + str(jtxt['data']['pullzone']['id']))
                        screen.refresh()
                        screen.getch()

                    # Modify Pull Zone

                    if z == ord('2'):
                        zone_id = get_param('Enter the Zone ID')
                        param = \
                            get_param('Enter the Pull Zone modification parameter(example: sslshared 1)'
                                ).split()

                        # value = get_param("Enter the Value for the ["+param+"]parameter")

                        params = {param[0]: param[1]}
                        jtxt = api.put('/zones/pull.json/' + zone_id,
                                params=params)

                        # display JSON params

                        screen.addstr(11, 7, 'Updated [' + param[0]
                                + '] with value: ' + str(jtxt['data'
                                ]['pullzone'][param[0]]))
                        screen.refresh()
                        time.sleep(1)

                    # Delete Pull Zone

                    if z == ord('3'):
                        zone_id = get_param('Enter the Zone ID')
                        jtxt = api.delete('/zones/pull.json/' + zone_id)

                        # display JSON params

                        screen.addstr(11, 7, 'Code: ' + str(jtxt['code'
                                ]) + ', Success!')
                        screen.refresh()
                        time.sleep(1)

                    # Purge files

                    if z == ord('4'):
                        zone_id = get_param('Enter the Zone ID')
                        f_arr = []
                        while True:
                            f_path = \
                                get_param('Enter relative paths of the files to purge (example: /favicon.ico) or q to end input')
                            if f_path == 'q':
                                break
                            f_arr.append(f_path)
                        jtxt = api.purge(zone_id, f_arr)

                        # display JSON params

                        screen.addstr(11, 7, 'Code: ' + str(jtxt['code'
                                ]) + ', Success!')
                        screen.refresh()
                        time.sleep(1)

                    # Purge zone

                    if z == ord('5'):
                        zone_id = get_param('Enter the Zone ID')
                        jtxt = api.purge(zone_id)

                        # display JSON params

                        screen.addstr(11, 7, 'Code: ' + str(jtxt['code'
                                ]) + ', Success!')
                        screen.refresh()
                        time.sleep(1)

                    # Print zones

                    if z == ord('6'):
                        json_zprint(api, 'pullzones', 'pull')
                except:

                    err(sys.exc_info())
                    break
            curses.endwin()

        # Push Zone

        if y == ord('2'):
            z = 0
            while z != ord('5'):
                screen.clear()
                screen.border(0)
                screen.addstr(1, 2, 'Push Zone')
                screen.addstr(2, 2, 'Please enter a number...')
                screen.addstr(4, 4, '1 - Create')
                screen.addstr(5, 4, '2 - Modify')
                screen.addstr(6, 4, '3 - Delete')
                screen.addstr(7, 4, '4 - View Zones')
                screen.addstr(8, 4, '5 - Back')
                screen.refresh()
                z = screen.getch()
                try:

                    # Create Push Zone

                    if z == ord('1'):
                        zone_name = get_param('Enter the Zone name')
                        zone_password = \
                            get_param('Enter the Zone password')
                        params = {'name': zone_name,
                                  'password': zone_password}
                        jtxt = api.post('/zones/push.json', data=params)

                        # Display JSON params

                        screen.addstr(11, 7, 'Created zone with ID: '
                                + str(jtxt['data']['pushzone']['id']))
                        screen.refresh()
                        screen.getch()

                    # Modify Push Zone

                    if z == ord('2'):
                        zone_id = get_param('Enter the Zone ID')
                        param = \
                            get_param('Enter the Push Zone modification parameter'
                                ).split()

                        # value = get_param("Enter the Value for the ["+param+"] parameter")

                        params = {param[0]: param[1]}
                        jtxt = api.put('/zones/push.json/' + zone_id,
                                params=params)

                        # Display JSON params

                        screen.addstr(11, 7, 'Updated [' + param[0]
                                + '] with value: ' + str(jtxt['data'
                                ]['pushzone'][param[0]]))
                        screen.refresh()
                        time.sleep(1)

                    # Delete Push Zone

                    if z == ord('3'):
                        zone_id = get_param('Enter the Zone ID')
                        jtxt = api.delete('/zones/push.json/' + zone_id)

                        # Display JSON params

                        screen.addstr(11, 7, 'Code: ' + str(jtxt['code'
                                ]) + ', Success!')
                        screen.refresh()
                        time.sleep(1)
                    if z == ord('4'):
                        json_zprint(api, 'pushzones', 'push')
                except:

                    err(sys.exc_info())
                    break
            curses.endwin()

        # VOD zone

        if y == ord('3'):
            z = 0
            while z != ord('5'):
                screen.clear()
                screen.border(0)
                screen.addstr(1, 2, 'VOD Zone')
                screen.addstr(2, 2, 'Please enter a number...')
                screen.addstr(4, 4, '1 - Create')
                screen.addstr(5, 4, '2 - Modify')
                screen.addstr(6, 4, '3 - Delete')
                screen.addstr(7, 4, '4 - View Zones')
                screen.addstr(8, 4, '5 - Back')
                screen.refresh()
                z = screen.getch()
                try:

                    # Create VOD Zone

                    if z == ord('1'):
                        zone_name = get_param('Enter the Zone name')
                        zone_password = \
                            get_param('Enter the Zone password')
                        params = {'name': zone_name,
                                  'password': zone_password}
                        jtxt = api.post('/zones/vod.json', data=params)

                        # Display JSON params

                        screen.addstr(11, 7, 'Created zone with ID: '
                                + str(jtxt['data']['vodzone']['id']))
                        screen.refresh()
                        screen.getch()

                    # Modify VOD Zone

                    if z == ord('2'):
                        zone_id = get_param('Enter the Zone ID')
                        param = \
                            get_param('Enter the VOD Zone modification parameter (example: label MyZone'
                                ).split()

                        # value = get_param("Enter the Value for the ["+param+"] parameter")

                        params = {param[0]: param[1]}
                        jtxt = api.put('/zones/vod.json/' + zone_id,
                                params=params)

                        # Display JSON params

                        screen.addstr(11, 7, 'Updated [' + param[0]
                                + '] with value: ' + str(jtxt['data'
                                ]['vodzone'][param[0]]))
                        screen.refresh()
                        time.sleep(1)

                    # Delete VOD Zone

                    if z == ord('3'):
                        zone_id = get_param('Enter the Zone ID')
                        jtxt = api.delete('/zones/vod.json/' + zone_id)

                        # Display JSON params

                        screen.addstr(11, 7, 'Code: ' + str(jtxt['code'
                                ]) + ', Success!')
                        screen.refresh()
                        time.sleep(1)
                    if z == ord('4'):
                        json_zprint(api, 'vodzones', 'vod')
                except:

                    err(sys.exc_info())
                    break
            curses.endwin()
        curses.endwin()



# User management

def cdn_users(api):
    y = 0
    while y != ord('5'):
        screen.clear()
        screen.border(0)
        screen.addstr(2, 2, 'Please enter a number...')
        screen.addstr(4, 4, '1 - Create a new user')
        screen.addstr(5, 4, '2 - Modify a current user')
        screen.addstr(6, 4, '3 - Delete a current user')
        screen.addstr(7, 4, '4 - List Users')
        screen.addstr(8, 4, '5 - Back')
        screen.refresh()
        y = screen.getch()
        try:

            # Create User

            if y == ord('1'):
                email = get_param('Enter the users email')
                password = get_param('Enter the users password')
                fname = get_param('Enter the users first name')
                lname = get_param('Enter the users last name')
                params = {
                    'email': email,
                    'password': password,
                    'firstname': fname,
                    'lastname': lname,
                    }
                jtxt = api.post('/users.json', data=params)

                # Display JSON params

                screen.addstr(11, 7, 'Created user with ID: '
                              + str(jtxt['data']['user']['id']))
                screen.refresh()
                screen.getch()

            # Modify User

            if y == ord('2'):
                user_id = get_param('Enter the users ID')
                param = \
                    get_param('Enter the parameter you want to modify(example: firstname Jon'
                              ).split()

                # value = get_param("Enter the Value for the ["+param+"] parameter")

                params = {param[0]: param[1]}
                jtxt = api.put('/users.json/' + user_id, params=params)

                # Display JSON params

                screen.addstr(11, 7, 'Updated [' + param[0]
                              + '] with value: ' + str(jtxt['data'][''
                              ][param[0]]))
                screen.refresh()
                time.sleep(1)

            # Delete User

            if y == ord('3'):
                user_id = get_param('Enter the users ID')
                jtxt = api.delete('/users.json/' + user_id)

                # Display JSON params

                screen.addstr(11, 7, 'Code: ' + str(jtxt['code'])
                              + ', Success!')
                screen.refresh()
                time.sleep(1)

	    # List Users
            if y == ord('4'):
		json_uprint(api)
        except:

            err(sys.exc_info())
            break
    curses.endwin()


def main():

    x = 0
    screen.clear()
    alias = get_param('Enter the CDN Alias')
    key = get_param('Enter the CDN Consumer Key')
    secret = get_param('Enter the CDN Consumer Secret')
    api = MaxCDN(alias, key, secret)

    while x != ord('4'):

        screen.clear()
        screen.border(0)
        screen.addstr(1, 2, 'Alias: ' + alias)
        screen.addstr(2, 2, 'Please enter a number...')
        screen.addstr(4, 4, '1 - Change API Credentials')
        screen.addstr(5, 4, '2 - Zone management')
        screen.addstr(6, 4, '3 - User management')
        screen.addstr(7, 4, '4 - Exit')
        screen.refresh()

        x = screen.getch()

        if x == ord('1'):
            alias = get_param('Enter the CDN Alias')
            key = get_param('Enter the CDN Consumer Key')
            secret = get_param('Enter the CDN Consumer Secret')
            curses.endwin()
            api = MaxCDN(alias, key, secret)
        if x == ord('2'):
            cdn_zones(api)
        if x == ord('3'):
            cdn_users(api)


# Curses cleanup

def cleanup():
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()


# Error displaying and returning to original state

def err(err):
    screen.clear()
    screen.refresh()
    screen.addstr(6, 4, str(err[0]))
    screen.addstr(7, 4, str(err[1]))
    screen.getch()
    curses.endwin()

    # Write errors to file

    working_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(working_dir, 'errors.txt'), 'a')
    f.write('<' + time.strftime('%H:%M:%S') + ' - '
            + time.strftime('%d/%m/%Y') + '>\n' + str(err) + '''

''')


# JSON zone print

def json_zprint(api, ztype, zuri):
    i = 0
    j = 0
    k = 0
    jtxt = api.get('/zones/' + zuri + '.json')

    # printing multipage JSON

    screen.clear()
    screen.addstr(0, 2, 'ID:    Date: \t             CDN url:')
    while k < int(jtxt['data']['pages']):
        while j < len(jtxt['data'][ztype]):
            screen.addstr(i + 1, 2, str(jtxt['data'][ztype][j]['id'])
                          + ' ' + str(jtxt['data'
                          ][ztype][j]['creation_date']) + ' '
                          + str(jtxt['data'][ztype][j]['cdn_url']))
            screen.refresh()
            i += 2
            if i == 24:
                screen.getch()
                i = 0
                screen.clear()
                screen.refresh()
            j += 1
        k += 1
        j = 0
        jtxt = api.get('/zones/' + zuri + '.json?start=' + str(2)
                       + '&limit=1000&end=' + str(jtxt['data']['pages'
                       ]) + '&page=' + str(k + 1))
    screen.getch()
    curses.endwin()

#JSON user print
def json_uprint(api):
    i = 0
    j = 0
    k = 0
    jtxt = api.get('/users.json')

    # printing multipage pages

    screen.clear()
    screen.addstr(0, 2, 'ID:    Name:')
    while k < int(jtxt['data']['pages']):
        while j < len(jtxt['data']['users']):
            screen.addstr(i + 1, 2, str(jtxt['data']['users'][j]['id'])
                          + '  ' + str(jtxt['data'
                          ]['users'][j]['firstname']) + ' '
                          + str(jtxt['data']['users'][j]['lastname']))
            screen.refresh()
            i += 2
            if i == 24:
                screen.getch()
                i = 0
                screen.clear()
                screen.refresh()
            j += 1
        k += 1
        j = 0
        jtxt = api.get('/users.json?start=' + str(2)
                       + '&limit=1000&end=' + str(jtxt['data']['pages'
                       ]) + '&page=' + str(k + 1))
    screen.getch()
    curses.endwin()



atexit.register(cleanup)
screen = curses.initscr()

main()

            
