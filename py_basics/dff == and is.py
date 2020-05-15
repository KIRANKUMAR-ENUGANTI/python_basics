x=[]
y=[]
z=x
if x==y:
    print(x,"==",y)
    print("equal checks ths values so,x==y")
if x is not y:
    print('id(x): ',id(x),"!= id(y): ",id(y))
    print("is doesnot check the vlues but the id's so, x is not y")
if x is z:
    print(id(x),"==",id(z))
    print("is checks the id's so, x is z")
if (x==z and x is z) and (x is not y and x == y):
    print("thats true")
print("this is beause they are immutables and unhashables like dic,set "
      "not like tuples or strings and frozensets")

print('\n\n\n♥♥')
a="hsi and hello"
b="hsi and hello"
print(a==b)
print(id(a),id(b))
print(a is b)
print("cause they are immuatable and hashable like tuple,forzenset unlike lis,dic,set")