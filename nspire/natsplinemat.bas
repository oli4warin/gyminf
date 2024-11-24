Define LibPub natsplinemat(xl)=
Func
	Local lambda,mu,n,twos
	n:=dim(xl)-1
	lambda:=seq(((xl[i+1]-xl[i])/(xl[i+1]-xl[i-1])),i,2,n)
	mu:=seq(1-lambda[i],i,2,n-1)
	lambda:=seq(lambda[i],i,1,n-2)
	twos:=newList(n-1)+2
	Return tridiag(mu,twos,lambda)
EndFunc
