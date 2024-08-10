# Importing necessary modules
import re # Regular expressions module for pattern matching
import subprocess as sp  # Module to run subprocesses like command line tools
import platform  # Module to access underlying platform’s data (e.g., OS)
import sys  # Module to access system-specific parameters and functions
import time  # Module to handle time-related tasks like sleep


# Define variables to store LinkedIn and GitHub profile links, with colored text formatting
LinkedIn = "\n My LinkedIn profile - \033[34m https://www.linkedin.com/in/wooshan-gamage-5b03b91bb/ \033[0m"
Github = " My Github profile   - \033[33m https://github.com/WooshanGamage \033[0m\n"



# Printing an ASCII banner with colored text and author name Wooshan Gamage
print('''
\033[91m
     __  __                                _      _                            _____  _                                      
    |  \/  |                    /\        | |    | |                          / ____|| |                                     
    | \  / |  __ _   ___       /  \     __| |  __| | _ __   ___  ___  ___    | |     | |__    __ _  _ __    __ _   ___  _ __ 
    | |\/| | / _` | / __|     / /\ \   / _` | / _` || '__| / _ \/ __|/ __|   | |     | '_ \  / _` || '_ \  / _` | / _ \| '__|
    | |  | || (_| || (__     / ____ \ | (_| || (_| || |   |  __/\__ \\__ \    | |____ | | | || (_| || | | || (_| ||  __/| |   
    |_|  |_| \__,_| \___|   /_/    \_\ \__,_| \__,_||_|    \___||___/|___/    \_____||_| |_| \__,_||_| |_| \__, | \___||_|   
                                                                                                            __/ |            
                                                                                                           |___/          
                                                                                                        \033[0m
                                                                         \033[92m - Wooshan Gamage ( Team Encryptix )\033[0m                      \n''')


# Checking if the script is being run on a Windows system
if platform.system().lower() == "windows":
    # Display message if the OS is Windows and exit
    print("This program is not compatible with Windows machines\n")
    time.sleep(1) # Pause for 1 second
    print(LinkedIn)   # Print LinkedIn profile link
    time.sleep(1)  # Pause for 1 second
    print(Github)  # Print GitHub profile link
    time.sleep(1)  # Pause for 1 second
    sys.exit()  # Exit the program


# Function to change MAC address of the specified network interface
def change_mac(interface, new_mac):
    # Inform the user about the MAC address change
    print(f"\n[+] Changing MAC address for \033[92m{interface}\033[0m to \033[92m{new_mac}\033[0m")
    # Execute commands to bring the interface down, change MAC, and bring it up again
    sp.call(["ifconfig", interface, "down"])  # Bring the interface down
    sp.call(["ifconfig", interface, "hw", "ether", new_mac])  # Change MAC address
    sp.call(["ifconfig", interface, "up"])  # Bring the interface up




# Function to get the current MAC address of the specified network interface
def get_current_mac(interface):
    try:
        # Run ifconfig command on the interface and decode the output
        ifconfig_result = sp.check_output(["ifconfig", interface]).decode('utf-8')
        # Use regular expression to search for MAC address pattern
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)


        # If MAC address is found, return it
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] MAC address not found")
            return None
    except sp.CalledProcessError as e:
        # Handle the case where ifconfig command fails
        print(f"[-] Error fetching interface information for {interface}: {e}")
        return None


# Interactive loop to get valid network interface input from the user
while True:
    # Ask user to input network interface name (e.g., eth0, wlan0)
    interface = input("Enter interface to change MAC [eth0, wlan0]: ")
    # Check if the entered interface is valid
    if interface != "eth0" and interface != "wlan0":
        print("You are not selected a right interface ")
    else:
        break # Break loop if valid interface is provided


# Ask user to input the new MAC address
new_mac = input("Enter the new MAC address: ")


# Get and display the current MAC address of the interface
current_mac = get_current_mac(interface)
if current_mac:
    print(f"\nCurrent MAC address = \033[92m{current_mac}\n\033[0m")

    # Call the function to change the MAC address
    change_mac(interface, new_mac)


    # Verify if the MAC address was successfully changed
    current_mac = get_current_mac(interface)
    if current_mac == new_mac:
        time.sleep(2)  # Pause for 2 seconds
        print(f"[+] MAC address successfully changed to \033[92m{current_mac}\033[0m")
    else:
        print("[-] MAC address did not change.")
else:
    print(f"[-] Could not change MAC address for {interface}")


# Print LinkedIn and GitHub profiles again before exiting
time.sleep(1)
print(LinkedIn)
time.sleep(1)
print(Github)
time.sleep(1)
