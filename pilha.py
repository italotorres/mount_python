class Pilha: #Definindo a classe pilha
	def __init__(self): #definindo a funcao do construtor
		self.__listaPilha = []


	def dentro(self, val):
		self.__listaPilha.append(val)

	def fora(self):
		val = self.__listaPilha[-1]
		del self.__listaPilha[-1]
		return val

class AdicionaPilha(Pilha):
	def __init__(self):
		Pilha.__init__(self)
		self.__sum = 0

	def getSum(self):
		return self.__sum

	def dentro(self, val):
		self.__sum += val
		Pilha.dentro(self, val)

	def fora(self):
		val = Pilha.fora(self)
		self.__sum -= val
		return val


pilhaObjeto = AdicionaPilha()


for i in range(5):
	pilhaObjeto.dentro(i)
	print(pilhaObjeto.getSum())

for i in range(5):
	print(pilhaObjeto.fora())
