class maquinaTuring:
	global cinta
	global transiciones
	global estado_act 
	global posicion

	def computa(self):
		while self.estado_act in self.transiciones.keys():
			instrucciones = self.transiciones[self.estado_act]
			instrucciones = instrucciones[self.cinta[self.posicion]]
			self.ejecuta(instrucciones)
			if self.posicion >= len(self.cinta) or self.posicion < 0:
				print ("MLE")
				break
			

	def ejecuta(self, ins):
		self.estado_act = ins[0]
		self.cinta[self.posicion] = ins[1]
		self.movimiento(ins[2])


	def movimiento(self, ins):
		if ins == "R" :
			self.posicion += 1
		if ins == "L":
			self.posicion -= 1


def configCinta(n, cinta, c):
	for i in range (0, n):
		cinta[i] = c


def lee():
	contador = 0
	diccionario = {}
	cinta = []
	reglas = int(input("Hola dame el numero de reglas: "))
	reglas = int(reglas/2)
	for i in range (0, reglas):
		lista = []
		print ("Para el estado ", i)
		for j in range (0,2):
			print ("leyendo... ", j)
			lista2 = []
			lista2.append(int(input("Dame el nuevo estado: ")))
			lista2.append(int(input("Dame lo que escribira en la cinta: ")))
			lista2.append(str(input("Dame el movimiento: ")))
			lista.append(lista2)
		diccionario[i] = lista
	print (diccionario)
	pruebas = int(input("Dame el numero de casos prueba: "))
	listPruebas = []
	for x in range (0, pruebas):
		print("Para la prueba ", x)
		x = int(input("Dame el numero de unos de entrada: "))
		y = int(input("Dame el numero de unos de salida: "))
		listPruebas.append((x,y))
		print(listPruebas)
	for x in range (1000):
		cinta.append(0)
	for p in listPruebas:
		contador += 1
		configCinta(int(p[0]), cinta, 1)
		maquina = maquinaTuring()
		maquina.cinta = cinta
		maquina.transiciones = diccionario
		maquina.estado_act = 0
		maquina.posicion = 0
		maquina.computa()
		if contador > 10000:
			print("TLE")
		print("en la prueba:")
		if maquina.cinta.count(1) == p[1]:
			print("AC")
		else:
			print("WA")
lee()
