Define LibPub lagrange(xlist,i)=
Func
	Local n
	n:=dim(xlist)
	Return product(seq(((x-xlist[j])/(xlist[i]-xlist[j])),j,1,i-1))*product(seq(((x-xlist[j])/(xlist[i]-xlist[j])),j,i+1,n))
EndFunc
