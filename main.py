import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

import player		#importa modulo do jogador
import difficulties	#importa definicoes de niveis de dificuldades

from datetime import date

from colors import *			#importa arquivo com a definicao das cores que criei
from pygame.locals import *		#importa as constantes do pygame, entre elas o QUIT

pygame.init()					#inicializa modulos importados

surface = pygame.display.set_mode((800, 600))	#abre a janela e cria um objeto surface que eh retornado pra variavel surface

pygame.display.set_caption("Earth Defense")					#muda o nome na barra da janela

while True:
	pygame.display.update()
	for event in pygame.event.get():			#se ocorrer um evento
		if event.type == QUIT:					#se for o evento de fechar a janela
			pygame.quit()						#fecha modulos do pygame
			sys.exit()							#termina o programa
