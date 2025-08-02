nums = input("enter a list: ")
numbers = list(map(int, nums.split(",")))
a = True
if len(numbers) < 2:
    a = False
else:
    diff = numbers[1] - numbers[0]
    for j in range (1, len(numbers) - 1):
        if numbers[j + 1] - numbers[j] != diff:
            a = False
        break
b = True
if len(numbers) < 2:
    b = False
else:
    ratio = numbers[1] / numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i + 1] / numbers[i] != ratio:
            b = False
        break
if a:
    print("This is an arithmetic sequence")
elif b:
    print("This is a geometric sequence")
else:
    print("This is not neither arithmetic and geometric")
