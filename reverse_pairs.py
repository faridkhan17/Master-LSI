from datetime import datetime

#to open file
file = open('words.txt','r')
l = []
start=datetime.now()
for i in file:
    l.append(i.rstrip("\r\n"))
#print(l)
print(datetime.now()-start)
file.close()

file = open('words.txt','r')
start=datetime.now()
for x in file:
    l+= [x.rstrip("\r\n")]
#print(l)
print(datetime.now()-start)

def palindrome():
    #finding palindromes in the file
    counter = 0
    file = open('words.txt','r')
    for i in file:
        if i.rstrip("\r\n") == i.rstrip("\r\n")[::-1]:
            #checking word and its inverse
            counter +=1
            #print(i)
    return counter
       
print(palindrome())

def reverse_pair():
    file = open('words.txt')
    file=file.read().splitlines()
    #print(file)
    l = []
    #to start counter
    c=0
    for word in file:
        if word[::-1] in file:
            l.append(word)
            #giving number of counts
            c+=1
    #print(l)
    return c
print(reverse_pair())

'''output
0:00:00.070354
0:00:00.091085
91
885
'''
        