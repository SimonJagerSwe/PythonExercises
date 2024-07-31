########## REPEAT CHARACTERS ##########
single_string = str(input('Enter a string to be doubled: '))

def string_doubling():
    double_string = []
    for char in single_string:
        double_string.append((char * 2))
        double_string2 = ''.join(double_string)
    print(double_string2)

print(single_string)
string_doubling()