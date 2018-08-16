#!/usr/bin/python
#Developed by Tiago Neves
#Github: https://github.com/TiagoANeves
#Version: 1.0
#All rights reserved

#Import necessary modules
import string
import random


#Color scheme
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Create Banner
def banner():
    print("""%s

	 _______ _____ _______                                        _  _____ ______ _   _
  	|__   __|  __ \__   __|                                      | |/ ____|  ____| \\ | |
	   | |  | |  | | | |_ __   __ _ ___ _____      _____  _ __ __| | |  __| |__  |  \\| |
    	   | |  | |  | | | | '_ \ / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` | | |_ |  __| | . ` |
           | |  | |__| | | | |_) | (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | |__| | |____| |\\  |
    	   |_|  |_____/  |_| .__/ \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|\\_____|______|_| \\_|
             	           | |
                           |_|%s%s

	# Coded By Tiago Neves
     	# Github https://github.com/TiagoANeves%s
	""" % (bcolors.OKBLUE, bcolors.ENDC, bcolors.FAIL, bcolors.ENDC))


#Getting the info
def get_info():
    global numofpwd
    numofpwd = input('%sHow many passwords do you wanna generate:%s '%(bcolors.OKGREEN, bcolors.ENDC))
    global size
    size = input('%sEnter the password lenght:%s '%(bcolors.OKGREEN, bcolors.ENDC))
    global num_uppercase
    num_uppercase = input('%sHow many upper case characters at least?:%s '%(bcolors.OKGREEN, bcolors.ENDC))
    global num_lowercase
    num_lowercase = input('%sHow many lower case characters at least?:%s '%(bcolors.OKGREEN, bcolors.ENDC))
    global num_especialchars
    num_especialchars = input('%sHow many especial characters at least?:%s '%(bcolors.OKGREEN, bcolors.ENDC))
    global num_number
    num_number = input('%sHow many numbers at least?:%s '%(bcolors.OKGREEN, bcolors.ENDC))

    global total_choice
    total_choice = num_uppercase + num_lowercase + num_especialchars + num_number

    if total_choice > size:
        print('%sThe sum of the characters cant be greater than the password lenght!%s'%(bcolors.FAIL, bcolors.ENDC))
        exit()
    else:
        global size_left
        size_left = size - total_choice

    global especialchars_def
    especialchars_def = "!@#$%&()-_=+[]{}|/?.:;<>\'\"\\"
    global especialchars
    especialchars = raw_input('%sEnter the especial chars allowed in the password ( default:%s %s %s):%s '%(bcolors.OKGREEN, bcolors.WARNING, especialchars_def, bcolors.OKGREEN, bcolors.ENDC))

    if especialchars == "":
        especialchars = especialchars_def

# Random Function
def random_generator(number, chars):
    return ''.join(random.choice(chars) for x in range(number))

# Passowrd Generator
def get_password():
    numbers = random_generator(num_number, string.digits)
    uppercases = random_generator(num_uppercase, string.ascii_uppercase)
    lowercases = random_generator(num_lowercase, string.ascii_lowercase)
    especial_chars = random_generator(num_especialchars, especialchars)

    if size_left > 0:
        chars_left = random_generator(size_left, string.digits + string.ascii_letters + especialchars)
        return  numbers + uppercases + lowercases + especial_chars + chars_left
    else:
        return  numbers + uppercases + lowercases + especial_chars

# Main function
if __name__ == "__main__":
    try:
        banner()
        print('%s%s\nGetting password info...\n%s'%(bcolors.WARNING, bcolors.UNDERLINE, bcolors.ENDC))
        get_info()
    except:
        print('%sError getting the info%s'%(bcolors.FAIL, bcolors.ENDC))
        exit()
 
    print('%s%s\nGenerating password...\n%s'%(bcolors.WARNING, bcolors.UNDERLINE, bcolors.ENDC))
    for x in range(numofpwd):
        temp_password = get_password()
        final_password = ''.join(random.sample(temp_password, len(temp_password)))
        print (final_password)
