########## RADIANS TO DEGREES ##########
num_list = [1, 3, 11, 2, 75, 4, 6, 5, 19, 89]
str_def = input('Choose asc, desc or none: ')

def asc_list():
    num_list.sort()
    print(num_list)

def desc_list():
    num_list.sort(reverse = True)
    print(num_list)
    
if str_def == 'asc':
    asc_list()

elif str_def == 'desc':
    desc_list()
    
elif str_def == 'none':
    print(num_list)