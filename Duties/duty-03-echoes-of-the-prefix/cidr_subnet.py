def generate_cidr_subnet():
    user_input = input(f"Enter any IP address in the format of 192.168.1.50/17\n")

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
    bit_mask = gen_bit_mask(int_prefix)
    print(f"Default subnet mask: {bit_mask}")

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

    return final_decimal
    
generate_cidr_subnet()
