from abc import ABCMeta, abstractmethod
from random import randrange

from defines.definitions import *

#Classe abstrata Inimigos

class Ship(object):
	__metaclass__ = ABCMeta
	_num = 0
	_hp = 3
	_armor = 0
	_damage = 0
	_speed = 0
	_x = MAXX
	_y = randrange(MAXY)
	deslocX = 0
	deslocY = 0

	def __init__(self, n = None, a = None, d = None, s = None):
		if n != None:
			self._num = n
		if a != None:
			self._armor = a
		if d != None:
			self._damage = d
		if s != None:
			self._speed = s

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
	def speed(self):
		return self._speed

	@speed.setter
	def speed(self, s):
		if s >= 0:
			_speed = s

	@property
	def hp(self):
		return self._hp

	@hp.setter
	def hp(self, h):
		if h >= 0:
			_hp = h

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
			_y = y

	def set_x(self, x):
		self._x = x

	def set_y(self, y):
		self._y = y

	def get_x(self):
		return self._x

	def get_y(self):
		return self._y

	def get_id(self):
		return self._num

	def hit(self, damage):
		self._hp -= damage

	def get_hp(self):
		return self._hp

#Classes especificas Inimigas
class FastShip(Ship):		#Mais rapidas porem com ataque medio e a menor resistencia de todas
	def __init__(self, n = None):
		super(FastShip, self).__init__(n, 5, 7, 20)
		self.deslocX = -4
		self.deslocY = 4

	def Attack(self):
		return "FastShip attack!"

	def Move(self):
		if(self._x < PLANET_EARTH_POSX):
			self._x = MAXX-10
		if(self._y < 10):
			self.deslocY = 4
		if(self._y > MAXY-10):
			self.deslocY = -4

		self._x = self._x +  self.deslocX
		self._y = self._y +  self.deslocY

class WarShip(Ship):		#Mais resistentes das naves, porem seu ataque nao eh tao forte e eh a mais lenta


	def __init__(self, n = None):
		super(WarShip, self).__init__(n, 20, 7, 5)
		self.deslocX = -2
		self.deslocY = 2

	def Attack(self):
		return "WarShip attack!"

	def Move(self):
		if(self._x < PLANET_EARTH_POSX):
			self._x = MAXX-10
		if(self._y < 10):
			self.deslocY = 2
		if(self._y > MAXY-10):
			self.deslocY = -2

		self._x = self._x +  self.deslocX
		self._y = self._y +  self.deslocY
		
		return "WarShip moving!"


class DestroyerShip(Ship):	#Tem o ataque mais potente, porem nao sao tao rapidas nem tao resistentes
	def __init__(self, n = None):
		super(DestroyerShip, self).__init__(n, 7, 15, 7)
		self.deslocX = -0.9
		self.deslocY = 0.9

	def Attack(self):
		return "DestroyerShip attack!"

	def Move(self):
		if(self._x < PLANET_EARTH_POSX):
			self._x = MAXX-10
		if(self._y < 10):
			self.deslocY = 0.9
		if(self._y > MAXY-10):
			self.deslocY = -0.9

		self._x = self._x +  self.deslocX
		self._y = self._y +  self.deslocY

