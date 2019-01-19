import sys
from numpy import mat,mean,power

def read_input(file):
	for line in file:
		yield line.rstrip()
		
input=read_input(sys.stdin)
mapperOut=[line.split('\t') for line in input]
cumVal=0.0
cumSumSq=0.0
cumN=0.0
instance=mapperOut[0]
nj=float(instance[0].strip())
cumN+=nj
cumVal+=nj*float(instance[1].strip())
cumSumSq+=nj*float(instance[2].strip())
mean=cumVal/cumN
varSum=(cumSumSq-2*mean*cumVal+cumN*mean*mean)/cumN
print(("%d\t%f\t%f")%(cumN,mean,varSum))
print(sys.stderr,"report:still alive")
