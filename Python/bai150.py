def divisible(i):
    if i % 3 == 0 and i % 5 != 0:
        return True
    else:
        return False
n = int(input("Enter a number: "))
divisibles_list = []
for a in range(1, n):
    if divisible(a):
        divisibles_list.append(a)
print("The sum of numbers divisible by 3 but not divisible by 5 is:", sum(divisibles_list))