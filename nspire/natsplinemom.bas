Define LibPub natsplinemom(xl,yl)=
Func
	Local b,m,n,mom
	n:=dim(xl)
	b:=list@>mat(seq(6*div({xl[k],xl[k+1],xl[k+2]},{yl[k],yl[k+1],yl[k+2]}),k,1,n-2),1)
	m:=natsplinemat(xl)
	mom:=subMat(rref(augment(m,b)),1,n-1,n-2,n-1)
	Return augment({0},augment(mat@>list(mom),{0}))
EndFunc
