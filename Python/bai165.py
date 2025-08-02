n = input("enter a number: ")
base_from = int(input("enter base of the number (2/8/10/16): "))
base_to = int(input("enter base you want to convert to (2/8/10/16): "))
decimal_number = int(n, base_from)
if base_to == 2:
    result = format(decimal_number, "b")
elif base_to == 8:
    result = format(decimal_number, "o")
elif base_to == 10:
    result = decimal_number
elif base_to == 16:
    result = format(decimal_number, "X")
else:
    result = "base doesn't support!"
print("result:", result)