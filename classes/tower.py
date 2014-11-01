from random import randrange

from defines.definitions import *
from classes.entity import *
from classes.bullet import *

class tower(Entity):
	#_x = 0
	#_y = 0
	_shooting = False #flag que indica se torre esta atirando

	bullet = None 
	#bullet = Bullet() #futuramente cada lista podera ter uma lista de projeteis caso atirar mais de uma vez seguida

	def __init__(self, x = None, y = None):
		if x != None and y != None:
			super(tower, self).__init__(x, y)
		#	self._x = x 
		#	self._y = y
		



	def is_shooting(self):
		return self._shooting

	def stop_shoot(self):
		self._shooting = False

	#Funcao tem por objetivo mirar no inimigo
	#Futuramente pode receber o id do inimigo tambem para poder achar ele na lista de inimigos
	#Nao pega novos inimigos enquanto esta atirando (mas podemos mudar isso criando mais um objeto Bullet e colocando numa lista,
	#chamando alguma funcao de alta ordem para atirar e tal)
	def lock_target(self, enemyX, enemyY):
		if(self._shooting == False): #So pega novo alvo se nao tiver atirando
			self.bullet = Bullet(self._x, self._y, enemyX, enemyY) #"mira" em um novo alvo (na pratica eh calcular a reta ate ele para atirar)
			self._shooting = True

    #Essa funcao basicamente so chama a funcao que fica atualizando a posicao do projetil da classe bullet
	def shoot_target(self):
		if(self._shooting == True):
			bullet_x, bullet_y, end = self.bullet.shoot_coordinates() #retorna coordenadas atualizadas do projetil
	
		if(end == True): #fim da trajetoria do projetil
			self._shooting = False

		#Com essa informacao aqui da posicao do projetil, podemos utilizar para verificar se atingiu algum inimigo
		return bullet_x, bullet_y

