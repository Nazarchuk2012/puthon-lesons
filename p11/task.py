#1
# X1 = 12
# X2 = 5.7
# X3 = "Kaput"
# X4 = True

#2
my_tuple = (2, 6, 9, 'Кортеж', False)
e1 = [5, 7, 10, 'Список', False, 222]
My_dict = {'x': 1, 'y': 222, 'name': 'Словник'}

#print(my_tuple[3])
#print(e1[0])
#print(My_dict['y'])

e1[0] = 'Новий список'
#print(e1)
My_dict['y'] = 111
#print(My_dicty)

#for i in my_tuple:#
  #  print(i)

#for i in e1:
 #   print(i)

for key in My_dict:
    print(key, My_dict[key])




numbers = (1, 3, 6, 8, 0, 12, 5, 7)

for key in numbers:
    if key % 2 == 0:
        print(key * 2)
    else:
        print(key * 3)



































