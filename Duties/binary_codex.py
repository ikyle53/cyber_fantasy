""" 
##################################################################################
The following code is native with no AI generated code

Binary Codex - Duty: 1
##################################################################################
"""
# Program Start
# ---------------------------------------------------------------------------------------
def start_program():
    userInput = input("Please submit option 1 or 2:\n" \
    "1: Convert decimal to binary\n" \
    "2: Convert binary to decimal\n")

    if userInput == "1":
        translate_to_binary()
    elif userInput == "2":
        translate_to_decimal()
    else:
        start_program()

# Translation from decimal to binary
# ----------------------------------------------------------------------------------------
def translate_to_binary():
    # Ask for user input
    userInput = input(f"\nEnter a number between 0 - 255 to tranlate it to binary\n")
    
    # Check for integers between 0-255
    if userInput.isalpha():
        print(f"Number submitted isn't within the range of 0-255\n")
        start_program()
    elif int(userInput) in range(0, 256):
        # reference for binary
        binary_template = [128, 64, 32, 16, 8, 4, 2, 1]
        # final binary output for printing
        binary_number = []
        # helper number ensures the original user input isn't changed
        helper_number = int(userInput)

        """
        The following for loop iterates through the binary_template and compares each
        number in the iteration to the user's submitted number (helper_number).

        First: Checks to see if the number in the iteration is less than or equal to 
               the helper_number. If it IS less than or equal to the helper_number it 
               will then subtract the number in the iteration from the helper_number.
               Afterwards it appends a 1 to the binary_number list.

        Second: Checks to see if the number in the iteration is greater than the
                helper_number. If it IS greater than the helper_number it will append
                a 0 to the binary_number list.
        """
        
        for x in binary_template:
            # First
            if x <= helper_number:
                helper_number = helper_number - x
                binary_number.append(1)
            # Second
            elif x > helper_number:
                binary_number.append(0)
        print("********************************************")
        print(f"{userInput} converts to:")
        print(*binary_number, sep='')
        print(f"********************************************\n")
    start_program()

# Translation from binary to decimal
# ---------------------------------------------------------------------------------------------
def translate_to_decimal():
    userInput = input(f"\nEnter an 8-bit binary number to convert to decimal\n")
    binary_helper = userInput
    binary_template = [128, 64, 32, 16, 8, 4, 2, 1]
    decimal_number = 0

    """
    This for loop uses the built in zip() method to iterate over
    both the binary_template array and the user's input. This is
    based off of the 8bit decimal and won't work outside of that.
    I added a check to make sure the binary is 1, 0, and a length
    of 8 digits. Outside of that it will return to program start.
    """

    for index1, index2 in zip(binary_helper, binary_template):
        if index1 == "1" and len(binary_helper) == 8:
            print("if1 = 1")
            decimal_number = decimal_number + index2
        elif index1 == "0" and len(binary_helper) == 8:
            print("if2 = 0")
            pass
        elif len(index1) < 8:
            print(f"The binary entered wasn't 8 digits long or wasn't a number\n")
            start_program()

    print("********************************************")
    print(f"\n{userInput} converts to: \n{decimal_number}\n")
    print("********************************************")

    start_program()

start_program()
