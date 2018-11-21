import re

def to_decimal(bin_value):
    bin_value=str(bin_value)
    decimal_value=0
    digit=len(bin_value)-1
    for n in bin_value:
        if(n=='1'):
            decimal_value+=2**digit
            digit-=1
        else:
            continue
    return  decimal_value




def generator(message,key):
    message = re.sub('\n', '', message)
    old_message = message
    n = len(key) - 1
    extra_bits = ''
    for i in range (n-1):
        extra_bits = extra_bits + '0'

    message = message + extra_bits
    key = int(key)
    message = int(message)
    key=to_decimal(key)
    message=to_decimal(message)
    remainder=message % key
    remainder=int(bin(remainder)[2:])
    old_message = str(old_message)
    remainder = str(remainder)
    trans_message = old_message + remainder
    return remainder, trans_message
