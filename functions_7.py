my_list = [*range(5)]
a = list(map(lambda x: x**2 if x % 2 == 0 else x , my_list))
print(a)



