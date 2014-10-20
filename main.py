import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

import player					#importa modulo do jogador
import difficulties				#importa definicoes de niveis de dificuldades

from datetime import date		#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *		#importa as constantes do pygame, entre elas o QUIT

from colors import *			#importa arquivo com a definicao das cores que criei
from menu import *

pygame.init()					#inicializa modulos importados

surface = pygame.display.set_mode((854,480))	#abre a janela e cria um objeto surface que eh retornado pra variavel surface

pygame.display.set_caption("Earth Defense")					#muda o nome na barra da janela

surface.fill(BLACK)
menu = Menu()
menu.set_colors(WHITE, BLUE, BLACK)
menu.set_fontsize(64)
menu.init(['Earth Defense', 'Start','Options','Quit'], surface)
menu.draw(1)
pygame.key.set_repeat(199,69)#(delay,interval)

while True:										#loop do menu
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_UP:
				if menu.get_position() != 1:
					menu.draw(-1)
				else:
					menu.draw(-2)
			if event.key == K_DOWN:
				if menu.get_position() != 3:
					menu.draw(1)
				else:
					menu.draw(2)
			if event.key == K_RETURN:
				if menu.get_position() == 3:#here is the Menu class function
					pygame.display.quit()
					sys.exit()                        
			if event.key == K_ESCAPE:
				pygame.display.quit()
				sys.exit()
			pygame.display.update()
		elif event.type == QUIT:
			pygame.display.quit()
			sys.exit()
	pygame.time.wait(8)

while True:										#loop principal
	pygame.display.update()
	for event in pygame.event.get():			#se ocorrer um evento
		if event.type == QUIT:					#se for o evento de fechar a janela
			pygame.quit()						#fecha modulos do pygame
			sys.exit()							#termina o programa
