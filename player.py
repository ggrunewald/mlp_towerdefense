from difficulties import *	#importa definicoes de niveis de dificuldades

class Player(object):
	_name = "Anonimo"
	_difficulty = EASY
	_hp = 100

	def __init__(self, n = None, d = None):
		if n != None:
			self.name = n
		if d != None:
			self.difficulty = n

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, n):
		if len(n) > 15:
			return
		elif len(n) == 0:
			return
		else:
			self._name = n

	@property
	def difficulty(self):
		return self._difficulty

	@difficulty.setter
	def difficulty(self, d):
		if d != EASY and d != MEDIUM and d != HARD:
			return
		else:
			self._difficulty = d

	@property
	def difficulty(self):
		return self._difficulty

	@difficulty.setter
	def difficulty(self, d):
		if 0 <= d <= 100:
			self._difficulty = d
		else:
			return
