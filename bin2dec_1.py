# ‐*‐ encoding: utf‐8 ‐*‐
#!/usr/bin/python python ‐tt
# 1011.11101 => 11.90625
# ff_bin2dec("1100011.1110111")
# ff_bin2dec("1011.11011")
# ff_bin2dec("11100.0110110001100010001")

import math
#import sys

def ff_bin2dec(n):                      # 'n' is an string

    neg = False
    if n[0] == '-':
        n, neg = n[1:], True            # checks whether the number is negative

    if n.count('.') == 0:               # If there is no decimal places
        inteiro = n
    elif n.count('.') == 1:             #
        index_ponto = n.find('.')
        inteiro = n
        inteiro = inteiro[:index_ponto]
        mantissa = n[index_ponto + 1:]
    else:
        break

    soma, som = 0., 0.
    
    if mantissa:    
        mantissa = str(format(mantissa, '.24'))
        for nun in range(len(mantissa)):
            if mantissa[nun] != '0':
                soma += 1./math.pow(2., (nun + 1))
        soma = str(soma)[2:]

    if inteiro:
        inteiro = inteiro[::-1]
        for unu in range(len(inteiro)):
            if inteiro[unu] != '0':
                som += math.pow(2., unu)
        som = str(som)[:-2]
        inteiro = inteiro[::-1]
        
    if som == 0: som = '0'
    if soma == 0: soma = '0'
    return ('-' if neg else '') + "{0:s}.{1:.12s}".format(som, soma)
