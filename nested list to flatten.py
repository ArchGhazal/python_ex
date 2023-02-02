nested_list = [1,2,3, [33,44]]
flatten_list = []
for part_list in nested_list :
    if type(part_list) == list:
      for n in part_list:
            flatten_list.append(n)
    else : 
        flatten_list.append(part_list)
print(flatten_list) 