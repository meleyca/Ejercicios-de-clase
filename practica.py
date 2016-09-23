# MELEYCA CABRERA (UNEFA)
#ver: https://repl.it/Dfq0/1
# CLASE NODO


class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info
			nodo=nodo.sig		
			
	def pos_actual (self, pos):

		nodo  = self.__primero
		cont = 0
		while (nodo != None) :
			
			if (cont == pos):
				self.__actual=nodo
				self.__pos=cont
				return self.__actual.info
			
			nodo = nodo.sig
			cont=cont+1
		return 
		

        # Metodo para buscar un elemento de la lista 
	def buscar_elem (self, valor):

		nodo  = self.__primero
		p = 0
		while (nodo != None) :
			if (nodo.info == valor):
				print p 
			
			nodo = nodo.sig
			p = p + 1
			
		return -1    


	def eliminar_primero(self):
		
		if (self.__primero == None):
			return None
		nodo = self.__primero
		self.__primero = nodo.sig
		if (nodo == self.__actual):
			
			self.__actual = nodo.sig
			
		if (self.__ultimo == nodo):
			
			self.__ultimo = None
			
		self.__n = self.__n - 1
		self.__pos = self.__pos - 1
		del nodo


	# Metodo para eliminar la mitad de una lista

	def eliminar_mitad(self):

		if (self.__primero == None):
			return
		nodo=self.__n
		mitad=nodo/2
		
		for i in range(mitad):
			self.eliminar_primero()

	# Metodo de numeros repetidos en la lista

	def repetidos(self):

		nodo = self.__primero
		nodo=nodo.sig
		cont = 0
		
		while (nodo != None):
			dato = nodo.sig
			while (dato != None):
				if (nodo.info==dato.info):
					cont=cont+1
					print nodo.info
				dato=dato.sig
			nodo = nodo.sig					

		if (cont > 0):
			return True
		if (cont == 0):
			return False
			
	# Metodo mezclar dos listas
	def mezclar(self,x):
		if (self.__n ==None ):
			return False
		
		nodo=self.__primero
		nodo1=x.__primero
		mezcla=[]
		mezcla2=[]
		for i in range(self.__n):
			mezcla=mezcla+[nodo.info]	
			nodo=nodo.sig

		for j in range(x.__n):
			mezcla2=mezcla2+[nodo1.info]
			nodo1=nodo1.sig
		l2=mezcla+mezcla2
		print l2

	# Metodo para invertir la lista

	def invertir(self):
		nodo=self.__primero
		inversa=[]
		for i in range(self.__n):
			inversa = [nodo.info] + inversa
			l=inversa
			nodo=nodo.sig
			
		print l

	# Metodo suma los elementos de una lista

	def sumar(self):
		if (self.__primero==None):
			return
		nodo=self.__primero
		suma=0
		for i in range(self.__n):
			if (type(i)==int):
				suma=suma+nodo.info
			nodo=nodo.sig
		return suma	

        #Metodo compara si dos listas son iguales
	def comparar(self,x):
		if (self.__n ==None ):
			return

		nodo=self.__primero
		nodo2=x.__primero
		cont = 0

		while(nodo!=None) and (nodo2!=None):
			if (nodo.info==nodo2.info):
				return True

			nodo=nodo.sig
			nodo2=nodo2.sig
		return False
	


	
# PRINCIPAL 

# Crea la lista de elementos
l=Lista()
l1=Lista()

# Inserta elementos en la lista 
l.insertar_actual(11);
l.insertar_actual(18);
l.insertar_actual(15);
l.insertar_actual(10);
l.insertar_inicio(16);
l.insertar_actual(18);
l.insertar_ultimo(1);

l1.insertar_actual(11);
l1.insertar_actual(18);
l1.insertar_actual(15);
l1.insertar_actual(10);
l1.insertar_inicio(16);
l1.insertar_actual(18);
l1.insertar_ultimo(1);

# Muestra los elementos de la lista 
l.mostrar()
l.repetidos()
print (l.repetidos())
l.mostrar()
