import machine
import time
import math
import esp
import sys
from machine import Pin
import network

#esp-os dev 1.0
#!DEV VERSION!
#made by Pepe57
# Copyright Pepe57 2023-2023

#import webrepl
#webrepl.start()
ap_if = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)

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
    si=input("Options:\n 1.Change CPU clockspeed\n 2.Wifi settings\n 3.null\n 4.Exit to desktop:")
    if int(si) == 1:
        print("-CPU Settings-")
        oc=input(" 1.80MHz Normal\n 2.160MHz Overclock:")
        if int(oc) == 1:
            machine.freq(80000000)
            print("Clockspeed changed to 80MHz")
            settings()
        elif int(oc) == 2:
            machine.freq(160000000)
            print("Clockspeed changed to 160MHz")
            settings()
        else: return
    elif int(si) == 2:
        print("-WiFi settings-")
        wi=input(" 1.Enable WiFi\n 2.Disable WiFi\n 3.Connect to WiFi network:")
        if int(wi) == 1:
            ap_if.active(True)
            settings()
        elif int(wi) == 2:
            ap_if.active(False)
            settings()
        elif int(wi) == 3:
            ssid=input("SSID:")
            wpas=input("Password:")
            sta_if.connect(ssid, wpas)
            settings()
        else: return
    elif int(si) == 4:
        desktop()
    else:
        return
        
def sysinfo():
    print("--SysInfo--")
    print("OS Version: ESP-OS DEV 1.0")
    print("Free memory:",gc.mem_free(),'bytes')
    print("CPU clockspeed:",machine.freq(),"Hz")
    yi=input("Press 'e' to exit:")
    if yi == 'e':
        desktop()

def console_commands(command):
    if command == "help":
        return "Commands:\n help\n shutdown\n desktop\n restart\n ip\n settings\n systeminfo\n"
    elif command == "shutdown":
        sys.exit()
    elif command == "desktop":
        desktop()
    elif command == "restart":
        time.sleep(0.5)
        startup()
    elif command == "ip":
        return ap_if.ifconfig()
    elif command == "settings":
        settings()
    elif command == "systeminfo":
        print("OS Version: ESP-OS DEV 1.0")
        print("Free memory:",gc.mem_free(),'bytes')
        print("CPU clockspeed:",machine.freq(),"Hz")
    else:
        print("Unknown command. Type 'help' for available commands")
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
        sys.exit()
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
    print("Welcome to ESP-OS DEV 1.0")
    time.sleep(0.5)
    print("Processing to desktop..")
    time.sleep(1)
    desktop()
startup()


