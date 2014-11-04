
from classes.entity import *

class Entity(object):
	_x = 0
	_y = 0
	_deslocX = 0
	_deslocY = 0

	def __init__(self, x = None, y = None, dx = None, dy = None):
		if x != None:
			self._x = x
		if y != None:
			self._y = y
		if dx != None:
			self._deslocX = dx
		if dy != None:
			self._deslocY = dy

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, n):
			self._x = n

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, n):
			self._y = n

	@property
	def deslocX(self):
		return self._deslocX

	@deslocX.setter
	def deslocX(self, n):
			self._deslocX = n

	@property
	def deslocY(self):
		return self._deslocY

	@deslocY.setter
	def deslocY(self, n):
			self._deslocY = n

