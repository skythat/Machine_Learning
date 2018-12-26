
def stumpClassify(dataMatrix,dimen,threshIneq):
	retArray=ones((shape(dataMatrix)[0],1))
	if threshIneq=='lt':
		retArray[dataMatrix[:,dimen]<=threshVal]=-1.0
	else:
		retArray[dataMatrix[:,dimen]>threshVal]=-1.0
	return retArray

def buildStump(dataArr,classLabels,D):
	dataMatrix=mat(dataArr);labelMat=mat(classLabels).T
	m,n=shape(dataMatrix)
	numSteps=10.0; bestStump={};bestClasEst=mat(zeros((m,1)))
	minError=inf
	for i in range(n):
		rangeMin=dataMatrix[:,i].min(); rangeMax=dataMatrix[:,i].max();
		stepSixe=(rangeMax-rangeMin)/numSteps
		for j in range(-1,int(numSteps)+1):
			for inequal in ['lt','gt']:
				threshVal=(rangeMin+float(j)*stepSize)
				predictedVals=stumpClassify(dataMatrix,i,threshVal,inequal)
				errArr=mat(ones((m,1)))
				errArr[predictedVals==labelmat]=0
				weightedError=D.T*errArr
				print ("split: dim %d,thresh %.2f, thresh inequal: %s, the weighted error is %.3f" %(i,threshval, inequal, weightedError))
				if weightedError<minError:
					minError=weightedError
					bestClasEst=predictedVals.copy()
					bestStump['dim']=i
					bestStump['thresh']=threshval
					bestStump['ineq']=inequal
	return bestStump,minError,bestClasEst
