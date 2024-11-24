Define LibPub spline(xl,yl,mom)=
Func
	Local c,d,n
	n:=dim(xl)
	c:=seq(((yl[i]-yl[i-1])/(xl[i]-xl[i-1]))+((xl[i-1]-xl[i])/(6))*(mom[i]-mom[i-1]),i,2,n)
	d:=seq(((yl[i]+yl[i-1])/(2))-(((xl[i]-xl[i-1])^(2))/(12))*(mom[i]+mom[i-1]),i,2,n)
	Return seq(((mom[i]*(x-xl[i-1])^(3)-mom[i-1]*(x-xl[i])^(3))/(6*(xl[i]-xl[i-1])))+c[i-1]/2*(2*x-xl[i]-xl[i-1])+d[i-1],i,2,n)
EndFunc
