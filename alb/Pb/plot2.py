import subprocess as sp
import time as t
from sys import argv
import numpy as np
import linecache 

a1, a2 = [], []
vol, tote = [], []

for k in np.arange(1, 20 , 1):
	template = """
tasks
  0


spinpol
  .true.

spinorb
  .true.

nempty
  8

rgkmax
  8.0

avec
  0.0  0.5  0.5
  0.5  0.0  0.5
  0.5  0.5  0.0


sppath
  '../../../species/'

atoms
  1                                   : nspecies
  'Pb.in'                             : spfname
  1                                   : natoms
  0.0  0.0  0.0    0.0  0.0  0.0      : atposl, bfcmt

ngridk
  {} {}  {}

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
	t.sleep(2)
	try:
		_file = open("INFO.OUT", 'r')
		data = _file.readlines()
		vol.append(data[23].split()[-1])
		tote.append(data[-49].split()[-1])
		_file.close()
		print(vol)
		print(tote)
	finally:
		print("--> {}".format(k))
	a=sp.check_output('cp INFO.OUT {}/INFO{}.OUT'.format(argv[1], k),shell=True)

print("vol")
print(vol)
print("totalE")
print(tote)
