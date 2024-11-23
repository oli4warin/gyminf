Define LibPub lagrange(xl,i)=
Func
	Local n
	n:=dim(xl)
	Return product(seq(((x-xl[j])/(xl[i]-xl[j])),j,1,i-1))*product(seq(((x-xl[j])/(xl[i]-xl[j])),j,i+1,n))
EndFunc
