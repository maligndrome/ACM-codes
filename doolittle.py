import datetime
from __future__ import division

def initializeMatrix(order):
	return [[0]*order]*order

def Doolittle(A,b):
	##start timer
	t1=datetime.datetime.now()
	order=len(A)
	U=initializeMatrix(order)
	L=initializeMatrix(order)
	for i in xrange(order):
		L[i][i]=1
		for j in xrange(i,order):
			U[i][j]=A[i][j]
			for k in xrange(i):
				U[i][j]-=L[i][k]*U[k][j]
		for j in xrange(i+1,order):
			L[j][i]=A[j][i]
			for k in xrange(i):
				L[j][i]-=L[j][k]*U[k][i]
			L[j][i]/=U[i][i]
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
		z[i]=(b[i]-sum)

	##Now solve Ux=z
	for i in range(0,order):
		sum=0
		for j in range(0,i+1):
			sum+=U[order-1-i][order-1-j]*X[order-1-j]
		X[order-1-i]=(z[order-1-i]-sum)/U[order-1-i][order-1-i]
	##stop timer
	t2=datetime.datetime.now()
	d_t=t2-t1
	print 'time elapsed:'+str(d_t.seconds+d_t.microseconds*0.000001)+'s'
	return X

def main(): 
     A=input('Enter the coefficient matrix (A):') 
     B=input('Enter the right hand vector (B):') 
     X=Doolittle(A,B) 
     print 'Solution vector is:'+str(X) 