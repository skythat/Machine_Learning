#coding:utf-8
from numpy import *
import operator
from os import listdir

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group, labels

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    #print "dataSetSize:"
    #print dataSetSize
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    #print "diffMat:"
    #print diffMat
    sqDiffMat=diffMat**2
    #print "sqDiffMat:"
    #print sqDiffMat
    sqDistances=sqDiffMat.sum(axis=1)
    #print "sqDistances:" 
    #print sqDistances
    distances=sqDistances**0.5
    #print "distances:" 
    #print distances
    sortedDisIndicies=distances.argsort()
    #print "sortedDisIndicies:" 
    #print sortedDisIndicies
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDisIndicies[i]]
        #print "voteIlabel:" 
        #print voteIlabel
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        #print "classCount:" 
        #print classCount
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    #print "sortedClassCount:" 
    #print sortedClassCount
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr=open(filename)   
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,3))
    #print "returnMat:"
    #print (type(returnMat))
    #print returnMat
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        #print "listFromLine:"
        #print listFromLine
        returnMat[index,:]=listFromLine[0:3]
        #print "returnMat:"
        #print returnMat
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat, classLabelVector
    
def autoNorm(dataSet):
    minvals=dataSet.min(0)
    maxvals=dataSet.max(0)
    ranges=maxvals-minvals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minvals,(m,1))
    #print "normDataSet:"
    #print normDataSet
    normDataSet=normDataSet/tile(ranges,(m,1))
    #print "ranges:"
    #print ranges
    #print "tile(ranges,(m,1))"
    #print tile(ranges,(m,1))
    #print "normDataSet"
    #print normDataSet
    return normDataSet,ranges,minvals

def datingClassTest():
    hoRatio=0.1
    datingDataMat,datingLabels=file2matrix("datingTestSet2.txt")
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    print "numTestVecs"
    print numTestVecs
    errorCount=0.0
    for i in range(numTestVecs):
        #print "normMat[numTestVecs:m,:]"
        #print normMat[numTestVecs:m,:]#表示下标从numtestVecs到m-1的数据
        classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with %d ,the real answer is %d"\
    %(classifierResult,datingLabels[i])
        if (classifierResult !=datingLabels[i]):
            errorCount+=1.0
    print "the total error rate is:%f"%(errorCount/float(numTestVecs))
    print errorCount
       
def classifyPerson():
    resultList=["not all all","in small doses","in large doses"]
    percentTats=float(raw_input("percentage of time spent playing video games?"))   
    ffMiles=float(raw_input("frequent flier miles earned per year?"))
    iceCream=float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels=file2matrix("datingTestSet2.txt")
    normMat, ranges, minVals=autoNorm(datingDataMat)
    inArr=array([ffMiles,percentTats,iceCream]) 
    classifierResult=classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "You will probably like this person:",resultList[classifierResult-1]

def img2vector(filename):
    returnVect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels=[]
    trainingFileList=listdir('trainingDigits')
    #print trainingFileList
    m=len(trainingFileList)
    #print m
    trainingMat=zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:]=img2vector('trainingDigits/%s'%fileNameStr)
    testFileList=listdir('testDigits')
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        vectorUnderTest=img2vector('testDigits/%s'%fileNameStr)
        classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print "the classifier came back with:%d, the real answer is: %d"%(classifierResult,classNumStr)
        if(classifierResult!=classNumStr):
            errorCount+=1.0
    print "\nthe total number of errors is: %d" %errorCount
    print "\nthe total error rate is: %f" %(errorCount/float(mTest))
     
