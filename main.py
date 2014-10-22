import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

from datetime import date			#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *			#importa as constantes do pygame, entre elas o QUIT

from classes.player import *		#importa modulo da classe jogador
from classes.enemy import *		#importa modulo da classe jogador
from classes.tower import *

from defines.colors import *		#importa definicoes de cores
from defines.difficulties import *	#importa definicoes de niveis de dificuldades
from defines.definitions import *	#importa outras definicoes

from menu.menu import *			#importa o modulo de menu
from menu.inputbox import *		#importa modulo de caixa de texto


#TA AQUI A FUNCAO PRA ATUALIZAR AS TORRES E ATIRAR...NAO SABIA EXATAMENTE ONDE COLOCAR PRA FICAR MAIS ORGANIZADO
def shoot_bullet(a_tower):
	surface.blit(towers, (a_tower.get_posX(), a_tower.get_posY()))
	a_tower.shoot_bullet()
	surface.blit(bullet, (a_tower.get_bullet_posX(), a_tower.get_bullet_posY()))

pygame.init()					#inicializa modulos importados

surface = pygame.display.set_mode((MAXX, MAXY))	#abre a janela e cria um objeto surface que eh retornado pra variavel surface

pygame.display.set_caption("Earth Defense")					#muda o nome na barra da janela

surface.fill(BLACK)
menu = Menu()
menu.set_colors(WHITE, BLUE, BLACK)
menu.set_fontsize(64)
menu.init(['Earth Defense', 'Start','Name', 'Difficulty','Exit'], surface)
menu.draw()

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

pauseMenu = Menu()
pauseMenu.set_colors(WHITE, BLUE, BLACK)
pauseMenu.set_fontsize(64)
pauseMenu.init(['Paused', 'Resume', 'Exit'], surface)


#CARREGA AS IMAGENS
space = pygame.image.load("images/space.jpg")
earth = pygame.image.load("images/earth.png")
towers = pygame.image.load("images/tw.png")
bullet = pygame.image.load("images/bl.png")

#LISTAS PARA GUARDAR INIMIGOS/TORRES DO JOGO
enemyList = []
towerList = []   #Talvez aqui possamos aplicar aquelas funcoes de alta ordem para calcular a trajetoria de todos os projeteis

matriz = [ [ 0 for j in range(20) ] for i in range(10) ]
#MATRIZ GRID
for i in range(10):
	for j in range(20):
		matriz[i][j] = 0

while True:										#loop principal

	surface.blit(space, (0, 0))
	surface.blit(earth, (-300, 20))
	#APLICA FUNCAO MAP PARA TODAS AS LISTAS DO JOGO (nao sabia onde por a funcao e coloquei no topo)
	map(shoot_bullet, towerList) #atualiza projetil para todas as torres

	pygame.display.update()

	for event in pygame.event.get():			#se ocorrer um evento

		if event.type == QUIT:	#se for o evento de fechar a janela ou apertar ESC
			pygame.quit()						#fecha modulos do pygame
			sys.exit()							#termina o programa

		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pauseMenu.draw()
				paused = True
				while paused:
					for event in pygame.event.get():
						if event.type == KEYDOWN:
							if event.key == K_ESCAPE:
								paused = False
						#COMEcO
							if event.key == K_UP or event.key == K_DOWN:
								if pauseMenu.get_position() == RESUME:
									pauseMenu.draw(1)
								else:
									pauseMenu.draw(-1)
							elif event.key == K_RETURN:
								if pauseMenu.get_position() == RESUME:
									paused = False
								else:
									pygame.quit()
									sys.exit()
						#FIM
					pauseMenu.draw()
					pygame.display.update()

		if event.type == MOUSEBUTTONDOWN:
			#Pega as coordenadas do mouse
			mouseX, mouseY = pygame.mouse.get_pos()
			print "X = " + str(mouseX) + "   " + "Y = " + str(mouseY)
			#Cria nova torre na poiscao do mouse
			#Se nao tem nenhuma torre nos vizinhos...
			if towerList == []:
				new_tower = tower(mouseX, mouseY)
				#Adiciona torre na lista de torre
				towerList.insert(0, new_tower)	

			adiciona = 1
			for elem in towerList:
				if mouseX > elem.get_posX()+70 or mouseX < elem.get_posX() - 70 or mouseY > elem.get_posY()+70 or mouseY < elem.get_posY() - 70:
					new_tower = tower(mouseX, mouseY)
					adiciona = adiciona*1
				else:
					adiciona = 0

			if(adiciona == 1):
				#Adiciona torre na lista de torre
				towerList.insert(0, new_tower)
