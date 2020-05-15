boys_money=[1.,9,10,4,3]
def extra_money(boy_money):
    return 10
final_money=[extra_money(i) if i<5 else i for i in boys_money]
print(final_money)

sqr=[i*i if i%2==0 else i for i in range(5)]
print("condition before loop",sqr)

sq=[i*i  for i in range(5) if i%2==0]
print("condition after loop",sq)

matrix=[[i for i in range(4)] for j in range(4)]
print(matrix)
mat=[ j for i in matrix for j in i]
print(mat)
print(ord('a'))
