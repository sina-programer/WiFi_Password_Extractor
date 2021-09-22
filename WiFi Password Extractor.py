import os
try:
    from termcolor import cprint
except ModuleNotFoundError:
    os.system('python -m pip install -r requirements.txt')
from itertools import cycle
from sys import stdout
import subprocess

colors = iter(cycle(['blue', 'red']))
loading_chars = iter(cycle('/-\|'))
os.system('cls')

print('\n Welcome to WiFi Password Extractor(written by Sina.f and Advik.B)\n')

for i in range(40):
    stdout.write(f'\r Extracting wifi passwords... {next(loading_chars)}')

print('\n\n\n {:<30}|  Password\n'.format('Host name'))
output = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode().splitlines()

profiles = [i.split(':', 1)[1][1:] for i in output if 'All User Profile' in i]

for profile in profiles:
    result = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('ISO-8859-1').splitlines()
    color = next(colors)

    try:
        password = [b.split(':', 1)[1][1:]
                    for b in result if 'Key Content' in b][0]
        cprint(f' {profile:<30}|  {password}', color=color)

    except:
        cprint(f' {profile:<30}|  <No password>', color=color)


figlet = f'''\n
   _____ _                __
  / ____(_)              / _|
 | (___  _ _ __   __ _  | |_
  \___ \| | '_ \ / _` | |  _|
  ____) | | | | | (_| |_| |
 |_____/|_|_| |_|\__,_(_)_|
'''

for line in figlet.splitlines():
    print(line)
input('\n\n Press enter to exit...')
