########## VOWEL COUNTER ##########

str = str(input('Please input a string to be counted: '))
vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

def vowel_counter():
    vowels_in_string = []
    for char in str:
        if char in vowel_list:
            vowels_in_string.append(char)
    print(len(vowels_in_string))

vowel_counter()