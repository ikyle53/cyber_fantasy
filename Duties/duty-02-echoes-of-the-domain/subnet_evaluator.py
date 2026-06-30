""" 
##################################################################################
The following code is native with no AI generated code

Subnet evaluator - Duty: 2
##################################################################################
"""

# Program Start
# ---------------------------------------------------------------------------------------
def start_program():
    userInput = input("Please submit an IP address for subnet evaluation:\n") # 192.12.6.45
    ip_addr = userInput

    """
    1. Take an IP address and split it into 4 different parts using the "." 
    as the seperator.
    2. Convert the 4 parts to integers.
    3. Validate the integers between the range of 0-255
    """

    # Split the IP address into 4 different parts
    ip_split = ip_addr.split(".")

    # Convert the split IP address to intergers - using the pythonic way
    int_split = [int(i) for i in ip_split]
    
    # Validation of the IP address as integers between 0 and 255
    for i in int_split:
        if i in range(0, 256):
            pass
        else:
            print(f"{i} needs to be within range of 0-255")
            start_program()

# Function calls for subnet evaluation ----------------

    # Retreive the IP's class and CIDR notation
    # -------------------------------------------------
    ip_class, cidr_notation = determine_class(int_split)

    # Retrieve the default subnet mask
    # -------------------------------------------------
    subnet_mask = get_default_subnet_mask(cidr_notation)

    # Retreive the network address
    # -------------------------------------------------
    network_address = get_network_address(cidr_notation, int_split)

    # Retreive the broadcast address
    # -------------------------------------------------
    broadcast_address = get_broadcast_address(cidr_notation, int_split)

    # Retreive the last host address
    # -------------------------------------------------
    last_host_address = get_last_host_address(cidr_notation, int_split)

    # Print the evaluation attributes of the given IP
    print(f"\nClass: {ip_class}\n"
          f"CIDR: {cidr_notation}\n"
          f"Def Subnet Mask: {subnet_mask}\n"
          f"Network Address: {network_address}\n"
          f"Broadcast Address: {broadcast_address}\n"
          f"Last Host Address: {last_host_address}")


# ----------------------------Functions for evaluation ----------------------------------

# Determine class
# -------------------------------------------------------------------------------
# Checks number ranges to determine the class of the IP address. Then it returns
# the class letter and the CIDR notation for calcuation.
def determine_class(ip_list):
    if ip_list[0] in range(0, 128):
        return "A", 8 
    elif ip_list[0] in range(128, 192):
        return "B", 16
    elif ip_list[0] in range(192, 224):
        return "C", 24
    elif ip_list[0] in range(224, 240):
        return "D", 1
    elif ip_list[0] in range(240, 256):
        return "E", 1
# Determine default subnet mask
# ----------------------------------------------------------------------------------
# Takes the class from determine_class() and returns a default subnet mask.
def get_default_subnet_mask(cidr):
    if cidr == 8:
        return "255.0.0.0"
    elif cidr == 16:
        return "255.255.0.0"
    elif cidr == 24:
        return "255.255.255.0"
    elif cidr == 1:
        return "No subnet mask for these."

# Determine the network address
# -------------------------------------------------------------------------------
# Takes the CIDR notation of the IP and configures the network address
def get_network_address(cidr, ip):
    temp_ip = ip.copy() # Copy so I don't change the original IP address input

    """
    The if statements below take the classes and replaces 
    all numbers with 0's based on the class. "[1:], [2:],
    [3:]" Points to the index and replaces the rest of the
    list with 0's. "[0] * (len(temp_ip) - number) is a 
    memory effiecient way to replace items in a list. It 
    says "Take 0 and replace the number * the length of the list
    minus it's index" For instance, class B would replace
    numbers with 0 * (4-2) for a total of 2 replaced numbers.
    """
    if cidr == 8:
        temp_ip[1:] = [255] * (len(temp_ip) - 1)
        temp_ip[-1] = 254
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 16:
        temp_ip[2:] = [255] * (len(temp_ip) - 2)
        temp_ip[-1] = 254
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 24:
        temp_ip[3:] = [255] * (len(temp_ip) - 3)
        temp_ip[-1] = 254
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 1:
        return "No broadcast address for these."
    
# Determine the broadcast address
# --------------------------------------------------------------------------------
# Takes the CIDR notation of the IP and configures the network address
def get_broadcast_address(cidr, ip):
    temp_ip = ip.copy() # Copy so I don't change the original IP address input

    if cidr == 8:
        temp_ip[1:] = [255] * (len(temp_ip) - 1)
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 16:
        temp_ip[2:] = [255] * (len(temp_ip) - 2)
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 24:
        temp_ip[3:] = [255] * (len(temp_ip) - 3)
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 1:
        return "No broadcast address for these."
    
# Determine the last host address
# --------------------------------------------------------------------------------
# Takes the CIDR notation of the IP and configures the network address
def get_last_host_address(cidr, ip):
    temp_ip = ip.copy() # Copy so I don't change the original IP address input

    if cidr == 8:
        temp_ip[1:] = [254] * (len(temp_ip) - 1)
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 16:
        temp_ip[2:] = [254] * (len(temp_ip) - 2)
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 24:
        temp_ip[3:] = [254] * (len(temp_ip) - 3)
        stringify = '.'.join(map(str, temp_ip))
        return stringify
    elif cidr == 1:
        return "No broadcast address for these."

start_program()
