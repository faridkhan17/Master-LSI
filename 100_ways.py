import itertools
oper=['+','-','/','*','']
a=[]
l=[]
#i from 1 to 9
for i in range(1,10):
    temp=  []
    for j in oper:#appending string i and j in temp list
        temp.append(str(i)+j)
    a.append(temp)
y=itertools.product(*a)
#generating 5 power 8 possible combinations
c=0
for i in y:
    d=''.join(i)
    #print(d)
    if d[-1] in oper:
        #if last character is in oper variable it will remove it
        d=d[:-1]
        #appending it to new list
        l.append(d)
        #print(d)
l = set(l)
#removing duplicates from combinations
for i in l:   
    if eval(i) == 100:
        c+=1
        #print(i)
print(c)

'''Output
101
'''