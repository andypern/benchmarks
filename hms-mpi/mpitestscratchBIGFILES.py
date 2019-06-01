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

  os.system('yes>>file_rank_%s' % (rank)) 



############################ 
if __name__ == '__main__':
    main()
