import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

from datetime import date			#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *			#importa as constantes do pygame, entre elas o QUIT

from classes.player import *		#importa modulo da classe jogador
from classes.enemy import *		#importa modulo da classe jogador

from defines.colors import *		#importa definicoes de cores
from defines.difficulties import *	#importa definicoes de niveis de dificuldades
from defines.definitions import *	#importa outras definicoes

from menu.menu import *			#importa o modulo de menu
from menu.inputbox import *		#importa modulo de caixa de texto

pygame.init()					#inicializa modulos importados

surface = pygame.display.set_mode((MAXX, MAXY))	#abre a janela e cria um objeto surface que eh retornado pra variavel surface

pygame.display.set_caption("Earth Defense")					#muda o nome na barra da janela

surface.fill(BLACK)
menu = Menu()
menu.set_colors(WHITE, BLUE, BLACK)
menu.set_fontsize(64)
menu.init(['Earth Defense', 'Start','Name', 'Difficulty','Exit'], surface)
menu.draw(1)

menuContinue = True

player = Player()

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
					player.name = ask(surface, "Insert your name", player.name, True)
				elif menu.get_position() == DIFFICULTY:
					d = ['easy', 'medium', 'hard']
					player.difficulty = ask(surface, "Type easy, medium or hard", d[player.difficulty], False)
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
	space = pygame.image.load("images/space.jpg")
	surface.blit(space, (0, 0))

	earth = pygame.image.load("images/earth.png")
	surface.blit(earth, (-180, 0))


	#surface.fill(BLACK)
	pygame.display.update()

	enemy1 = Enemy(0);
	enemy2 = Enemy(1);

	ask(surface, "Insert your name", enemy1.y, True)
	ask(surface, "Insert your name", enemy2.y, True)

	for event in pygame.event.get():			#se ocorrer um evento

		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):	#se for o evento de fechar a janela ou apertar ESC
			pygame.quit()						#fecha modulos do pygame
			sys.exit()							#termina o programa

		
