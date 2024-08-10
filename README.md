# Automated MAC Address Changer

## Overview
The Automated MAC Address Changer is a Python-based utility designed to enhance network security by allowing users to modify the MAC address of their network interfaces. This tool is developed for Linux-based systems and provides an easy-to-use command-line interface to change the MAC address, which can be used to anonymize a device on a network or bypass certain network restrictions.

## Features
- Change the MAC address of network interfaces
- Simple command-line interface
- Utilizes Python's subprocess module for system command execution
- Regular expressions to parse network interface data
- Supports multiple network interfaces, including wired (eth0) and wireless (wlan0)

## Installation
1. Ensure you have Python installed on your system.
2. Clone this repository:
    ```bash
    git clone https://github.com/WooshanGamage/MAC_Address_Changer.git
    ```
3. Navigate to the project directory:
    ```bash
    cd MAC_Address_Changer
    ```

## Usage
1. Run the script with root privileges:
    ```bash
    sudo python3 mac_address_changer.py
    ```
2. Follow the command-line prompts to:
    - Select a network interface (e.g., eth0, wlan0)
    - Enter the new MAC address in the correct format

## System Requirements
- Linux-based operating system
- Python 3.x

## How It Works
1. **User Interface**: A command-line prompt guides the user through selecting a network interface and entering a new MAC address. Input validation ensures correct format and valid interface selection.
2. **MAC Address Retrieval**: The `ifconfig` command is executed using the subprocess module to obtain the current MAC address, which is then processed using regular expressions.
3. **MAC Address Modification**: The utility executes a series of commands to change the MAC address:
    - `ifconfig interface down`
    - `ifconfig interface hw ether new_mac`
    - `ifconfig interface up`
4. **Error Handling**: The utility checks for issues like invalid interface names, incorrectly formatted MAC addresses, and command execution failures, providing clear error messages.

## Limitations
- Designed for Linux-based systems; may not be compatible with Windows.
- Requires root privileges to modify MAC addresses.

## Future Work
- Extend compatibility to other operating systems.
- Explore alternative methods for MAC address modification that do not require root access.
- Add features like MAC address randomization.

## Authors
- M.G. Wooshan Rukmal Gamage

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Special thanks to my parents for their unwavering support and to my team, Encryptix, including Wathsala Dewmina, Rivindu Ahinsa, and Lakindu Minosha, for their insightful discussions and motivation.

## References
For more information, please refer to the [thesis document](./Mac_address_changer.pdf).

---

**LinkedIn**: [Wooshan Gamage](https://www.linkedin.com/in/wooshan-gamage-5b03b91bb/)  
**GitHub**: [WooshanGamage](https://github.com/WooshanGamage)
