def is_amstrong(n):
    strings = str(n)
    m = len(strings)
    if n == sum(int(i) ** m for i in strings):
        return True
    else:
        return False
n = int(input("enter a number: "))
amstrong_list = []
for a in range(1, n):
    if is_amstrong(a):
        amstrong_list.append(a)
if amstrong_list:
    print("the list of amstrong numbers less than", n, "are", amstrong_list)
else:
    print("not found any amstrong number less than", n)