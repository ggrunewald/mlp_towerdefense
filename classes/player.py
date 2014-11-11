from defines.difficulties import *	#importa definicoes de niveis de dificuldades
from defines.colors import *

class Player(object):
	_name = "anonimo"
	_difficulty = EASY
	_hp = 100
	_score = 0
	_money = 5

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

	@property
	def money(self):
	    return self._money
	@money.setter
	def money(self, value):
	    self._money = value
	

	@property
	def score(self):
	    return self._score
	@score.setter
	def score(self, value):
	    self._score = value

	def buy_tower(self):
			self._money = self._money - 1

	def sell_tower(self):
			self._money = self._money + 1

	def have_money(self):
		if(self._money > 0):
			return True
		else:
			return False

	def profit(self):
		self._money = self._money+1

	def get_money(self):
		return self._money


	def get_hp_status(self):
		if(self._hp > 60):
			return GREEN
		elif (self._hp < 60 and self._hp > 40):
			return YELLOW
		elif(self._hp < 40):
			return RED

	def lose_score(self):
		self._score = self._score-1
	
	
