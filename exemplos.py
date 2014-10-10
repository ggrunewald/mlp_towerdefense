#inicializar variaveis

s = "string"		#string

i = 3			#int

f = 1.2			#float

b = True		#boolean

complexo = 1 + 0.8j	#complexo

exp = 2**3		#2 elevado a 3 potencia


#strings

a = "ini"
b = "cio"
c = a+b		#concatenar

print a
print b
print c

d = c*2		#duplicar

print d

len(d)		#tambem serve pro tamanho da string

p = "python"

print p[1]	#p acessar caracteres da palavra
print p[-1]	#n acessar caracteres da palavra de tras pra frente

m = "montypython"

print m[:5]	#printa soh as 5 primeiras
print m[5:]	#tira as 5 primeiras e printa o resto
print m[5:8]	#tira as 5 primeiras e printa ateh a 7
print m[::2]	#a cada 2 caracteres
print m[::-1]	#printa a string ao contrario


#listas

lista = [1, 2, 3, 4]	#inicializar lista

print len(lista)	#tamanho da lista

animais = ["cavalo", "cachorro", "rato", "passaronho"]

print animais[3]

animais[3] = "passarinho"

print animais

animais = animais + [1, 2, 3, "vaca", "porco", 6, 7, 8]	#listas podem ter elementos de tipos diferentes

print animais[:5]	#printa soh os 5 primeiros elementos
print animais[5:]	#tira os 5 primeiros e printa o resto
print animais[5:8]	#tira os 5 primeiros e printa ateh o 7
print animais[::2]	#a cada 2 elementos
print animais[::-1]	#printa a lista ao contrario

primos = [2, 3, 5, 7]

vazia = []

vazia.append("oi")	#incluir elementos
vazia.append("tchau")

print vazia

vazia.remove("tchau")	#remover elementos pelo valor, e nao pelo indice

print vazia

vazia = [2, 3, 2, 2, 2]

if c in vazia:
    vazia.remove(6)	#da uma exception pois 6 nao esta na lista

try:
    vazia.remove(6)	
except:
    pass		#assim suprime a exception sem a necessidade de pesquisar duas vezes pelo 6 (uma no in e outra no remove)

print vazia

vazia = [x for x in vazia if x != 2]	#isso remove todas as ocorrencias de 2 na lista vazia (soh via sobrar o 3)

print vazia

vazia.remove(vazia[0])	#teste para remover pelo indice
print vazia		#funciona mas nao me parece o modo mais otimizado

a = [1, 2, 3]
a.pop(1)		#remocao de uma forma otimizada, 1 eh o indice
print a

pares = [0,2,4]
impares = [1,3,5]

seis = [pares, impares]	#lista de listas

print seis

pares.append(6)		#eh possivel atualizar as listas

print seis

print seis[0][0]	#eh posssivel chamar como se fosse matriz

sete = pares + impares

print sete

sete.insert(8, 7)	#insere o 7 no indice 8

print sete

sete.insert(0, 7)	#insere o 7 no indice 0, empurrando o resto

print sete

sete.insert(2, 7)	#insere o 7 no indice 2, empurrando o resto

print sete

print sete.index(7)	#indice da primeira ocorrencia de 7

print sete.count(7)	#conta ocorrencias de 7

sete.sort()	#ordena

print sete

sete.reverse()	#inverte

print sete

#entrada de dados

num = int(raw_input("Digite um numero: "))	#sempre tem que converter, pois por padrao a entrada eh string

#num1 = int(raw_input("Digite um numero: "))
#num2 = int(input("Digite um numero: "))		#nao entendi direito a diferenca entre esses dois

#if num1 == num2:
#	print "iguais"
#else:
#	print "diff"


#desvio condicional

if len(lista) > num:	#if else
	print  "A lista eh maior que "+ str(num) + ": " + str(lista)	#tem que converter as coisas pra str pra poder printa-lasi
else:
	print "A lista eh menor que " + str(num) + ": " + str(lista)

if num in lista:	#pesquisa por num na lista
	print str(num) + " esta na lista"
else:
	print str(num) + " nao esta na lista"

if 0 < num < 10:	#condicoes encadeadas
	print str(num) + " esta entre 0 e 10"
else:
	print str(num) + " nao esta entre 0 e 10"

for a in lista:
	print a**2	#percorre a lista

lista.insert(1, 'p')

for a in lista:
	if a == 'p':
		print "P nao eh numero"
	else:
		print a
else:
	print 'acabou a lista'	#esse else pertence ao for, e eh executado ao fim do for

#continuar na 29

