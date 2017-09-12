import numpy as np

def dotplot_matrix(seqA,seqB,w,s):
    t=int(w/2)
    #to put 1 in the middle of matching w
    dp = np.zeros((len(seqA),len(seqB)), dtype = int)
    #making matrix of zeros
    for i in range(len(seqA)-w+1):
        for j in range(len(seqB)-w+1):
#double for loop to excess elements in the matrix
            seq1=seqA[i:i+w]
            seq2=seqB[j:j+w]
            #print(seq1,seq2)
            #new variables with w size
            counter=0
            for k in range(w):
                if seq1[k]==seq2[k]:
                    counter += 1
                    #counting for threshold
            if counter >= s:
                dp[i+t][j+t] = 1
    #putting 1's when matched and zeros by default in matrix
    return dp

seqA = "WINDQWS" 
seqB = "WQNDERS"
w = 3
s = 2          
#print(dotplot_matrix(seqA,seqB, w, s))
'''output
[[0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0]
 [0 0 1 0 0 0 0]
 [0 0 0 1 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0]]
'''