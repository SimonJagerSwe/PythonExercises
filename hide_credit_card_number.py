########## VOWEL COUNTER ##########

card_number = str(input('Enter your 16 digit credit card number: '))
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if len(card_number) != 16:
    print('Wrong card number. Terminating')

def number_hider():
    first_12 = card_number[:12]
    # print(first_12)
    final_4 = card_number[12:]
    # print(final_4)
    hidden_12 = len(first_12) * 'X'
    # print(hidden_12)    
    final_numbers = str(hidden_12 + final_4)
    print(final_numbers)

number_hider()