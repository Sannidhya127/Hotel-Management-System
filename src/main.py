# Basic user-friendly Hotel Management System Developed in Python. Completely cli based.

from colored import fg, bg, attr
import os
import time
import json


if os.path.exists("config.json") ==  True:
    pass
else:
    configFile = open('config.json', 'w')
    numberOfRooms = [x for x in range(1,101)]
    config = {
        "number_of_rooms" : numberOfRooms,
    }
    json_object = json.dumps(config, indent=4)
    configFile.write(json_object)
    configFile.close()

def CheckRoomAvailabilty():
    with open('config.json', 'r') as openfile:
        json_object = json.load(openfile)
        print(json_object['number_of_rooms'])





if __name__ == '__main__':
    print(f"{fg('light_yellow')}Hotel Twilight - System management software | Developed by @sannidhya127 | Powered by Python 3{attr('reset')}")
    while True:
        command = input(f'''\n\n{fg('turquoise_4')}Please enter the corresponding number for using the option:{attr('reset')} 
        {fg('light_gray')}1. Check Room Availability{attr('reset')}
        {fg('gold_1')}2. Book room{attr('reset')}
        {fg('navajo_white_1')}3. Order Food{attr('reset')}
        {fg('misty_rose_3')}4. Get data by user{attr('reset')}
        {fg('khaki_1')}5. View Staff data by name{attr('reset')}
        {fg('light_sky_blue_3a')}6. Send mail{attr('reset')}
        {fg('purple_1a')}7. Room Status by number{attr('reset')}
        8. exit\n{fg('green_1')}Enter Here: {attr('reset')}''')

        if command == '8':
            exit()
        elif command == '1':
            CheckRoomAvailabilty()