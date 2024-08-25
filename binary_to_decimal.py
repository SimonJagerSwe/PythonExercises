########## CONVERT BINARY TO DECIMAL ##########
binary = bin(input(print('Enter a binary number: ')))

def bin_to_dec(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

print(bin_to_dec())