from defines.definitions import *

class tower(object):
	_x = 0
	_y = 0
	_shot_x = 0
	_shot_y = 0

	def __init__(self, x = None, y = None):
		if x != None:
			self._x = x
		if y != None:
			self._y = y

		self._shot_x = self._x
		self._shot_y = self._y

	def get_posX(self):
	    return self._x
	
	def set_posX(self, value):
	    self._x = value
	
	def get_posY(self):
	    return self._y
	
	def set_posY(self, value):
	    self._y = value

	def get_bullet_posX(self):
	    return self._shot_x
	
	def set_bullet_posX(self, value):
	    self._shot_x = value
	
	def get_bullet_posY(self):
	    return self._shot_y
	
	def set_bullet_posY(self, value):
	    self._shot_y = value
	

	def reset_shot_bullet(self):
		self._shot_x = self._x
		#self._shot_y = _y

	def shoot_bullet(self):
		self._shot_x = self._shot_x + SPEED
		#self._shot_y = self._shot_y + SPEED

		if(self._shot_x > BULLET_LIMIT):
			self.reset_shot_bullet()