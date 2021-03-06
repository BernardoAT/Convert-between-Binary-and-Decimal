# ‐*‐ encoding: utf‐8 ‐*‐
#!/usr/bin/python python ‐tt
# .11101 => .90625
# ff_dec2bin(.9296875) = .11101110
# ff_dec2bin(.06640625) = .000100010
# mantissa = .625
# mantissa = .06640625
# mantissa = .906339
# ff_dec2bin(.625) = .101
# ff_dec2bin(mantissa)

""" this program is a transformation from 'n' decimal number to binary number - only mantissa!"""

import math

#list comprehensions: 
sqrt_inv = [ 1/(2.**x) for x in range(1,55) ]


def ff_dec2bin(n):
    
    in_binary = ""
    for number in range(54):
        valor = sqrt_inv[number]       
        if n - valor >= 0:
            in_binary += in_binary.join("1")
            n = n - valor        
        else:
            in_binary += in_binary.join("0")
        if n == 0.0:
            break        
    return "0." + in_binary
