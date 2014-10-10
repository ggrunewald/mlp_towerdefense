dicionario = {'key1': 1, 'key2': 2, "keyn": 'n'}	#aspas simples e duplas sao iguais em python

print dicionario['key1']	#valores acessaveis pela key

print dicionario['keyn']

print dicionario.keys()		#todas as keys do dicionario

dic = dicionario		#ponteiro pra dicionario

print dic

dic = dicionario.copy()		#copia de dicionario

print dic

idades = {'joao': 20, 'jose': 32}

print idades['joao']


#list comprehension

pares = [i for i in range(101) if i%2 == 0 ]	#cria uma lista com os numeros pares entre 0 e 101


#funcoes

def func(n = 2):	#2 eh o valor default caso nenhum seja passado					
	print "O argumento passado foi " + str(n)
	return n

func()

a=17

def func(param=a):
	print param

func()

def func(param=a):	#escopo das variaveis entra nas funcoes, CUIDADOOOOOOOOOOOO!!!1111
	print a

func(2)

def func(a=a):
	print a

func(2)

g = lambda x: x**2	#funcao lambda

lista = range(16)


#filter

pares = filter(lambda x:x%2 == 0, lista)	#filtra a lista criando uma nova lista
impares = filter(lambda x:x%2 != 0, lista)	#com os numeros que tem true na funcao lambda

print pares
print impares


#map

paresQuadrados = map(lambda x:x**2, pares)	#mapeia funcao para elementos da lista

print paresQuadrados


#reduce

fibonacci = range(1,4)

print reduce(lambda x,y: x+y, fibonacci)	#soma os elementos de uma lista. os dois primeiros, depois o terceiro com a soma anterior...

print fibonacci


#arquivo

arq = open("arquivo", 'r')		#w sobrescrever, r ler, a escrever no fim, r+ ler e escrever

#arq.read()				#le todo o arquivo

num = int(arq.readline())		#le uma linha do arquivo

#arq.readlines()			#le todas as linhas de um arquivo e por numa lista

arq.close()				#fecha arquivo

arq = open("arquivo", 'a')

arq.write(str(num) + "oooi ")		#escreve no arquivo

arq.write("tchaaaau\n")

arq.close()				#fecha arquivo


#classes


class Cliente(object):
	satisfeito = True
	def __init__(self, n, i, s = None):		#funcao de inicializacao com o ultimo parametro sendo opcional
		self.nome = n
		self.idade = i
		if s != None:
			self.satisfeito = s
	def multiple_parameters(self, *args, **kwargs):	#funcao com numero indefinido de parametros
		print 'args: ', args, ' kwargs: ', kwargs

joao = Cliente("Joao", 42)

jose = Cliente("Jose", 54, False)

joao.multiple_parameters(1, 2, 3, a = 4, b = 2)		#passa uma lista com 1, 2, 3 e um dicionario com as keys a, b


