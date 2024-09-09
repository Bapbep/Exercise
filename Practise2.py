string = input("Enter a string: ")
if string.isalpha():
    print("The string is made up only of alphabets.")
else:
    print("The string contains characters other than alphabets.")
    string = input("Enter a string: ")
if string.isalnum():
    print("The string is made up of alphabets and/or numbers.")
else:
    print("The string contains characters other than alphabets and numbers.")
    string = input("Enter a string: ")
if any(char.isdigit() for char in string) and any(char.isalpha() for char in string):
    print("The string contains both alphabets and at least one number.")
else:
    print("The string must contain both alphabets and at least one number.")
    import string as str_lib

special_characters = str_lib.punctuation
user_input = input("Enter a string: ")

if (any(char.isdigit() for char in user_input) and 
    any(char.isalpha() for char in user_input) and 
    any(char in special_characters for char in user_input)):
    print("The string contains alphabets, numbers, and at least one special character.")
else:
    print("The string must contain alphabets, numbers, and at least one special character.")
    import string as str_lib

special_characters = str_lib.punctuation

while True:
    user_input = input("Enter a valid string: ")
    if (any(char.isdigit() for char in user_input) and 
        any(char.isalpha() for char in user_input) and 
        any(char in special_characters for char in user_input)):
        print("Valid string entered!")
        break
    else:
        print("Invalid input. Please enter a string with alphabets, numbers, and at least one special character.")