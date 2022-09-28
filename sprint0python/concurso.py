print ("Quien ganó el mundial de 2010?")
print("a.Brasil")
print("b.Holanda")
print("c.España")
op=input("Teclea tu respuesta: ")
while(op!="a")and(op!="b")and(op!="c"):
	op=input("Teclea tu respuesta: ")
	
if(op=="a")or(op=="b"):
	print("Respuesta incorrecta")
elif(op=="c"):
	print("RESPUESTA CORRECTA")
