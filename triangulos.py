def triangulo(x1, y1, x2, y2, x3, y3):
	if(((x1-x3)*(y2-y3)-(y1-y3)*(x2-x3)) >= 0):
		return True
	return False

def punto(x1, y1, x2, y2, x3, y3):
	if((triangulo(x1, y1, x2, y2, 0, 0) == True) and  (triangulo(x2, y2, x3, y3, 0, 0) == True) and (triangulo(x3, y3, x1, y1, 0, 0) == True)):
		return True
	if(((triangulo(x1, y1, x2, y2, 0, 0) == False) and (triangulo(x2, y2, x3, y3, 0, 0) == False)) and ((triangulo(x2, y2, x3, y3, 0, 0) == False) and (triangulo(x3, y3, x1, y1, 0, 0) == False))):
		return True
	return False
	

def lectura():
	lista=[]
	lista2=[]
	numero = None
	contador =0
	lector = open("/home/watanuki/python/p102_triangles.txt", "r+")
	for linea in lector.readlines():
		
		lista.append(linea.split(","))
	for e in lista:
		for i in e:
			lista2.append(int(i))
	while len(lista2) >= 6:
		if (punto(lista2[-6],lista2[-5],lista2[-4],lista2[-3],lista2[-2],lista2[-1])):
			contador += 1
		if lista2 != None: 
			lista2.pop()
			lista2.pop()
			lista2.pop()
			lista2.pop()
			lista2.pop()
			lista2.pop()
	return contador			

print "el numero de triangulos con el origen es: ",lectura()	 
