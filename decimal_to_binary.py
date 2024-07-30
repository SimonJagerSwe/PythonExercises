########## DECIMAL TO BINARY ##########

dec_num = float(input('Enter a floating point number of 1024 or lower: '))

def bin_conversion():
    float(bin_num = bin(dec_num))
    print(dec_num)

if dec_num > 1024:
    print('Float too great! Exiting program')

else:
    bin_conversion()

