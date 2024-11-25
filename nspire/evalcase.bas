Define LibPub evalcase(fl,xl,xval)=
Func
Local i,n
n:=dim(fl)
	If xval<xl[1] Then
		Return fl[1]|x=xval
	EndIf
	For i,2,n
		If xval>=xl[i-1] and xval<xl[i] Then
			Return fl[i-1]|x=xval
		EndIf
	EndFor
		Return fl[n]|x=xval
EndFunc
