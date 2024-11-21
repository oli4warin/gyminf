Define LibPub div(xlist,ylist)=
Func
Local n
	n:=dim(xlist)
	If n=1 Then
		Return ylist[1]
	EndIf
	Return ((div(seq(xlist[i],i,2,n),seq(ylist[i],i,2,n))-div(seq(xlist[i],i,1,n-1),seq(ylist[i],i,1,n-1)))/(xlist[n]-xlist[1]))
EndFunc
