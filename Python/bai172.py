n = input("enter a number (can be 0b, 0o, 0x or decimal): ")
decimal = int(n, 0)
print("binary base is:", format(decimal, "b"))
print("octal base is:", format(decimal, "o"))
print("decimal base is:", str(decimal))
print("hexadecimal base is:", format(decimal, "X"))
def symmetric(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
if symmetric(format(decimal, "b")):
    print(format(decimal, "b"), "is symmetric")
else:
    print(format(decimal, "b"), "is not symmetric")
if symmetric(format(decimal, "o")):
    print(format(decimal, "o"), "is symmetric")
else:
    print(format(decimal, "o"), "is not symmetric")
if symmetric(str(decimal)):
    print(str(decimal), "is symmetric")
else:
    print(str(decimal), "is not symmetric")
if symmetric(format(decimal, "X")):
    print(format(decimal, "X"), "is symmetric")
else:
    print(format(decimal, "X"), "is not symmetric")