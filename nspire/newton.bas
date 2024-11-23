Define LibPub newton(xl,yl)=
Func
	Local poly,k,coef
	poly:=0
	For k,1,dim(xl)
		coef:=div(seq(xl[i],i,1,k),seq(yl[i],i,1,k))
		poly:=poly+coef*product(seq(x-xl[i],i,1,k-1))
		EndFor
	Return poly
EndFunc
