import pygame	#importa modulo pygame

from abc import ABCMeta, abstractmethod
from random import randrange

from defines.definitions import *
from classes.entity import *
from classes.explosion import *

import random
#Classe abstrata Inimigos

class Ship(Entity):
	__metaclass__ = ABCMeta
	_num = 0
	_armor = 0
	_damage = 0
	_delay = 0
	_explosion = False
	_explosion_x = 0
	_explosion_y = 0
	_explosion_time = 10

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

	@abstractmethod
	def ResetStats(self):
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

	@property
	def delay(self):
	    return self._delay
	@delay.setter
	def delay(self, value):
	    self._delay = value
	

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

	def exploding(self):
		if(self._explosion_time > 0):
			self._explosion_time = self._explosion_time - 1
		else:
			self._explosion = False
			self._explosion_time = 20

		return self._explosion

	def self_destruct(self):
		self._explosion_x = self._x
		self._explosion_y = self._y
		self._explosion = True

	def get_explosion_coordinate(self):
		return self._explosion_x, self._explosion_y

	def ResetStats(self,x_ini, y_ini, new_delay, new_armor, new_desloc_x, new_desloc_y):
		self._x = x_ini
		self._y = y_ini
		self._delay = new_delay
		self._armor = new_armor
		self.deslocX = new_desloc_x
		self.deslocY = new_desloc_y

#Classes especificas Inimigas
class FastShip(Ship):		#Mais rapidas porem com ataque medio e a menor resistencia de todas
	image = pygame.image.load("images/ufast.png")

	def __init__(self, n = None):
		super(FastShip, self).__init__(n, 3, 3)
		self.deslocX = -4
		self.deslocY = 4

	def Attack(self):
		print "FastShip attack!"

	def ResetStats(self):
		super(FastShip, self).ResetStats(MAXX, randrange(MAXY), randrange(20), self._armor+1, self.deslocX-0.3, self.deslocY)
		#self._x = MAXX
		#self._y = random.randrange(1,MAXY)
		#self._delay = randrange(20)
		#self._armor = 3*2
		#self.



class WarShip(Ship):		#Mais resistentes das naves, porem seu ataque nao eh tao forte e eh a mais lenta
	image = pygame.image.load("images/uwar.png")

	def __init__(self, n = None):
		super(WarShip, self).__init__(n, 10, 5)
		self.deslocX = -2
		self.deslocY = 2*2

	def Attack(self):
		print "WarShip attack!"

	def ResetStats(self):
		super(WarShip, self).ResetStats(MAXX, randrange(MAXY), randrange(20), self._armor+1, self.deslocX-0.3, self.deslocY)
		#self._x = MAXX
		#self._y = random.randrange(1,MAXY)
		#self._armor = 10*2


class DestroyerShip(Ship):	#Tem o ataque mais potente, porem nao sao tao rapidas nem tao resistentes
	image = pygame.image.load("images/udestroyer.png")

	def __init__(self, n = None):
		super(DestroyerShip, self).__init__(n, 5, 10)
		self.deslocX = -0.9
		self.deslocY = 0.9

	def Attack(self):
		print "DestroyerShip attack!"

	def ResetStats(self):
		super(DestroyerShip, self).ResetStats(MAXX, randrange(MAXY), randrange(20), self._armor+1, self.deslocX-0.3, self.deslocY)
		#self._x = MAXX
		#self._y = random.randrange(1,MAXY)
		#self._armor = 5


