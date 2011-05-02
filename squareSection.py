#!/usr/bin/env python

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def main():

    MSize = (100,100)
    phiExt = 0.0
    phiInt = 100
    w = 2   # Correction factor w, belongs [0,2]
    pValue = 1E-8    # Desired precision value
    x = np.linspace(0,10,MSize[0])
    y = np.linspace(0,10,MSize[1])
    side = 20

    M = np.random.random_integers( 10, phiInt-1, MSize ) # Initial matrix
    M[0,:] = M[-1,:] = M[:,0] = M[:,-1] = phiExt # Set the external potential boundary to phiExt

    if MSize[0] % 2 == 0 :   # Odd row/column square matrix

        med = MSize[0]/2.0
        M[med-side:med+side,med-side:med+side] = phiInt # Set the iternal potential

    else:                    # Even row/column square matrix

         med = np.trunc( MSize[0]/2. )
         M[med-1:med+2,med-1:med+2] = phiInt # Set the inner potential

    M = np.asfarray(M)
    flag = True
    count = 0
    error = []
    iteration = []
    while flag:

        for i in xrange(0,MSize[0]-2):    # Odd i positions"

            for j in xrange(0,MSize[1]-2):    # Odd j positions

                if M[i+1,j+1] != phiInt:
                    prom = 0.25*( M[i+1,j] + M[i,j+1] + M[i+1,j+2] + M[i+2,j+1] )
                    R = prom - M[i+1,j+1]
                    M[i+1,j+1] = prom
                    count += 1
                    print count, '\t', abs(R)
                    ## M[i+1,j+1] = M[i+1,j+1] + w*R
                    if abs(R) < pValue:
                        flag = False
                        print '<------------------------------------>'

    plt.contourf(x,y,M,100)
    # plt.contour(M,100)
    plt.xticks((0,1),('',''))
    plt.yticks((0,1),('',''))
    plt.colorbar()
    plt.show()


if __name__ == '__main__':

    main()
