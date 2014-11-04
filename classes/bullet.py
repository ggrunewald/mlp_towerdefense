from __future__ import division
from random import randrange

from defines.definitions import *
from classes.entity import *

class Bullet(Entity):
	path_angle = 0
	end = 0 #Flag que indica se bala concluiu sua trajetoria

	def __init__ (self, tower_x  = None, tower_y  = None, enemy_x  = None, enemy_y = None):
		
		################################################
		#CALCULA COEFICIENTE ANGULAR DA EQUACAO DA RETA#
		################################################

		if(enemy_x != tower_x):
			self.path_angle = (enemy_y - tower_y)/(enemy_x - tower_x)
		else:
			if(enemy_y < tower_x): #Inimigo logo em cima da torre
				self.path_angle = MAX_ANGLE_TOWER_ENEMY
			elif(enemy_y > tower_y): #Inimigo logo em baixo da torre
				self.path_angle =- -MAX_ANGLE_TOWER_ENEMY 


		#Ajusta valores do anglo entre torre e inimigo para quando exceder limite
		#OBS: Tangente da reta com eixo x (coeficiente angular) possui valores muito grandes quando se aproxima de 90 graus
		if(self.path_angle < -MAX_ANGLE_TOWER_ENEMY):
			self.path_angle = -MAX_ANGLE_TOWER_ENEMY
		elif (self.path_angle > MAX_ANGLE_TOWER_ENEMY):
			self.path_angle = MAX_ANGLE_TOWER_ENEMY

	    ##########################################################
		#CALCULA O "b" DA EXPRESSAO: y = ax + b (EQUACAO DA RETA)#
		##########################################################
		self.constant_b = tower_y - (self.path_angle*tower_x)

		#########################################################################
		#AJUSTA DESLOCAMENTO DO PROJETIL (esq ou dir) APARTIR DA POSX DO INIMIGO#
		#########################################################################
		if(enemy_x > tower_x): #Se inimigo a direita da torre
			self.deslocX = BULLET_SPEED - abs(BULLET_SPEED_ADJUST_FACTOR*self.path_angle)
		elif(enemy_x < tower_x): #Se inimigo a esquerda da torre
			self.deslocX = -1*(BULLET_SPEED - abs(BULLET_SPEED_ADJUST_FACTOR*self.path_angle))


		###########################################################
		#POSICAO X INICIAL DO PROJETIL = POSICAO INICIAL DA TORRE##OBS: Posicao Y sera calculada pela equacao da reta
		###########################################################
		self.x = tower_x	#Comeca a incrementar posicao x do projetil a partir da posicao atual da torre


	def shoot_coordinates(self):
		########################################################################
		#CALCULA Y DO PROJETIL USANDO A EQUACAO DA RETA CALCULADA NO CONSTRUTOR#
		########################################################################
		self.y = self.path_angle*self.x + self.constant_b

		#Copia os valores para retorno da funcao
		new_x = self.x
		new_y = self.y

		################################
		#FAZ O DESLOCAMENTO DO PROJETIL#
		################################
		self.x =self.x + self.deslocX
		self.y = self.y + self.deslocY


		#################################################################
		#VERIFICA LIMITES DO PROJETIL (NAO PODE EXCEDER LIMITES DA TELA)#
		#################################################################
		if(new_x >= MAXX or new_x <= 0 or new_y >= MAXY or new_y <= 0):
			end = 1
		else:
			end = 0

		##################################################################
		#RETORNA COORDENADAS >>E<< SE PROJETIL ATINGIU OS LIMITES DA TELA#
		##################################################################
		return new_x, new_y, end

