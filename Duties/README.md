# DUTY COMMENCE - Duty 01: Binary Codex

>“Before I could read the deeper secrets of the network, I first had to understand the ancient language of bits and bytes. This simple codex allows me to translate between the binary runes and their decimal meaning.”

### Why binary matter (and why I'm learning it)
At its core, binary is just an on and off system like a light switch. Computers use electricity and electricity is either flowing or it isn’t. So everything a computer does ultimately comes down to these two states. That’s why we use base-2 (binary [0 or a 1] ) instead of the decimal system we’re used to. There's other systems out there but this one takes the cake for simplicity reasons. 0s and 1s are used to represent letters, numbers, images, network addresses, instructions for the CPU, and even the packets flying across the internet. I realized that being able to understand what these bits/bytes actually mean would help me a lot.

### The build
I built this using plain Python (no external libraries). The script takes a number between 0 and 255 from the user and converts it into its binary equivalent. It also takes an 8bit binary (10101010) and converts it to a decimal.

I used a `for` loop that compares the user’s number against the binary place values in descending order: `128, 64, 32, 16, 8, 4, 2, 1`. If the current number is greater than or equal to the place value, it adds a `1` and subtracts that value from the total. Otherwise it adds a `0`.

I used another `for` loop in conjunction with the zip() method to iterate throguh the binary place values of `128, 64, 32, 16, 8, 4, 2, 1` and the binary value the user submits (example: 10101010). It looks for each `1` in the binary number and adds the corresponding binary place value to get the decimal number.

### After action report
I re-established my working knowledge of the `for` loop and caught on pretty quickly. At first I overcomplicated it, I was trying to write logic for every possible case (`==`, `<`, `>`, and handling zero separately). After writing out a few conversions by hand on paper I realized I only needed two conditions if I updated the remaining value after each step. After ~2 hours total I finally got a working converter with no mistakes.

For the binary to decimal logic it was a bit easier but I kept hitting snags with type errors when it came to using the `len()` method. I now know that `input()` automatically converts it to a string type. Additionally I used the `and` operator to help with validation of the user's input. This helped shorten my validation if statements. Lastly, the built in `zip()` method was just what I need to iterate through both the user's input and the binary values to get the right numbers added.

#### Future improvements
- Add additional validation with another library or extensive exclusions using native methods.
- Make a UI for better user experience
