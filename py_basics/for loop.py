for index, item in enumerate([1,2,3,4,5,6]):
 print(index,item)


for i in range(5):
 print(id(i))
print()
for i in [8760,109,321,123]:
  print(id(i))
print()
for i in ['a','b','c','d']:
  print(id(i))
print()
for i in ['a', 'b', 'c', 'd']:
      print(id(i))


# l_of_t=[(1,2,3),(4,5,6),(7,8,9)]
# i=l_of_t[0]
# j=l_of_t[1]
# k=l_of_t[2]
# for i,j,k in l_of_t: #its unpacking the tuple ele to the parameters every time
#   print('i',i)
#   print('j',j)
#   print('k',k)





l_of_t=['kiran','kumar','enuganti']
i=l_of_t[0]
j=l_of_t[1]
k=l_of_t[2]
print(i,j,k)
for i in l_of_t: #its unpacking the tuple ele to the parameters every time
  print('i',i)


