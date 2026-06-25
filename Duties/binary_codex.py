""" ##################################################################################
The following code is native with no AI generated code

Binary Codex - Duty: 1

Time to completion: ~2 hours

What I learned: I originally spent most of my time thinking of if/else cases where
                it would cover 0, less than, equal to, and more than. However, trouble 
                arose in the case of any numbers above 128. I did the binary on paper
                after awhile and realized I have to be able to change/update the user's 
                number in order to deal with that range of numbers. I'd have to subtract
                the iteration from the user's number~ by doing so this also takes care of 
                further 'less than' cases to skip to a relevant iteration. I realized 
                the zero case was redundant if I have a 'more than' statement so I got 
                rid of that. Alas, it dawned on me that combining 'less than' and 
                'equal to' was what matched on my paper representation. This also makes
                complete sense given that the user's number is being updated so it won't
                have to individually compare for equality.

Future implementations: If a non-integer is submitted the program breaks. I need to 
                create a way to check for integers only (try/except?). Once it asks 
                for a number it only asks once more and doesn't actually run the program. 
                I'll need to loop for user input until something is valid. 

    ##################################################################################
"""

def translate_to_binary():
    # Ask for user input
    userInput = int(input(f"\nEnter a number between 0 - 255 to tranlate it to binary\n"))
    
    # Check for integers between 0-255
    if userInput in range(0, 256):
        # reference for binary
        binary_template = [128, 64, 32, 16, 8, 4, 2, 1]
        # final binary output for printing
        binary_number = []
        # helper number ensures the original user input isn't changed
        helper_number = userInput

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

        print(*binary_number, sep='')
    else:
        userInput = int(input(f"\nEnter a number between 0 - 255 to tranlate it to binary\n"))
translate_to_binary()