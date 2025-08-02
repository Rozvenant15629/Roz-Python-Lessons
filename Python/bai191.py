def is_lowercase(s):
    i = 0
    while i < len(s):
        if s[i].isalpha() and not s[i].islower():
            return False
        i = i + 1
    return True
text = input("enter a string: ")
if is_lowercase(text):
    print("YES")
else:
    print("NO")