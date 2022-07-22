# Basic user-friendly Hotel Management System Developed in Python. Completely cli based.

from colored import fg, bg, attr
import os
import time


print(f"{fg('light_yellow')}Hotel Twilight - System management software | Developed by @sannidhya127 | Powered by Python 3{attr('reset')}")


if __name__ == '__main__':
    while True:
        command = input(f'''{fg('turquoise_4')}Please enter the corresponding number for using the option:{attr('reset')} 
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