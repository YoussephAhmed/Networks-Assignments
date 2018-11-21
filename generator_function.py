

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




def generator(key,message):
    key=to_decimal(key)
    message=to_decimal(message)
    remainder=message%key
    remainder=int(bin(remainder)[2:])
    return  remainder


if __name__ == '__main__':
    print(to_decimal(110))