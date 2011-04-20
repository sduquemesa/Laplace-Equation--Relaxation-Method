#!/usr/bin/env python

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

def main():

    MSize = (1000,1000)
    phiExt = 0
    phiInt = 99999
    iterN = 100

    M = np.random.random_integers( 10, phiInt-1, size = MSize ) # Initial matrix
    ## M = np.random.rand(MSize[0], MSize[1])
    M[0,:] = M[-1,:] = M[:,0] = M[:,-1] = phiExt # Set the external potential boundary to phiExt

    if MSize[0] % 2 == 0 :   # Odd row/column square matrix

        med = MSize[0]/2
        M[med-2:med+2,med-2:med+2] = phiInt # Set the inner potential

    else:                    # Even row/column square matrix

         med = np.trunc( MSize[0]/2. )
         M[med-1:med+2,med-1:med+2] = phiInt # Set the inner potential

    print 'Initial Matrix:\n', M

    for k in xrange(0,iterN):
    
        for i in xrange(0,MSize[0]-2):

            for j in xrange(0,MSize[0]-2):

                if M[i+1,j+1] != phiInt:
                    M[i+1,j+1] = 0.25*( M[i+1,j] + M[i,j+1] + M[i+1,j+2] + M[i+2,j+1] )
                    

    print '\n\n\n', M

    plt.contourf(M,100)
    plt.colorbar()
    plt.show()

if __name__ == '__main__':

    main()
