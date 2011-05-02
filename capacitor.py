#!/usr/bin/env python

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def main():
    
    phiInt = 100
    MSize = (70,100)
    relation = MSize[0]/MSize[1]
    w = 2   # Correction factor w, belongs [0,2]
    pValue = 1E-7    # Desired precision value
    x = np.linspace(0,relation*10,MSize[0])
    y = np.linspace(0,10,MSize[1])

    M = np.random.random_integers( 10, phiInt-1, MSize ) # Initial matrix
    M[0,:] = 0
    M[-1,:] = 100 # Set the external potential boundary to phiExt

    M = np.asfarray(M)
    flag = True
    count = 0
    error = []
    iteration = []
    while count<1E8:

        for i in xrange(0,MSize[0]-2):    # Odd i positions"

            for j in xrange(0,MSize[1]-2):    # Odd j positions

                if M[i+1,j+1] != phiInt:
                    prom = 0.25*( M[i+1,j] + M[i,j+1] + M[i+1,j+2] + M[i+2,j+1] )
                    R = prom - M[i+1,j+1]
                    M[i+1,j+1] = prom
                    count += 1
                    print count, '\t', abs(R)
                    M[:,0] = M[:,1]
                    M[:,-1] = M[:,-2]
                    ## M[i+1,j+1] = M[i+1,j+1] + w*R
                    if abs(R) < pValue:
                        flag = False
                        print '<------------------------------------>'

    plt.contourf(M,100)
    # plt.contour(M,100)
    plt.xticks((0,1),('',''))
    plt.yticks((0,1),('',''))
    plt.colorbar()
    plt.savefig('capacitor.eps')
    # plt.show()


if __name__ == '__main__':

    main()
