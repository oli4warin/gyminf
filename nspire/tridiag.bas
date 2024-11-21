Define LibPub tridiag(u,v,w)=
Func
	Local low,middle,high,n
	n:=max(dim(v))
	low:=subMat(diag(augment({0},augment(u,{0}))),1,2,n,n+1)
	middle:=diag(v)
	high:=subMat(diag(augment({0},augment(w,{0}))),2,1,n+1,n)
	Return low+middle+high
EndFunc
