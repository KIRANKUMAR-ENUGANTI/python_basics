print('\n1♥importing module, using array() and printing')
from array import *
my_array1=array('i',[1,2,3])
print('trying to print direct arrayIdentifierName')
print(my_array1)# prints the total discription
import array as arr
my_array2=arr.array('i',[4,5,6])
print('using index')
for i in range(len(my_array2)):
    print(my_array2[i],end=' ')
print("\nslice of array: ",my_array2[2:4])

import array
li_for_arr3=[7,8,9]
my_array3=array.array('i',li_for_arr3)
print('\nusing direct reference')
for i in my_array3:
    print(i,end=' ')



print('\n\n\n2♥using append, extend and insert methods')
print('append: ')
my_array1.append(4)
print(my_array1)

print()
print('extend: ')
my_array2.extend(my_array3)
print(my_array2)
print('slicing works on arry anyhow all type of slicing')
for i in my_array2[:]:
    print(i,end=" ")

print()
print('insert: takes pos and value to append at')
my_array3.insert(3,10)
print('inserted 10 at 3: ',my_array3)


print('\n\n\n3♥using pop and remove methods')
print("array: ",my_array1)
print('pop: can pop last by default or the position and it returns')
print("pop(): ",my_array1.pop())
print('pop(0): ',my_array1.pop(0))
print('pop(0): ',my_array1.pop(0))
print("array af pop: ",my_array1)

print()
print("array: ",my_array3)
print('remove:takes exactly one value and desont returns ')
my_array3.remove(8)
print("remove(8): ",my_array3)
my_array3.remove(9)
print('remove(9): ',my_array3)
my_array3.remove(7)
print('remove(7): ',my_array3)
print("array af remove: ",my_array3)




print('\n\n\n4♥using tolist and fromlist methods')
print('array: ',my_array2)
print('tolist: convert a array to list')
li=my_array2.tolist()
print('my_array2 to li: ',li)

print()
print('fromlist: append list at last to the array')
print('array,li:',my_array3,li)
my_array3.fromlist(li)
print(my_array3)




print('\n\n\n5♥using index, reverse and sorted methods')
print('array: ',my_array3)
print('index : takes value to finds its pos')
print('index of value 10: ',my_array3.index(10))
print('index of value 4: ',my_array3.index(4))
print('index of value 9: ',my_array3.index(9))
my_array3.insert(3,6)
print('now arr is insert with 6: ',my_array3)
print('index of value 6: ',my_array3.index(6))

print()
print('reverse: takes no arg and deosnot return')
my_array3.reverse()
print('reverse of my_array_3 is : ',my_array3)
print('reverse using split: ',my_array3[::-1])

print()
print('sorted fun: ')
print('reverse sort of the array is : ',sorted(my_array3,reverse=True))




print('\n\n\n6♥using buffer_info and count methods')
print("array: ",my_array3)
print('buffer_info: takes no arg return arr buffer addr and no of ele')
print('buffer_infor of myarrat3 is : ',my_array3.buffer_info())

print()
print('count: counts the no of occurances')
print('count of 6: ',my_array3.count(6))





