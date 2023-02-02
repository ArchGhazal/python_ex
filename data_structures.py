list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
length_list1 = len(list1)
print(length_list1)
length_tuple1 = len(tuple1)
print(length_tuple1)
length_set1 = len(set1)
print(length_set1)
length_dict1 = len(dict1)
print(length_dict1)
print('the first elemnt of list is', list1[0])
print('the first element of tuple1 is ' , tuple1[0])
print(dict1["lion"])
list1[1] = "rabbit"
print(list1)
#tuple1[1] = "rabbit"
#print(tuple1)
## so the tuple strucure do not support this method 
list1.append('monkey')
print(list1)
list1.pop(1)
print(list1)
dict1["fish"] = 0
print(dict1)
