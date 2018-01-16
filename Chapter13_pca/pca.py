from numpy import *

def loadDateSet(filename,delim='\t'):
	fr=open(filename)
	stringArr=[line.strip().split(delim) for line in fr.readlines()]
	datArr=[list(map(float,line)) for line in stringArr]
	return mat(datArr)
	
def pca(dataMat,topNfeat=9999999):
	meanVals=mean(dataMat,axis=0)
	meanRemoved=dataMat-meanVals
	covMat=cov(meanRemoved,rowvar=0)
	eigVals,eigVects=linalg.eig(mat(covMat))
	eigValInd=argsort(eigVals)
	eigValInd=eigValInd[:-(topNfeat+1):-1]
	redEigVects=eigVects[:,eigValInd]
	lowDDataMat=meanRemoved*redEigVects
	reconMat=(lowDDataMat*redEigVects.T)+meanVals
	return lowDDataMat,reconMat

def replaceNanWithMean():
	datMat=loadDateSet("secom.data"," ")
	numFeat=shape(datMat)[1]
	for i in range(numFeat):
		meanVal=mean(datMat[nonzero(~isnan(datMat[:,i].A))[0],i])
		datMat[nonzero(isnan(datMat[:,i].A))[0],i]=meanVal
	return datMat
