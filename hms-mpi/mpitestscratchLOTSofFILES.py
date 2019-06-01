#!/usr/bin/env python

# IMPORT EVERYTHING HERE

import os
import random
import math
import time
from mpi4py import MPI    
# CREATE FUNCTIONS AND/OR CLASSES HERE


# MAIN CODE
def main():

  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()
  
  memarray=[] 
  
  FilexCore=1000


  filename=[]
  for ii in range(1,FilexCore):
      filename.append('testfile_%s_rank_%s' % (ii, rank)) 
  

 
  fds = [open(path, 'w') for path in filename]
 
  for fd in fds:
      for i in range(1,10000):
        fd.write('this is just a test')

  for fd in fds:
      fd.close() 
 
############################ 
if __name__ == '__main__':
    main()
