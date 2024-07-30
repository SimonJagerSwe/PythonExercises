########## VOWEL COUNTER ##########

card_number = str(input('Enter your 16 digit credit card number: '))
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if len(card_number) != 16:
    print('Wrong card number. Terminating')

def number_hider():
    first_12 = card_number[:12]
    # print(first_12)
    hidden_numbers = []
    for num in first_12:
        if num in numbers_list:
            hidden_numbers.append(num)
    hidden_numbers.replace(num, 'X')
    print(hidden_numbers)

number_hider()