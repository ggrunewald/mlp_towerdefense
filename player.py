from defines.difficulties import *	#importa definicoes de niveis de dificuldades

class Player(object):
	_name = "anonimo"
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
		if len(n) > 18:
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
		if d == 'easy':
			self._difficulty = EASY
		elif d == 'medium':
			self._difficulty = MEDIUM
		elif d == 'hard':
			self._difficulty = HARD
		else:
			return

	@property
	def hp(self):
		return self._hp

	@hp.setter
	def hp(self, p):
		if 0 <= p <= 100:
			self._hp = p
		else:
			return
