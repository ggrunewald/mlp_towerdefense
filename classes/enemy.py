from abc import ABCMeta, abstractmethod
from random import randrange
from defines.definitions import *

#Classe abstrata Inimigos

class Ship(object):
	__metaclass__ = ABCMeta
	_num = 0
	_hp = 100
	_armor = 0
	_damage = 0
	_speed = 0
	_x = 0
	_y = randrange(MAXY)

	def __init__(self, n = None, a = None, d = None, s = None):
		if n != None:
			self.num = n
		if a != None:
			self.armor = a
		if d != None:
			self.damage = d
		if s != None:
			self.speed = s

	@abstractmethod
	def attack(self):
		pass

	@abstractmethod
	def move(self): 
		pass

	@property
	def num(self):
		return self._num

	@num.setter
	def num(self, n):
		if n >= 0:
			_num = n;

	@property
	def armor(self):
		return self._armor

	@armor.setter
	def armor(self, a):
		if a >= 0:
			_armor = a;

	@property
	def damage(self):
		return self._damage

	@damage.setter
	def damage(self, d):
		if d >= 0:
			_damage = d;

	@property
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, s):
		if s >= 0:
			_speed = s;

	@property
	def hp(self):
		return self._hp

	@hp.setter
	def hp(self, h):
		if h >= 0:
			_hp = h;

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if 0 <= x <= MAXX:
			_x = x;

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		if 0 <= y <= MAXY:
			_y = y;

#Classes especificas Inimigas

class FastShip(Ship):		#Mais rapidas porem com ataque medio e a menor resistencia de todas
	def __init__(self, n = None):
		super(FastShip, self).__init__(n, 5, 7, 20)

	def attack(self):
		return "FastShip attack!"

	def move(self):
		return "FastShip moving!"

class WarShip(Ship):		#Mais resistentes das naves, porem seu ataque nao eh tao forte e eh a mais lenta
	def __init__(self, n = None):
		super(WarShip, self).__init__(n, 20, 7, 5)

	def attack(self):
		return "WarShip attack!"

	def move(self):
   		return "WarShip moving!"

class DestroyerShip(Ship):	#Tem o ataque mais potente, porem nao sao tao rapidas nem tao resistentes
	def __init__(self, n = None):
		super(DestroyerShip, self).__init__(n, 7, 15, 7)
	
	def attack(self):
   		return "DestroyerShip attack!"

	def move(self):
   		return "DestroyerShip moving!"
