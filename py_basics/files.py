'''# Use the file name sample.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
value=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    i=line.split()
    v=float(i[-1])
    print(v)
    value=value+v
avg=value/count
print("Average spam confidence:",avg)







# Use the file name sample.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
value=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    i=line.partition("0")
    print(i)
    v=float(i[2])
    value=value+v
avg=value/count
print("Average spam confidence:",avg)









fname = input("Enter file name: ")
fh = open(fname)
count=0
value=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    i=line.find('0.')
    v=float(line[i:])
    value=value+v
avg=value/count
print("Average spam confidence:",avg)






 alternative method

fname = input("Enter file name: ")
if len(fname)<1:fname='sample.txt'
fh = open(fname)
count=0
value=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    for i in range(len(line)):
        if not line[i].isdigit(): continue
        v=float(line[i:]) 
        value=value+v
        break
avg=value/count
print("Average spam confidence:",avg)

#ans:  Average spam confidence: 0.750718518519






fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    line = line.rstrip()
    for word in line.split():
        if word in lst: continue
        lst.append(word)

'''





#to find high number user and his email
name = input("Enter file:")
if len(name)< 1 : name = "sample.txt"
handle = open(name)
counts={}
for line in handle:
    if not line.startswith("From") or line.startswith("From:"): continue
    word=line.split()[1]
    counts[word]=counts.get(word,0)+1
'''bigcount=None
user=None
newlist=list()
for users,counter in counts.items():
    if bigcount is None or counter>bigcount:
        bigcount=counter
        user=users
    print(user,bigcount)
    
    
    newtuple = counter, users
    newlist.append(newtuple)
newlist.sort(reverse=True)
print(newlist[0][1], newlist[0][0])
'''
#print(sorted([(v,k) for (k,v) in counts.items()],reverse=True)[0])

#print([i for i in sorted([v,k for k,v in hnd.items()])])
name = input("Enter file:")
if len(name) < 1 : name = "sample.txt"
handle = open(name)
hnd={}
for lines in handle:
    line=lines.rstrip()
    if not line.startswith("From") or line.startswith("From:"): continue
    words=line.split()
    word=words[-2].split(':')[0]
    hnd[word]=hnd.get(word,0)+1
l=sorted([(k,v) for (k,v) in hnd.items()])
for i in l:
    print(i[0],i[1])