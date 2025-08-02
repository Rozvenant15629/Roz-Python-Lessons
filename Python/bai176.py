string = input("enter a list: ")
list = list(map(int, string.split()))
print(f"Original list: {list}")
print("Sorted ascending:", sorted(list))
print("sorted descending:", sorted(list, reverse=True))
print("The max of list is:", max(list))
print("The min of list is:", min(list))
print("The sum of list is:", sum(list))
product = 1
for a in list:
    product = product * a
print("The product of list is:", product)
print("The average of list is:", sum(list) / len(list))