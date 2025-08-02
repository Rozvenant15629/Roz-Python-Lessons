def is_amstrong(n):
    string = str(n)
    m = len(string)
    if n == sum(int(i) ** m for i in string):
        return True
    else:
        return False
a = int(input("enter first number: "))
b = int(input("enter second number: "))
amstrong_list = []
for c in range(a, b + 1):
    if is_amstrong(c): 
        amstrong_list.append(c)
if amstrong_list:
    print("the list of amstrong numbers smaller than", b, "and bigger than", a, "are:", amstrong_list)
else:
    print("not found any amstrong numbers!")
