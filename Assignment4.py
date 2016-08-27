from __future__ import division
import datetime
Q=5
s=0.0002
B=20
n=0.03
e_a=0.0005
pi=3.14159265359

def g(H):
	return (((Q*n*(B+2*H)**(2/3))/s**0.5)**0.6)/B

def f(h):
	return pi*h*h*(9-h)/3 - 30

def f_dash(h):
	return pi*h*(6-h)

def NR(initialGuess):
	ctr=0
	h=initialGuess- f(initialGuess)/f_dash(initialGuess)
	h=float("{0:.5f}".format(h))
	err=error(initialGuess,h)
	while(err>e_a):
		initialGuess=h
		h=initialGuess- f(initialGuess)/f_dash(initialGuess)
		h=float("{0:.5f}".format(h))
		err=error(initialGuess,h)
		print str(h)+'\t\t'+str(err)
		ctr+=1
	return [h,ctr]

def FPI(initialGuess):
	ctr=0
	H=function(initialGuess)
	while(error(initialGuess,H)>e_a):
		initialGuess=H
		H=function(initialGuess)
		ctr+=1
	return [H,ctr]

def main():
	print 'Newton-Raphson Method:\nh\t\terror'
	t1=datetime.datetime.now()
	NRsolution=NR(10)
	t2=datetime.datetime.now()
	d_t=t2-t1
	print 'Depth of the tank: '+ str(NRsolution[0]) +'m\nNo. of iterations:'+ str(NRsolution[1])+'\n'
	print 'Time required:'+str(d_t.seconds+d_t.microseconds*0.000001)+'s\n'
	t1=datetime.datetime.now()
	FPIsolution=FPI(3)
	t2=datetime.datetime.now()
	d_t=t2-t1
	print 'Fixed point iteration problem\nH=' + str(FPIsolution[0]) + 'm\nNo. of iterations:'+ str(FPIsolution[1])+'\nTime required:'+str(d_t.seconds+d_t.microseconds*0.000001)+'s\n'
	ctr=0
	for i in xrange(1,1000):
		if(error(FPIsolution[0],FPI(i/10)[0])>e_a):
			ctr+=1
	if(ctr!=0):
		print 'Not converging to same solution!'
	else:
		print 'Fixed point iteration converges to the same solution.'


def error(oldVal,newVal):
	return abs(newVal-oldVal)/newVal
