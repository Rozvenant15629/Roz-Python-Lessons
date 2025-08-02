n = input("enter a float number: ")
if '.' in n:
    decimal_parts = str(n).split(".")[1]
    decimal_parts = decimal_parts.rstrip("0")
    count = sum(1 for ch in decimal_parts if ch != "0")
print("COUNT:", count)