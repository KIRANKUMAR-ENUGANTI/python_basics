print("{} with using .(format values) will replace the {}".format("format","place holder"))
print("we can use {1} in the {2} which rep the {0}".format('format value','index numbers','palce holder'))


my_list = ['zero', 'one', 'two']


# to replace only one ele form the list
print("2nd element is: {[2]}".format(my_list))


# to replace multiple values accoridng to the index numbers
print("""
        1st element is :{0}
        2nd element is : {1}
        3rd element is : {2}
        """.format(*my_list))



a=input("enter the values to split based on comma").split(",",3)
print(a)


# we can use f string
name ="kiran"
age=21
sli=["kiran",'kumar']
print(f"my name is {name} and I'm {age} old and list is {sli}")

#% operator
print("my name is %s and I'm %d years old"%("kiran",21))




print('\n\n\n♥')
print('using dict understading format in print')
captials ={
    1:"Delhi",
    2:"Kolkata",
    3:"Pudhucherry",
    4:"Banguluru"
}
for i in captials:#i iterates only througn keys by default so no need to use .keys() method
    print("the {} ranked captial is {}".format(i,captials[i]))
    print(f"the {i} ranked captial is {captials[i]}")
    print("the %d ranked captial is %s"%(i,captials[i]))
    print()

