#!/usr/bin/env python

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def main():

    MSize = (10,10)
    phiExt = 0
    phiInt = 100
    w = 2   # Correction factor w, belongs [0,2]
    pValue = 1    # Desired precision value

    M = np.random.random_integers( 10, phiInt-1, MSize ) # Initial matrix
    M[0,:] = M[-1,:] = M[:,0] = M[:,-1] = phiExt # Set the external potential boundary to phiExt

    if MSize[0] % 2 == 0 :   # Odd row/column square matrix

        med = MSize[0]/2.0
        M[med-2:med+2,med-2:med+2] = phiInt # Set the inner potential

    else:                    # Even row/column square matrix

         med = np.trunc( MSize[0]/2. )
         M[med-1:med+2,med-1:med+2] = phiInt # Set the inner potential

    M = np.asfarray(M)
    flag = True
    while flag:

        for i in np.arange(0,MSize[0]-2):    # Odd i positions

            for j in np.arange(0,MSize[0]-2):    # Odd j positions

                if M[i+1,j+1] != phiInt:
                    #phiO = M[i+1,j+1]
                    prom = 0.25*( M[i+1,j] + M[i,j+1] + M[i+1,j+2] + M[i+2,j+1] )
                    M[i+1,j+1] = prom
                    #R = phiO - M[i+1,j+1]
                    ## #phiN = phiN + w*R
                    ## if abs(R) < pValue:
                    ##     flag = False
                    ##     raw_input()
                    ## print M

    plt.contourf(M,100)
    plt.colorbar()
    plt.show()

    ## np.savetxt("matrix.txt", M)

if __name__ == '__main__':

    main()
