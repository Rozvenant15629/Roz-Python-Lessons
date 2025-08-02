def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = input("enter a string: ")
if is_palindrome(n):
    print("True")
else:
    print("False")