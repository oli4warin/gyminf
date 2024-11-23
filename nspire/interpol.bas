Define LibPub interpol(xl,yl)=
Func
Local n
	n:=dim(xl)
	Return sum(seq(lagrange(xl,i)*yl[i],i,1,n))
EndFunc
