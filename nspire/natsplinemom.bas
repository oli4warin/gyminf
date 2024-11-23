Define LibPub natsplinemom(xlist,ylist)=
Func
	Local b,m,n,mom
	n:=dim(xlist)
	b:=list▶mat(seq(6*div({xlist[k],xlist[k+1],xlist[k+2]},{ylist[k],ylist[k+1],ylist[k+2]}),k,1,n-2),1)
	m:=natsplinemat(xlist)
	mom:=subMat(rref(augment(m,b)),1,n-1,n-2,n-1)
	Return augment({0},augment(mat▶list(mom),{0}))
EndFunc
