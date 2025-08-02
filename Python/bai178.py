string = input("enter a string: ")
list = list(map(int, string.split(",")))
inc = True
dec = True
for a in range(len(list) - 1):
    if list[a] <= list[a+1]:
        dec = False
    elif list[a] >= list[a+1]:
        inc = False
if inc:
    print("The sequence is increasing")
elif dec:
    print("The sequence is decreasing")
else:
    print("The sequence is neither increasing or decreasing")