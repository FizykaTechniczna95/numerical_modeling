import subprocess as sp
import time as t
from sys import argv
import numpy as np

for k in np.arange(1, 8, 0.5):
	template = """
tasks
  20

avec
  0.0  0.5  0.5
  0.5  0.0  0.5
  0.5  0.5  0.0    

atoms
   1                                    : nspecies
'Pb.in'                                 : spfname
   1                                    : natoms; atposl, bfcmt below
    0.00000000    0.00000000    0.00000000    0.00000000  0.00000000  0.00000000

sppath
  '../../../species/'

ngridk
  11 11 11

rgkmax
  {}

plot1d
  7 200                               : nvp1d, npp1d
  0.0   0.0   1.0                     : vlvp1d
  0.5   0.5   1.0
  0.0   0.0   0.0
  0.5   0.0   0.0
  0.5   0.5   0.0
  0.5   0.25 -0.25
  0.5   0.0   0.0
""".format(int(k), int(k), int(k))
	with open('elk.in','w') as file:
		file.writelines(template)
	a =sp.check_output('../../../src/elk',shell=True)
	print(a)	
	a=sp.check_output('gracebat {}'.format(argv[2]),shell=True)
	print(a)	
	a=sp.check_output('convert {}.ps {}.png'.format(argv[2][:-4],argv[2][:-4]),shell=True)
	print(a)	
	a=sp.check_output('mv {}.png {}/BD{}{}{}.png'.format(argv[2][:-4],argv[1],k,k,k),shell=True)
	print(a)	
	#t.sleep(2)
	print("--> {}".format(k))
