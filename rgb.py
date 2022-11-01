"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""

#my_solution

def rgb(r, g, b):
    args = [r, g, b]
    hex_value = []
    for x in args:
        if x < 0:
            hex_value.append(hex(0))
        elif x > 255:
            hex_value.append(hex(255))
        else:
            hex_value.append(hex(x))

    return "".join([x.replace("x","").upper() if len(x)==3 else x[-2:].upper() for x in hex_value])

#another solutions

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

