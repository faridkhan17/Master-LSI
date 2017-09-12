import sys
import numpy as np
import matplotlib.pylab as plt

def dotplot(seqA,seqB,w,s):
    t=int(w/2)
    dp = np.zeros((len(seqA),len(seqB)), dtype = int)
    for i in range(len(seqA)-w+1):
        for j in range(len(seqB)-w+1):
            seq1=seqA[i:i+w]
            seq2=seqB[j:j+w]
            counter=0
            for k in range(w):
                if seq1[k]==seq2[k]:
                    counter += 1
            if counter >= s:
                dp[i+t][j+t] = 1
    
    return dp           

def dotplot2Ascii(dp, seqA, seqB, heading, file_name):
    fl = open(file_name,"w")
    print('|' + seqB, file = fl)
    for i in range(len(dp)):
        print(seqA[i], file = fl,end='')
        for j in range(len(dp[0])):
            if dp[i][j] == 0:
                print(" ", end = '',file=fl)
            elif dp[i][j] == 1:
                print("*", end = '',file=fl)
        print(file=fl)
        

def dotplot2Graphics(dp,hdA,hdB,heading,filename):
    x = []
    y = []
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i,j] == 1:
                x.append(j)
                y.append(i)
    plt.plot(x,y,'ro')
    plt.ylim([len(dp), 0])
    #plt.scatter(y, x)
    #plt.imshow(dp)
    plt.xlabel(hdA)
    plt.ylabel(hdB)
    plt.title(heading)
    plt.savefig(filename)
    plt.show()
           

#print(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
#command line Arguments 
w=int(sys.argv[1])
# w as integer
s =int(sys.argv[2])
# s as integer
seqA=str(sys.argv[3])
''.join([i.rstrip("\r\n") for i in open(seqA,'r')][1:])
# reading seqA FASTA file
seqB=str(sys.argv[4])
''.join([i.rstrip("\r\n") for i in open(seqB,'r')][1:])
# reading seqB FASTA file
output=str(sys.argv[5])
heading='something'
dp=dotplot(seqA, seqB, w, s)

if output[-3:]== 'txt':
    # if last 3 digits are txt go to following function
    dotplot2Ascii(dp, seqA, seqB, heading, output)
elif output[-3:]== 'png':
    # and if png than go to following
    dotplot2Graphics(dp,"x lable","y lable",heading,output)
    

