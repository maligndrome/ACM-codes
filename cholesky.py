from __future__ import division
import datetime
from math import sqrt

def transpose(A):
	return [list(i) for i in zip(*A)]

def cholesky(A,b):
	try:
		t1=datetime.datetime.now()
		order=len(A)
		L=initializeMatrix(order)
		for i in xrange(order):
			for j in xrange(i+1):
				sum=0
				for k in xrange(j):
					sum+=L[i][k]*L[j][k]
				L[i][j]=sqrt(A[i][i]-sum) if (i == j) else (1.0 / L[j][j] * (A[i][j] - sum))
		U=transpose(L)
		##Now we have L,U do forward subsitution to get z, such that Lz=b
		z=[]
		X=[]
		for i in xrange(order):
			z.append(0)
			X.append(0)
		for i in xrange(order):
			sum=0
			for j in xrange(i+1):
				sum+=L[i][j]*z[j]
			z[i]=(b[i]-sum)/L[i][i]
		##Now solve Ux=z
		for i in range(0,order):
			sum=0
			for j in range(0,i+1):
				sum+=U[order-1-i][order-1-j]*X[order-1-j]
			X[order-1-i]=(z[order-1-i]-sum)/U[order-1-i][order-1-i]
		t2=datetime.datetime.now()
		d_t=t2-t1
		print 'time elapsed:'+str(d_t.seconds+d_t.microseconds*0.000001)+'s'
		return X
	except:
		return 0

def checkSymmetry(A):
	order=len(A)
	for i in xrange(order):
		for j in xrange(order):
			if(A[i][j]!=A[j][i]):
				return 0
	return 1

def main(): 
	A=input('Enter the coefficient matrix (A):') 
	b=input('Enter the right hand vector (B):') 
	if(checkSymmetry(A)==1):
		X=cholesky(A,b)
		if(X!=0):
			print 'Solution vector is:'+str(X)
		else:
			print 'The matrix is not positive definite.' 

def initializeMatrix(order):
	return [[0]*order]*order
