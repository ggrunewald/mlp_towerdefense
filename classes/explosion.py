import pygame	#importa modulo pygame

from defines.definitions import *
from classes.enemy import *	



class explosion(object):

	def __init__(self, enemy):
		self._explosion = enemy

	def draw_explosion(self, enemy, surface):
		if(  type(enemy) is FastShip):
			surface.blit(fast_ship_explosion_image, enemy.get_explosion_coordinate())
		elif(type(enemy) is WarShip):
			surface.blit(war_ship_explosion_image, enemy.get_explosion_coordinate())
		elif(type(enemy) is DestroyerShip):
			surface.blit(destroyer_ship_explosion_image, enemy.get_explosion_coordinate())



	



