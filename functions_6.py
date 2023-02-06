def fibonacci(a):
     if a < 0 :
      print( 'no input')
     elif a == 0 :
      return 0
     elif a == 1 :
      return 1
     elif a == 2 : 
      return 1
     else:
      return fibonacci(a-1) + fibonacci(a-2)
for a in range(5): 
  print(fibonacci(a))