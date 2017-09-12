import numpy as np
from Dotplot_matrix import dotplot_matrix

def dotplot2Ascii(dp, seqA, seqB, heading, filename):
    fl=open('first-dotplot.txt','w')
    #creating text file
    print(heading, file = fl) 
    print('|' + seqB, file = fl)
    #writing seqB on x axis in the file
    for i in range(len(dp)):
        print(seqA[i], file = fl,end='')
        #and seqA on y axis
        for j in range(len(dp[0])):
            if dp[i][j] == 0:
            #if dp index has 0 printing space to the file
                print(" ", end = '',file=fl)
            elif dp[i][j] == 1:
            #if 1, printing * to the file
                print("*", end = '',file=fl)
        print(file=fl)

            
seqA = "peter piper picked a peck of pickled peppers" 
seqB = "a peck of pickled peppers peter piper picked"
heading = "heading"        
dp = dotplot_matrix(seqA, seqB, 5, 4)
print(dotplot2Ascii(dp, seqA, seqB, "My first dotplot", "first-dotplot.txt"))
