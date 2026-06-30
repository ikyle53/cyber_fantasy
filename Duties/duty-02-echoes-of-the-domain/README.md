# DUTY COMMENCE — Duty 02: Echoes of the Domain

> “Every domain has a shape, even if it cannot be seen. By listening to its echoes, I learned to trace its borders, find where it begins and ends, and understand who may dwell within it.”

### Why I Built This

Many people find subnetting intimidating or even something they want to avoid. However, understanding how to evaluate an IP address is foundational for mapping the logical shape and boundaries of a network. 

This tool reveals key information about a network:
- Where the network begins (Network Address)
- Where the network ends (Broadcast Address)
- Which addresses are usable by devices (Last Host Address)
- How the network is divided by default (based on IP Class)

It helps determine the territory of a digital domain: borders, size, and usable space. This is foundational reconnaissance work for anyone exploring or securing networks.

### The Build

This was built using native Python 3 with no external modules or libraries.

### How It Works

A user submits an IP address and the program determines its class along with the default subnet mask, network address, broadcast address, and last usable host address. Classes D and E are handled as edge cases with appropriate messages since they don't use traditional subnet masks in the same way.

### After Action Report

This project was one of the best learning experiences I’ve had so far regarding how functions pass data to each other. I gained a much clearer understanding of how to send information between functions using parameters and how to receive results using return values.

I also improved my skills with type conversion, joining lists into strings, and replacing sections of lists. One particularly useful technique I discovered was this memory efficient way to replace items in a list:

```python
list[1:] = [0] * (len(list) - 1)
