Implementación de una máquina de Turing determinista en Python

Creamos una clase maquinaTurnig que tiene como elementos 
	cinta = cinta de la máquina
	transiciones = diccionario con las transiciones de la máquina
	estado_act = el estado actual de la máquina
	posicion= la posición actual de la máquina
	
	tiene como funciones:
	
		def computa(self) = ya configurados los atributos de la máquina ejecuta las transiciones mientras el estado 
		actual esté definido en el conjunto de transicionesm, mientras no se intente acceder a un numero inválido en la cinta
		o que el numero de operaciones sea menor que 10 000.
		
		def movimiento(self, ins) = mueve la cinta a la izquiera o la derecha actualizando la variable "posicion".
		
		def ejecuta(self, ins)= ejecuta las instrucciones para el estado actual leyendo 1 o 0.
	

	en el mismo archivo tenemos la función def lee() que no pertenece a la clase máquinaTuring pero que nos sirve para que el usuario
	ingrese las reglas para las transiciones, para inicializar la máquina, configurar su cinta y probar los casos prueba que el usuario 
	ingrese, y def configCinta(n, cinta, c) que sólo llena la cinta con unos o ceros en un rango.
	
Funcionamiento:

	Se debe ejecutar el programa turing.py y en consola se mostrará un mensaje pidiendo el número de reglas,
	el usuario debe ingresar los datos en el siguiente orden para cada estado:
	
	    ingresar las reglas LEYENDO 0
	1.- Ingresar el nuevo estado
	2.- Ingresar el caracter que debe escribir en la cinta
	3.- Ingresar el movimiento. "R" para derecha y "L" para izquierda (en mayúsculas)
	
		ingresar las reglas LEYENDO 1	
	4.- Ingresar el nuevo estado
	5.- Ingresar el caracter que debe escribir en la cinta
	6.- Ingresar el movimiento. "R" para derecha y "L" para izquierda (en mayúsculas)
		

	si tenemos la regla 0 0 1 1 R, que es el estado cero, leyendo un 1, pasar al estado 2, escribir un 1 en la cinta y moverse a la izquierda
	el usuario sólo tendría que ingresar los útimos 1 caracteres. 
	
	IMPORTANTE: el usuario primero debe meter las reglas para el estado leyendo 0 y luego para el estado leyendo 1
				de lo contrario si el usuario ingresÓ primero las reglas cuando se lee el 1, éstas ocuparan las reglas para 0
	
	Ingresar los casos prueba: En consola pedirá el número de casos prueba que son el numero de unos en la cinta antes de hacer el computo
	y el número de unos después de realizar el computo 
	
