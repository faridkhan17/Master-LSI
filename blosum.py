import itertools
import math
import numpy as np
import sys

#creating empty list for sequence
L = []
alignment_list = open('alignment.dat', 'r')
#reading file
for i in alignment_list:
    i = i.rstrip("\r\n")
    #removing \r\n at the end of each list
    x= []
    for j in i:
        x.append(j)
    #appending sequence to the empty list
    L.append(x)
#creating file to write on
fl = open('blosum_matrix', 'w')
#FOR PA VALUE
dic = {}
#counter to find total length which is total frequency of the sequence 
counter = 0
for i in L:
    for j in i:
        counter += 1
        if j in dic:
            #if it is already in the dictionary than add 1 to find its frequency
            dic[j]+= 1
        else:
            #if not present than assign value of 1
            dic[j]= 1
#loop for keys and values in the dictionary
for k,v in dic.items():
    #finding pa value, by dividing frequency of sequence over total frequency
    dic[k]=v/counter

#print("pa", dic)
#FOR PAB VALUES
pairs_dic = {}
#creating list for different combination in columns of sequence
pairs = []
for i in range(len(L[0])):
    m = []
    for j in range(len(L)):
        m.append(L[j][i])
    # making all combinations in every column 
    n = itertools.combinations(m, 2)
    for k in n:
    #appending and sorting pairs to count pairs once i.e tk and kt as 1
        pairs.append(''.join(sorted(k)))
#print(pairs)
  
for i in pairs:
#adding pairs to the dictionary
    if i in pairs_dic:
        pairs_dic[i] += 1
    else:
        pairs_dic[i] = 1
for k,v in pairs_dic.items():
    #dividing frequency by total length to get pab values 
    pairs_dic[k] = v/len(pairs)
#print("pab", pairs_dic)       
                
#FOR EXPECTED PROBABILITY
exp = {}
#comparing keys from pab dictionay , if similar just multiply pa*pa
for i, j in pairs_dic.keys():
    if i == j:
        c = dic[i]**2
    else:
        #if different 2.pa*pa
        c = 2*dic[i]*dic[j]
    #updating dictionary for e values
    exp[i+j] = c 
#print("expected prob", exp) 
            
#TO FIND SCORES 
score = {}
#looping in expected prob dictionary keys
for i in exp.keys():
    #using formula to get scores
    score[i] = round(2*math.log2(pairs_dic[i]/exp[i]))
#print("scoring matrix", score)

#creating zeros matrix according to the length of pa dictionary 
matrix = np.zeros((len(dic),len(dic)),dtype = int)
#making list from dictionary
x = list(dic)
#all formating and saving to the file
print("  ",end="", file=fl)
for i in x:
    print('{:>3}'.format(i),end='', file=fl)
print(file=fl)
for i,j in score:
    #print(i,x.index(i),j,x.index(j))
    #filling the matrix with the scores according to the indexes of list(x)
    matrix[x.index(i)][x.index(j)]=score[i+j]
    #to make it a symmetric matrix 
    matrix[x.index(j)][x.index(i)]=score[i+j]
#formating the matrix    
for i in range(len(matrix)):
    print(x[i],end=' ', file=fl)
    for j in range(len(matrix[0])):
        print('{:>3}'.format(matrix[i][j]),end='', file=fl)
    # printing to file
    print(file=fl)
    
#COMMAND LINE ARGUMENTS
#first argument is .dat file       
alignment = sys.argv[1]
#2nd argument is output file
blosum_matrix=str(sys.argv[2])