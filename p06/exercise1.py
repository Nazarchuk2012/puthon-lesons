import random
#my_list_all = ['red', [2, 0, 1, 2, 5], [200.15, 251,], [632, 367, 6478,], [9.10,], 3.14, 'DF']

#for item in my_list_all:
   # print(item)

##red(red[0])
#red(red[0])



#number_list = [2, 5, 8, 0, 1,]
#print(number_list)

#number_list.append(800)

#1 = len(number_list)
#print(1)



random_number_list = []

# FOR
for i in range(20):
    n = random.randint(0, 100)
    random_number_list.append(n)


print(random_number_list)


sum = 0
for i in random_number_list:
    sum += sum + i
    print('\u2588'*i)

print('Sum = ', sum)

print('\u2588')
















































