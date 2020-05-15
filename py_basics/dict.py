print('1♥')
d1=dict({1:'a',2:'b',3:'c'})
print(d1) # dict() expects atmost one arg so same dict
d1=dict([(1,'a'),(2,'b'),(3,'c')])
print("list of tuples to dictionary: ",d1)
d1=dict(((1,'a'),(2,'b'),(3,'c')))
print("tuple of tuples to dictionay: ",d1)
d1['new_list']=[1,2,3]
d1['new_dict']={'nested_dit': 1}
print("updated: ",d1)
print(d1.get(1,'default_value1'))
print(d1.get(3,'default_value1'))
print(d1.get(4,'default_value1'))
print("get()-not updated:",d1)
print(d1.setdefault(1,'default_value1'))
print(d1.setdefault(2,'default_value1'))
print(d1.setdefault(4,'default_value1'))
print("setdefault-updated: ",d1)




print("\n\n\n2♥")
#using exceptional handling

for i in 1,5:
    try:
        value = d1[i]
        print("value found at 1: ", value)
        print(d1)
    except:
        print('exception raised cuz 5 not exist')
        d1[i] = 'default_value2'
        value = d1[i]
        print("found updated value: ", value)
        print("setdefault using exception: ", d1)



print("\n\n\n3♥")
#using del method
print('actual dict: ',d1)
del d1['new_dict']['nested_dit']
print("deleted the nested_dit key: ",d1)
del d1['new_dict']
print("deleted new_dictt: ",d1)
del d1['new_list'][0]
print("deleted new_list ele 0: ",d1)
del d1['new_list']
print('deleted new_list: ',d1)



print("\n\n\n4♥")
#items()method
print(d1.items())
for k,v in d1.items():
    print(k,v)
i=[ (k,v) for k,v in d1.items()]
print("LC using items(): ",i)

print("\n\n\n5♥")
# using values() method
print(d1)
print(d1.values())
for dvalues in d1.values():
    print(dvalues)
print([dvalues for dvalues in d1.values()])




print('\n\n\n6♥')
#using key() method
print(d1)
print(d1.keys())
for dkeys in d1.keys():
    print(dkeys)
print([dkeys for dkeys in d1.keys()])



print('\n\n\n7♥')
#using pop()
print(d1)
print("pop key 1: ",d1.pop(1))
print("pop key 2: ",d1.pop(2))
print("after using pop(): ",d1)
try:
    print("pop key 1: ", d1.pop(6))
except:
    print('exceptin cuz no default values in pop for non existing key')

print("pop key 6: ", d1.pop(6,'default_value3'))
print("poped key 1 already : ", d1.pop(6,-1))




print('\n\n\n8♥')
#using popitem() method
print(d1)
print("before using poptiem(): ",d1)
print("popitem last: ",d1.popitem())
print("after using poptiem(): ",d1)
d1[1]=1
print('updated dict with key 1 and value 1: ',d1)

print("popitem last: ", d1.popitem())
print("after using poptiem(): ",d1)

print("popitem last: ", d1.popitem())
print("after using poptiem(): ",d1)

print("popitem last: ", d1.popitem())
print("after using poptiem(): ",d1)

try:
    print("popitem last: ", d1.popitem())
except:
    print('exceptin cuz cannot pop item form empty dict')




print('\n\n\n9♥')
#using update() method
d2={1:10,2:20,3:30}
d1.update(d2)
print("updated empty d1 wih d2: ",d1)
d3={4:40,5:50}
li_of_tup=d3.items()
d1.update(li_of_tup)
print("updated with d3: ",d1)
d1.update(a=60,b=70)
print("updated d1 with a=60,b=70: ",d1)#cannot have int key with int values
#d1.update(('c',80),('d',90))#wont work
tup=(('c',80),('d',90))
d1.update(tup)
print("updated d1 with tup: ",d1)
lis=[['e',100],['f',110]]
d1.update(lis)
print("updated d1 with lis: ",d1)




print('\n\n\n10♥')
#keys
key_d={0:'z',1:'a',1.5:'b',bool:'c',int:'d',float:'e',
       True:'f',False:'g',hex:'h',oct:'i',str:'j',
        (1,2,3):"it's a tuple",None: 'None'}
print('key_d[0]should be z but:',key_d[0])
print('key_d[1] should be a but :',key_d[1])
print('key_d[False] :',key_d[False])
print('key_d[True] :',key_d[True])
print('key_d[None] :',key_d[None])
print('key_d[(1,2,3)] :',key_d[(1,2,3)])
print()
print(str(key_d))

print([ i for i in key_d.values()])
print("a and b values are missing\n")
print([ i for i in key_d.keys()])
print('True and False keys are missing\n')

#keys can be anything which are immutable and hashable
print("any string: ",hash("strings"))
print("any integer is itself :",hash(23))
htuple=(1,2,3)
print("any tuple: ",hash(htuple))




print('\n\n\n11♥')
#copy differ form assignment
di_for_copy={1:1,2:2,3:3}
print(di_for_copy)
c_di=di_for_copy.copy()
print("before clear di_for_copy,  c_di: ",di_for_copy,c_di)
c_di.clear()
print("after clear di_for_copy,  c_di: ",di_for_copy,c_di)
print("id's of  di_for_copy,c_di: ",id(di_for_copy),id(c_di))
#so when you compy its a seperate copy
if not di_for_copy is c_di: print("c_di is a seperate copy")

print('\n')
di_for_assig={1:10,2:20,3:30}
print(di_for_assig)
a_di=di_for_assig
print("before clear: di_for_assig,  a_di ",di_for_assig,a_di)
a_di.clear()
print("after clear: di_for_assig,  a_di ",di_for_assig,a_di)
print("id's of di_for_assig,a_di: ",id(di_for_assig),id(a_di))
#but when you assing is a same copy
if  di_for_assig is a_di: print("a_di and di_for_assig are smae or single")




print('\n\n\n12♥')
emp_di=dict()
keys_to_generate={1,2,3,4,5}
emp_di=dict.fromkeys(keys_to_generate,1)
print("emp_di.formkeys(seq,defalut_val): ",emp_di)
emp_di=dict.fromkeys(range(5),100)
print("emp_di.formkeys(seq,defalut_val): ",emp_di)




print('\n\n\n13♥')
#using default dict
from collections import defaultdict
d=defaultdict(lambda : 3)
print(d[2])
print(d[1])
print(d[12312412412342])
print(d[22])
d[0]='kiran'
print(d[0])
print(d.__missing__(321))




print('\n\n\n14♥')
#using dict comprahension
dl=[]
[dl.append((x,y)) for (x,y) in zip(range(5),range(5))]
print('the listof tuples using append: ',dl)
print('dl is converted into dict: ',{x:y for (x,y) in dl})
print('list of tuple converted into dictionary',{x:y for (x,y) in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]})
dl=[]
dl=dl+[x for x in zip(range(5),range(5))]
#zip can return a single element or multiple elements at a time 231 236
print('the listof tuples using assingnment: ',dl)
di={s:a for (s,a) in dl}
print(di)
print('used zip for list of tuples: ',{s:a for (s,a) in zip(range(10),range(10))})




print('\n\n\n14♥')
#sorting dictionary
d={s:a for (s,a) in zip(range(5),range(5,0,-1))}

print('used zip for list of tuples: ',d)

sortd_d=sorted(d.items(),key=lambda s:s[0])
print(sortd_d)