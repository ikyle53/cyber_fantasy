# DUTY COMMENCE — Duty 03: Echoes of the prefix

> I once mapped domains through slow and careful steps, counting bits one by one. Then I met a [fellow scholar](https://richardkilleen.co.uk/blog/python/python-bitwise-operators/) who showed me the hidden language of bitwise operations. What had once felt like tedious labor suddenly became precise and swift as if the borders of every realm revealed themselves at a single command. With this new art I could carve the true shape of any domain with clarity and speed.

### Why I Built This
Subnetting has a reputation for being difficult and I wanted to truly understand it rather than just memorize rules. I realized that to build something meaningful I first needed to understand how IP addresses are constructed at the binary level. After learning binary and discovering bitwise operations I finally understood how routers and networks actually calculate addresses. This tool lets me take any IP address with a CIDR prefix and reveal its network boundaries, subnet mask, and host information.

### The Build
This was built using native Python 3 with no external modules or libraries. It makes heavy use of bitwise operations to calculate network and broadcast addresses efficiently.

### How It Works
The program accepts an IP address in CIDR notation (for example `192.168.1.50/24`). It then:
- Generates the correct subnet mask from the prefix length
- Uses bitwise AND to calculate the network address
- Calculates the broadcast address
- Determines the usable host range and the total number of available hosts

### After Action Report
This project was a big step forward from my previous subnetting tool. Learning bitwise operations completely changed how I approach these calculations. Instead of manually counting bits or using slow loops I can now shift and compare bits directly to find network and broadcast addresses with just a few operations.

The biggest realization was understanding how routers actually work under the hood. It felt abstract but now feels logical and useful. I’m especially proud of moving from basic string/list manipulation in earlier duties to using proper bitwise logic here. It feels like I leveled up in both networking knowledge and Python skill at the same time.

I still have more to add (full host range calculation, special handling for /31 and /32, and better input validation), but the core bitwise foundation is now in place.
