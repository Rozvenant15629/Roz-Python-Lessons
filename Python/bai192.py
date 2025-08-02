text = input("enter any string: ")
numbers = 0
upper_letters = 0
lower_letters = 0
special_characters = 0
i = 0
while i < len(text):
    if text[i].isalpha() and text[i].isupper():
        upper_letters = upper_letters + 1
    elif text[i].isalpha() and text[i].islower():
        lower_letters = lower_letters + 1
    elif text[i].isdigit():
        numbers = numbers + 1
    else:
        special_characters = special_characters + 1
    i = i + 1
letters = upper_letters + lower_letters
characters = numbers + upper_letters + lower_letters + special_characters
print("Letters:", letters)
print("numbers:", numbers)
print("Upper letters:", upper_letters)
print("Lower letters:", lower_letters)
print("special characters in string is:", special_characters)
print("Characters in string:", characters)
    