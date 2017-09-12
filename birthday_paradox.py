import math   
from random import randint
import collections

L = [1, 2, 3, 4, 5]
def has_duplicates(L):
    #to find duplicates in a list
    a = set(L)
    #to remove duplicates from the list
    b = len(a)
    c = len(L)
    if b == c:
        #comparing length of before and after set function
        return False
    else:
        return True
    
#print(has_duplicates(L))

def Birthday_paradox():
    trial = 0
    counter=0
    while trial < 10000:
        #generating random birthday numbers for 27 students
        x=[randint(1,365) for i in range(0,27)]
        trial += 1
        if has_duplicates(x):
            #checking duplicates in above function
            counter+=1
    return counter/10000.0

print(Birthday_paradox())
#values of m and n from the question
m = 365.0
n = 27
def approx_value():
    var = -(n**2)/(2*m)
    #main formula to find approx, value
    form = 1- (math.e **(var))
    return form
print(approx_value())



def exact_value():
    probibility = 1
    for i in range(1,n+1):
        #main formula to find exact probability
        prob = (m - i)/m
        probibility = prob*probibility
    return 1-probibility
print(exact_value())        
    

def triplicate(L):
    #to find three people sharing the birthday
    counter=collections.Counter(L)
    #grouping the similar words and giving value(repeatition of that word)
    a = counter.values()
    for i in a:
        if i > 2:
            return True
    return False

def Birthday_paradox_3():
    trial = 0
    counter=0
    while trial < 10000:
        #generating random birthday numbers 
        x=[randint(1,365) for i in range(0,27)]
        trial += 1
        if triplicate(x):
            #above function for three people sharing birthday
            counter+=1
    return counter/10000.0

print(Birthday_paradox_3())

'''output
False
0.6369
0.631616269064
0.654461472342
0.02
'''
    




        