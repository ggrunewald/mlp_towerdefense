import pygame	#importa modulo pygame

from abc import ABCMeta, abstractmethod
from random import randrange

from defines.definitions import *
from classes.entity import *

#Classe abstrata Inimigos

class Ship(Entity):
	__metaclass__ = ABCMeta
	_num = 0
	_armor = 0
	_damage = 0

	def __init__(self, n = None, a = None, d = None):
		if n != None:
			self._num = n
		if a != None:
			self._armor = a
		if d != None:
			self._damage = d

		super(Ship, self).__init__(MAXX, randrange(MAXY))

	@abstractmethod
	def Attack(self):
		pass

	@abstractmethod
	def Move(self): 
		pass

	@property
	def num(self):
		return self._num

	@num.setter
	def num(self, n):
		if n >= 0:
			_num = n

	@property
	def armor(self):
		return self._armor

	@armor.setter
	def armor(self, a):
		if a >= 0:
			_armor = a

	@property
	def damage(self):
		return self._damage

	@damage.setter
	def damage(self, d):
		if d >= 0:
			_damage = d

	@property
	def hp(self):
		return self._armor

	@hp.setter
	def hp(self, h):
		_armor = h

	def get_id(self):
		return self._num

	def hit(self, damage):
		self._armor -= damage

	def Move(self):
		if(self.x < PLANET_EARTH_POSX):
			self.x = MAXX-10
		if self.y < 10 or self.y > MAXY-10:
			self.deslocY = - self.deslocY

		self.x = self.x + self.deslocX
		self.y = self.y + self.deslocY

#Classes especificas Inimigas
class FastShip(Ship):		#Mais rapidas porem com ataque medio e a menor resistencia de todas
	image = pygame.image.load("images/ufast.png")

	def __init__(self, n = None):
		super(FastShip, self).__init__(n, 3, 3)
		self.deslocX = -4
		self.deslocY = 4

	def Attack(self):
		print "FastShip attack!"



class WarShip(Ship):		#Mais resistentes das naves, porem seu ataque nao eh tao forte e eh a mais lenta
	image = pygame.image.load("images/uwar.png")

	def __init__(self, n = None):
		super(WarShip, self).__init__(n, 10, 5)
		self.deslocX = -2
		self.deslocY = 2

	def Attack(self):
		print "WarShip attack!"


class DestroyerShip(Ship):	#Tem o ataque mais potente, porem nao sao tao rapidas nem tao resistentes
	image = pygame.image.load("images/udestroyer.png")

	def __init__(self, n = None):
		super(DestroyerShip, self).__init__(n, 5, 10)
		self.deslocX = -0.9
		self.deslocY = 0.9

	def Attack(self):
		print "DestroyerShip attack!"



