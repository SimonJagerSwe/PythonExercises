########## JUST THE NUMBERS ##########
mixed_list = ['My name is Simon and I\'m 34, I mean Thirtyfour, Years old', 34, 'ABCD', 1, 35, '0', 'CLANGGG', 11]

def just_numbers():
    int_list = []
    for _ in mixed_list:
        if isinstance(_, int):
            int_list.append(_)
    print(int_list)

# print(mixed_list)
just_numbers()