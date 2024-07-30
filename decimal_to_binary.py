########## DECIMAL TO BINARY ##########

dec_num = int(input('Enter a floating point number of 1024 or lower: '))

def bin_conversion():
    bin_num = bin(dec_num)
    print(bin_num)

if dec_num > 1024:
    print('Float too great! Exiting program')

else:
    bin_conversion()