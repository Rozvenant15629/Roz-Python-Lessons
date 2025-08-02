def symmetric(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
n = input("enter a number (can be 0b, 0o, 0x or decimal): ")
i = int(n, 0)
decimal = str(i)
binary = format(i, "b")
octal = format(i, "o")
hexadecimal = format(i, "X")
print("Decimal is:", decimal)
print("Binary is:", binary)
print("Octal is:", octal)
print("Hexadecimal:", hexadecimal)
for a in (decimal, binary, octal, hexadecimal):
    if symmetric(a):
        print(a, "is symmetric!")
    else:
        print(a, "is not symmetric!")
largest = ""
for base, value in [("Decimal", decimal), ("Binary", binary), ("Octal", octal), ("Hexadecimal", hexadecimal)]:
    if symmetric(value):
        largest = f"{base}, ({value})"
if largest:
    print("Largest symmetric base:", largest)
else:
    print("No symmetric base founded")
