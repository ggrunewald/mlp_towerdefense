import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

import player					#importa modulo do jogador

import inputbox					#TESTE

from datetime import date		#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *		#importa as constantes do pygame, entre elas o QUIT

from colors import *			#importa arquivo com a definicao das cores que criei
from difficulties import *		#importa definicoes de niveis de dificuldades
from definitions import *		#importa outras definicoes
from pygame_menu_key.menu import *				#importa o modulo de menu

pygame.init()					#inicializa modulos importados

surface = pygame.display.set_mode((1050,620))	#abre a janela e cria um objeto surface que eh retornado pra variavel surface

pygame.display.set_caption("Earth Defense")					#muda o nome na barra da janela

surface.fill(BLACK)
menu = Menu()
menu.set_colors(WHITE, BLUE, BLACK)
menu.set_fontsize(64)
menu.init(['Earth Defense', 'Start','Name', 'Difficulty','Exit'], surface)
menu.draw(1)

menuContinue = True

player = player.Player()

while menuContinue:											#loop do menu

	menu.draw()
	pygame.display.update()

	for event in pygame.event.get():

		if event.type == KEYDOWN:

			if event.key == K_UP:
				if menu.get_position() != START:
					menu.draw(-1)
				else:
					menu.draw(-2)

			if event.key == K_DOWN:
				if menu.get_position() != EXIT:
					menu.draw(1)
				else:
					menu.draw(2)

			if event.key == K_RETURN:
				if menu.get_position() == START:
					menuContinue = False
				elif menu.get_position() == NAME:
					player.name = inputbox.ask(surface, "Insert your name", player.name, True)
				elif menu.get_position() == DIFFICULTY:
					player.difficulty = inputbox.ask(surface, "Type easy, medium or hard", "", False)
				elif menu.get_position() == EXIT:
					menuContinue = False
					pygame.display.quit()
					sys.exit()                      

			if event.key == K_ESCAPE:
				pygame.display.quit()
				sys.exit()

		elif event.type == QUIT:
			pygame.display.quit()
			sys.exit()

while True:										#loop principal

	surface.fill(BLACK)
	pygame.display.update()

	for event in pygame.event.get():			#se ocorrer um evento

		if event.type == QUIT:					#se for o evento de fechar a janela
			pygame.quit()						#fecha modulos do pygame
			sys.exit()							#termina o programa
