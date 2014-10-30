import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

from datetime import date			#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *			#importa as constantes do pygame, entre elas o QUIT

from classes.player import *		#importa modulo da classe jogador
from classes.enemy import *		#importa modulo da classe jogador
from classes.tower import *
from classes.bullet import *

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


######################################
#CARREGAMENTO DAS IMAGENS DO PROGRAMA#
######################################
space = pygame.image.load("images/space.jpg")
earth = pygame.image.load("images/earth.png")
towers = pygame.image.load("images/tw.png")
bullet = pygame.image.load("images/bl.png")
et = pygame.image.load("images/et.png")



#################################################################################
#                    ALGUMAS FUNCOES AUXILIARES PARA O PROGRAMA                 #  
#################################################################################
#FUNCAO PARA IMPRIMIR AS TORRES CRIADAS E ATIRAR NO INIMIGO
#NAO SABIA ONDE MELHOR BOTAR...BOTEI AQUI.
def attack_enemy(a_tower):
	surface.blit(towers, (a_tower.get_posX(), a_tower.get_posY()))
	
	if(not a_tower.is_shooting()):
		#ESCOLHE UM INIMIGO (Temos que decidir como fazer a logica selecao do inimigo (se o mais perto, mais longe,...))
		#Aqui coloquei todos atacam o primeiro inimigo so para testar as classes
		a_tower.lock_target(enemyList[0].get_x(),enemyList[0].get_y()) #Detecta inimigo que gostaria de atirar
	
	surface.blit(bullet, a_tower.shoot_target()) #Atira no inimigo

def move_enemy(a_enemy):
	surface.blit(et, (a_enemy.get_x(), a_enemy.get_y()))
	a_enemy.Move()


def insert_enemies():
	enemy1 = WarShip(1)
	enemy2 = WarShip(2)

	enemy1.set_x(1000)
	enemy1.set_y(0)
	
	enemy2.set_x(800)
	enemy2.set_y(400)

	enemyList.insert(0, enemy1)
	enemyList.insert(0, enemy2)


####################################################################################

###############################################
#INICIALIZA ESTRUTURAS NECESSARIAS PARA O JOGO#
###############################################
enemyList = []
towerList = []  

#Funcao para teste (ou nao)
insert_enemies()


#############################
#MENU PRINCIPAL DA INTERFACE#
#############################
while True:										#loop principal

	surface.blit(space, (0, 0))
	surface.blit(earth, (-300, 20))

	#######################
	#APLICA AS FUNCOES MAP#
	#######################
	#Atualiza projetil para todas as torres
	map(attack_enemy, towerList)
	#Imprime inimigos
	map(move_enemy, enemyList)


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
			#Cria nova torre na poiscao do mouse
			#Se nao tem nenhuma torre nos vizinhos...
			if towerList == []:
				new_tower = tower(mouseX, mouseY)
				#Adiciona torre na lista de torre
				towerList.insert(0, new_tower)	

			adiciona = 1
			for elem in towerList:
				if mouseX > elem.get_posX()+50 or mouseX < elem.get_posX() - 50 or mouseY > elem.get_posY()+ 50 or mouseY < elem.get_posY() - 50:
					new_tower = tower(mouseX, mouseY)
					adiciona = adiciona*1
				else:
					adiciona = 0

			if(adiciona == 1):
				#Adiciona torre na lista de torre
				towerList.insert(0, new_tower)
