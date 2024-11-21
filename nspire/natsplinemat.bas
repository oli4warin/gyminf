Define LibPub natsplinemat(xlist)=
Func
Local lambda,mu,n,twos
	n:=dim(xlist)-1
	lambda:=seq(((xlist[i]-xlist[i-1])/(xlist[i+1]-xlist[i-1])),i,2,n)
	mu:=seq(1-lambda[i],i,2,n-1)
	lambda:=seq(lambda[i],i,1,n-2)
	twos:=newList(n-1)+2
	Return tridiag(mu,twos,lambda)
EndFunc
