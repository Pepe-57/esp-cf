
import time
import math



#esp-cf dev 1.1
#!DEV VERSION!
#made by Pepe57
#copyright Pepe57 2023-2023

#import webrepl
#webrepl.start()
version = "ESP-CF DEV 1.1"
programs = "Calculator, Settings, SysInfo, Console"

def calculator():
    print("--Calculator--")
    a=input("First number:")
    b=input("Second number:")
    sum=0
    ci=input("Select operation:\n 1.Add\n 2.Subtract\n 3.Multiplication\n 4.Division\n 5.Square root:")
    if int(ci) == 1:
        sum = (int(a) + int(b))
    elif int(ci) == 2:
        sum = (int(a) - int(b))
    elif int(ci) == 3:
        sum = (int(a) * int(b))
    elif int(ci) == 4:
        sum = (int(a) / int(b))
    elif int(ci) == 5:
        sum = math.sqrt(int(a))
    else:
        print("Incorrect operation")
        return
    print(sum)
    ca=input("Would you like to calculate again? y/n:")
    if ca == 'y':
        calculator()
    elif ca == 'n':
        desktop()
    else:
        return
    
    
    
def settings():
    print("--Settings--")
    si=input("Options:\n 1.setting unavailable\n 2.setting unavailable\n 3.null\n 4.Exit to desktop\n 5.Exit to console:")
    if int(si) == 4:
        desktop()
    elif int(si) == 5:
        console()
    else:
        return
        
def sysinfo():
    print("--SysInfo--")
    print("Firmware Version:", version)
    yi=input("Press 'e' to exit to desktop:")
    if yi == 'e':
        desktop()

def console_commands(command):
    if command == "help":
        return "Commands:\n help\n shutdown\n desktop\n restart\n ip\n settings\n systeminfo\n update\n blink 'speed' 'times'\n repeat 'word'\n run 'program'\n programs\n"
    elif command == "shutdown":
        pass
    elif command == "desktop":
        desktop()
    elif command == "restart":
        time.sleep(0.5)
        startup()
    elif command == "ip":
        return "Command unavailable"
    elif command == "settings":
        settings()
    elif command == "systeminfo":
        return "Firmware Version: {}".format(version)
    elif command == "update":
        return "Current version: {}\nTo download the latest version: https://github.com/Pepe-57/esp-cf".format(version)
    elif command.startswith("blink"):
        return "Command unavailable"
    elif command.startswith("repeat"):
        ms = command[7:]
        return ms
    elif command.startswith("run"):
        program = command[4:].strip()
        if program == "calculator":
            calculator()
        elif program == "settings":
            settings()
        elif program == "sysinfo":
            sysinfo()
        elif program == "console":
            console()
        else:
            return "Unknown program. Type 'programs' to see available programs or type with lowercase letters."
    elif command == 'programs':
        return "Available programs:", programs
    else:
        return "Unknown command. Type 'help' for available commands"
def console():
    print("--Console--")
    while True:
        command = input('> ')
        response = console_commands(command)
        print(response)

def desktop():
    print("--Welcome to desktop--")
    i=input("Programs:\n 1.Calculator\n 2.Settings\n 3.SysInfo\n 4.Console\n 5.Shutdown:")
    if int(i) == 1:
        calculator()
    elif int(i) == 2:
        settings()
    elif int(i) == 3:
        sysinfo()
    elif int(i) == 4:
        console()
    elif int(i) == 5:
        pass
    else:
        print("Incorrect program")
        time.sleep(1)
        desktop()
        
    
def startup():
    st=input("Boot to console? y/n:")
    if st == 'y':
        console()
    elif st == 'n':
        pass
    else:
        pass
    print("Welcome to", version)
    time.sleep(0.5)
    print("Processing to desktop..")
    time.sleep(1)
    desktop()
startup()


