def generate_cidr_subnet():
    user_input = input(f"Enter any IP address in the format of 'xxx.xxx.xxx.xxx/xx' (ex: 175.1.1.50/17)\n")

# Parse the input ---------------------------
    # First, split the prefix from the octets
    ip_split, prefix = user_input.split('/')

    # Second, split the octets while the prefix is split. Convert to int.
    octet_split = [int(i) for i in ip_split.split('.')]

    # Convert the prefix to integer for validation
    int_prefix = int(prefix)

# Validation --------------------------------
    # Validate the octets from ranges of 0-255
    for i in octet_split:
        if i in range(0, 256):
            pass
        else:
            print(f"{i} wasnt within the range of 0-255\n")
            generate_cidr_subnet()

# Generate the subnet mask ------------------
    # Create a 32-bit mask
    bit_mask, decimal_mask = gen_bit_mask(int_prefix)
    print(f"\nDefault subnet mask: {bit_mask}")

# Generate the network address --------------
    network_address, first_host = gen_net_address(octet_split, decimal_mask)
    print(f"Network address: {network_address}")

# Generate the broadcast address ------------
    broadcast_address, last_host = gen_broadcast_address(octet_split, decimal_mask)
    print(f"Broadcast address: {broadcast_address}")

# First and last host
    print(f"First host: {first_host}")
    print(f"Last host: {last_host}")

# Generate the number of hosts available ----
    hosts = usable_hosts(int_prefix)
    print(f"Usable hosts: {hosts}")

# ---------------------------------------------------------------------------------------
def gen_bit_mask(cidr):

    # Binary representation of the CIDR notation
    binary_number=[]

    # Create a binary representation of the CIDR notation
    for i in range(cidr):
        binary_number.append("1")
    for i in range(32-cidr):
        binary_number.append("0")

    # Create octets: range 0-32 and creates octets every 8 digits 
    binary_string_octets = [binary_number[i:i + 8] for i in range(0, 32, 8)]

    # Convert to integer, List comprehension to join the octets, use int() built in method to convert binary to decimal :)
    decimal_octets = [int(''.join(octet), 2) for octet in binary_string_octets]

    # Join all the decimals for readability
    final_decimal = ".".join(map(str, decimal_octets))

    return final_decimal, decimal_octets

# ----------------------------------------------------------------------------------------
def gen_net_address(ip, subnet):

    # Take the list indexes, shift them according to a 32 bit integer format.
    ip_32bit = ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3] # Now = a 32bit number

    # Do the same for the subnet as above and convert to a 32 bit integer
    subnet_32bit = subnet[0] << 24 | subnet[1] << 16 | subnet[2] << 8 | subnet[3] # Now = a 32bit number

    # Compare bit by bit the ip and subnet
    """
    Using the bitwise & operator it compares the two 32 bit numbers. If the subnet has a 1 in its
    bit it keeps the ip bit. Where the subnet has a 0 it sets the result of ip to 0. This zeros out
    the host bits and only leaves the network bits.
    """
    network_32bit = ip_32bit & subnet_32bit

    # Unpack the results into readable numbers. It shifts the octets back to to 8 bits.
    # & 255 keeps only the lowest 8 bits (like 01100001)
    network_address = [
        (network_32bit >> 24) & 255,
        (network_32bit >> 16) & 255,
        (network_32bit >> 8) & 255,
        network_32bit & 255
    ]

    # generates the first host
    first_host = [
        (network_32bit >> 24) & 255,
        (network_32bit >> 16) & 255,
        (network_32bit >> 8) & 255,
        (network_32bit & 255) + 1
    ]
    
    final_network_address = ".".join(map(str, network_address))
    final_first_host = ".".join(map(str, first_host))
    return final_network_address, final_first_host

def gen_broadcast_address(ip, subnet):
    ip_32bit = ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3] # Now = a 32bit number

    # Do the same for the subnet as above and convert to a 32 bit integer
    subnet_32bit = subnet[0] << 24 | subnet[1] << 16 | subnet[2] << 8 | subnet[3] # Now = a 32bit number

    # Compare bit by bit the ip and subnet
    network_32bit = ip_32bit & subnet_32bit

    # Change the bits using bitwise OR comparing with NOT
    # Additionally, NOT can cause numbers to grow so it will need addtional
    # help to stay in the 32 bit range using "& 0xFFFFFFFF"
    broadcast_32bit = network_32bit | (~subnet_32bit & 0xFFFFFFFF)

    # Unpack the broadcast address
    broadcast_address = [
        (broadcast_32bit >> 24) & 255,
        (broadcast_32bit >> 16) & 255,
        (broadcast_32bit >> 8) & 255,
        broadcast_32bit & 255
    ]

    # generstes the last host
    last_host = [
        (broadcast_32bit >> 24) & 255,
        (broadcast_32bit >> 16) & 255,
        (broadcast_32bit >> 8) & 255,
        (broadcast_32bit & 255) - 1
    ]

    final_broadcast_address = ".".join(map(str, broadcast_address))
    final_last_host = ".".join(map(str, last_host))
    return final_broadcast_address, final_last_host

def usable_hosts(cidr):
    return (2**(32-cidr))-2

generate_cidr_subnet()
