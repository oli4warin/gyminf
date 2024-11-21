Define LibPub interpol(xlist,ylist)=
Func
Local n
	n:=dim(xlist)
	Return sum(seq(lagrange(xlist,i)*ylist[i],i,1,n))
EndFunc
