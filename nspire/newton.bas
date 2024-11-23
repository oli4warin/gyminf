Define LibPub newton(xlist,ylist)=
Func
	Local poly,k,coef
	poly:=0
	For k,1,dim(xlist)
		coef:=div(seq(xlist[i],i,1,k),seq(ylist[i],i,1,k))
		poly:=poly+coef*product(seq(x-xlist[i],i,1,k-1))
		EndFor
	Return poly
EndFunc
