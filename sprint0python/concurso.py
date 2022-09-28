punt = 0
print ("Quien ganó el mundial de 2010?")
print("a.Brasil")
print("b.Holanda")
print("c.España")
op=input("Teclea tu respuesta: ")
while(op!="a")and(op!="b")and(op!="c"):
	op=input("Teclea tu respuesta: ")
if(op=="a")or(op=="b"):
	print("Respuesta incorrecta")
	punt = punt -5
elif(op=="c"):
	print("RESPUESTA CORRECTA")
	punt = punt +10
print ("Cual es la capital de Francia?")
print("a.Paris")
print("b.Versalles")
print("c.Eiffel")
op=input("Teclea tu respuesta: ")
while(op!="a")and(op!="b")and(op!="c"):
	op=input("Teclea tu respuesta: ")
if(op=="c")or(op=="b"):
	print("Respuesta incorrecta")
	punt = punt -5
elif(op=="a"):
	print("RESPUESTA CORRECTA")
	punt = punt + 10
print ("Quien es el presidente de España?")
print("a.Pedro Sánchez")
print("b.Mariano Rajoy")
print("c.José María Aznar")
op=input("Teclea tu respuesta: ")
while(op!="a")and(op!="b")and(op!="c"):
	op=input("Teclea tu respuesta: ")
if(op=="c")or(op=="b"):
	print("Respuesta incorrecta")
	punt = punt-5
elif(op=="a"):
	print("RESPUESTA CORRECTA")
	punt = punt+10
print(punt)
