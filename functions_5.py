from random import randint 
def random_list_summer (n = 15):
    my_list = [randint(-100 , 100) for _ in range(n) ]  
    return sum(my_list) 
print ( ' the summery of the elemnts in my list = ' , random_list_summer() ) 