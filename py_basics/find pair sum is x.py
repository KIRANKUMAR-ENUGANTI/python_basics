'''a=[int(x) for x in input("enter the arry number").split()]
print(a)
b=[int(y) for y in input("enter the arry number").split()]
print(b)
c=int(input("etner the comparision value"))

###d=[(i,j) for i in a for j in b if i+j==c]
d=[(i,i-c) for i in a if c-i in b]
print(d)
'''



##Nested list comprehension
data=[[1],[5,2],[3,15,24],[10,4,25,30]]
print(data)
output=[element
        for each_list in data
        if len(each_list)!=0
        for element in each_list
        if element%5 !=0]
print(output)