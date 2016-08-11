def solve(A,B):
	t1=datetime.datetime.now()
	order=len(A)
	X=[]
	for i in range(0,order):
		X.append(0)
	for i in range(0,order):
		for j in range(i+1,order):
			ratio=A[j][i]/A[i][i]
			for k in range(i,order):
				A[j][k]-=(ratio*A[i][k])
			B[j]-=(ratio*B[i])
	for i in range(0,order):
		sum=0
		for j in range(0,i+1):
			sum+=A[order-1-i][order-1-j]*X[order-1-j]
		X[order-1-i]=(B[order-1-i]-sum)/A[order-1-i][order-1-i]
	t2=datetime.datetime.now()
	d_t=t2-t1
	print 'time elapsed:'+str(d_t.seconds+d_t.microseconds*0.000001)+'s'
	return X

def main():
     A=input('Enter the coefficient matrix (A):')
     B=input('Enter the right hand vector (B):')
     X=solve(A,B)
     print 'Solution vector is:'+str(X)