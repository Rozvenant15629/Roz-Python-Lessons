text = input("enter a string: ")
i = 0
upper_letter = 0
lower_letter = 0
while i < len(text):
    if text[i].isalpha() and text[i].isupper():
        upper_letter += 1
    elif text[i].isalpha() and text[i].islower():
        lower_letter += 1
    i = i + 1
print("Upper letters is:", upper_letter)
print("Lower letters is:", lower_letter)
print("Letters:", upper_letter + lower_letter)