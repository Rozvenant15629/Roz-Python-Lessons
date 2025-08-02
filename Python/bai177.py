string = input("enter a string: ")
list = list(map(int, string.split(",")))
print("Original list is:", list)
print("The Ascending list is:", sorted(list))
print("The Descending list is:", sorted(list, reverse=True))
if list == sorted(list):
    print("The list is already ASCENDING!")
elif list == sorted(list, reverse=True):
    print("The list is already DESCENDING!")
else:
    print("The list is not already Ascending or Descending")