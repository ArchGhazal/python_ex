list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for i in list1 :
    print(i)
for x in tuple1:
    print(x)
for s in set1 :
    print(s)
for d in dict1 :
    if  dict1[d] == "land" :
        print (d , 'lives in' , dict1[d])