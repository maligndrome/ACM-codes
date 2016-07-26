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
 X[order-1]=B[order-1]/A[order-1][order-1]
 for i in range(1,order-1):
  sum=0
  for j in range(i+1,order):
   sum+=A[i][order-1-j]*X[order-1-j]
  X[order-1-i]=(B[i]-sum)/A[i][i]
 t2=datetime.datetime.now()
 d_t=t2-t1
 print str(d_t.seconds+d_t.microseconds*0.000001)
 return [A,B,X]
