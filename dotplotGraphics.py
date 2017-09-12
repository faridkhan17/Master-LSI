import numpy as np
import matplotlib.pylab as plt
from Dotplot_matrix import dotplot_matrix

hdA = "peter piper picked a peck of pickled peppers" 
hdB = "a peck of pickled peppers peter piper picked"        
dp = dotplot_matrix(hdA, hdB, 5, 4)

def dotplot2Graphics(dp,hdA,hdB,heading,filename):
    fl=open('scatterplot.png','w')
    #creating .png file
    x = []
    y = []
    #looping in the matrix
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            # accessing the index
            if dp[i,j] == 1:
                x.append(j)
                y.append(i)
    plt.plot(x,y,'ro', marker = '+')
    # to invert the plot
    plt.ylim([len(dp), 0])
    #plt.scatter(y, x)
    #plt.imshow(dp)
    # 2nd version with in-built imshow function
    plt.xlabel(hdA)
    #labeling x and y axis
    plt.ylabel(hdB)
    plt.title('scatterplot')
    plt.savefig('scatterplot.png')
    #saving figure to a .png file
    plt.show()
print(dotplot2Graphics(dp, hdA, hdB, "heading", "filename"))