from __future__ import division
import datetime
##0 is for Jacobi
##1 is for Gauss siedel
##2 for SOR
def iter(A,b,method):
	if method==2 : w = optimum_w(A,b)
	else : w=1
	n=len(b);x=[0]*n;temp=[0]*n;iter=0;c=0
	while c!=1 and iter<10000:
		if method>0 : temp=x[:]
		else : print temp
		for i in xrange(n):
			sum=0
			for j in xrange(n):
				if i!=j : sum+=A[i][j]*temp[j]
			temp[i]=temp[i]+w*(((b[i]-sum)/A[i][i]) - temp[i])
		iter+=1
		if (checkerror(x,temp)<0.001): c=1
		x=temp[:]
	if(iter==100000): return 0
	return [x,iter]	

##main call for SOR method
def optimum_w(A,b):
	histogram=[]; t1=datetime.datetime.now()
	for i in xrange(1,199): histogram.append(SOR(A,b,i/100)[1])
	##determine optimum w that solves equation in minimum iterations
	w=histogram.index(min(histogram))/100 + 0.01
	t2=datetime.datetime.now(); d_t=t2-t1 
	print 'time required to determine optimum w:'+str(d_t.seconds+d_t.microseconds*0.000001)+'s'
	return w

def checkerror(x_prev,x_next):
	max_error=0
	mutated=0
	for i in xrange(len(x_prev)):
		if(x_prev[i]!=0):
			max_error=max(abs((x_prev[i]-x_next[i])/x_prev[i]),max_error)
			mutated+=1
	if mutated==0:
		return 100
	else:
		return max_error

def main():
    A=input('Enter the coefficient matrix (A):')
    b=input('Enter the right hand vector (B):')
    method=input('Enter 1 for Jacobi method, 2 for Gauss-Siedel method, 3 for SOR method, 0 to exit:')
    while(method):
	    X=iter(A,b,method-1)
	    print 'Solution vector is:'+str(X[0])
	    print 'No. of iterations required:'+str(X[1])
	    method=input('Enter 1 for Jacobi method, 2 for Gauss-Siedel method, 3 for SOR method, 0 to exit:')
