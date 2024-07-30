########## X's & O's ##########
string = str(input('Input a string: '))
upper_string = string.upper()

def x_o_counter():
    xs = []
    os = []
    for char in upper_string:
        if char == 'X':
            xs.append(char)
        if char == 'O':
            os.append(char)
    # print(xs)
    # print(os)
    if len(xs) == len(os):
        return True
    else:
        return False

print(x_o_counter())