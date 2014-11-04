import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

from datetime import date			#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *			#importa as constantes do pygame, entre elas o QUIT

from classes.player import *		#importa modulo da classe jogador
from classes.enemy import *			#importa modulo da classe jogador
from classes.tower import *
from classes.bullet import *
from classes.entity import *

from defines.colors import *		#importa definicoes de cores
from defines.difficulties import *	#importa definicoes de niveis de dificuldades
from defines.definitions import *	#importa outras definicoes

from menu.menu import *				#importa o modulo de menu
from menu.inputbox import *			#importa modulo de caixa de texto
import random



pygame.init()					#inicializa modulos importados

surface = pygame.display.set_mode((MAXX, MAXY))	#abre a janela e cria um objeto surface que eh retornado pra variavel surface

pygame.display.set_caption("Earth Defense")					#muda o nome na barra da janela


######################################
#CARREGAMENTO DAS IMAGENS DO PROGRAMA#
######################################
space = pygame.image.load("images/space.jpg")
earth = pygame.image.load("images/earth.png")
towers = pygame.image.load("images/human.png")
bullet = pygame.image.load("images/ball.png")
et = pygame.image.load("images/ufo.png")


surface.fill(BLACK)
menu = Menu()
menu.set_colors(WHITE, BLUE, BLACK)
menu.set_fontsize(64)
menu.init(['Earth Defense', 'Start','Name', 'Difficulty','Exit'], surface)
menu.draw()

menuContinue = True

player = Player()

while menuContinue:											#loop do menu

	surface.blit(space, (0, 0))
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




#################################################################################
#                    ALGUMAS FUNCOES AUXILIARES PARA O PROGRAMA                 #  
#################################################################################
#FUNCAO PARA IMPRIMIR AS TORRES CRIADAS E ATIRAR NO INIMIGO
#NAO SABIA ONDE MELHOR BOTAR...BOTEI AQUI.
def attack_enemy(a_tower):
	surface.blit(towers, (a_tower.x, a_tower.y))
	

	#===============================================#
	# Codigo para selecionar um inimigo para atirar #
	#===============================================#
	#Se tiver inimigos na lista de inimigos
		#Escolher inimigo mais perto do planeta (estabalecer coordenada)
			#verificar cada elemento da lista
				#se tiver distancia x menor que os outros inimigos, faz o lock dele

	#So tenta atacar inimigos se houver inimigos vivos!
	if(len(enemyList) > 0):
		if(not a_tower.is_shooting()):  #Nao faz a pesquisa tudo de novo caso torre estiver atualmente atirando (podemos mudar isso)
			closest_enemy = None
			shortest_distance = 999999 #infinito
			for enemy in enemyList:
				if (enemy.x - PLANET_EARTH_POSX) < shortest_distance: #Se eh o mais proximo do planeta
					shortest_distance = enemy.x - PLANET_EARTH_POSX #Salva distancia
					closest_enemy = enemy 	#Indica inimigo pre selecionado

			a_tower.lock_target(closest_enemy.x,closest_enemy.y) #Detecta inimigo que gostaria de atirar

	    #=================================#
		# Codigo para imprimir o projetil #
		#=================================#
		bullet_x, bullet_y = a_tower.shoot_target()
		surface.blit(bullet, (bullet_x, bullet_y)) #Atira no inimigo

		#============================================#
		# Codigo para detectar se atingiu um inimigo #
		#============================================#
		for enemy in enemyList:
			if(bullet_x >= enemy.x-DAMAGE_AREA and bullet_x <= enemy.x+DAMAGE_AREA):
					if(bullet_y >= enemy.y-DAMAGE_AREA and bullet_y <= enemy.y+DAMAGE_AREA):
						enemy.hit(1)  #Tira 1 de HP (coloquei um valor pequeno na classe enemy para teste)
						print "HIT!"
						a_tower.stop_shoot() #Torre acertou o inimigo, por isso, mesmo projetil nao continua trajetoria na tela
						if(enemy.hp <= 0):
							#Morreu
							enemyList.remove(enemy)
			elif(enemy.hp <= 0):
				#Morreu
				enemyList.remove(enemy)


def move_enemy(a_enemy):
	surface.blit(et, (a_enemy.x, a_enemy.y))
	a_enemy.Move()


def insert_enemies():

	enemies = [WarShip() for i in range(5)]
	for i in enemies:
		i.y = random.randrange(1,MAXY)
		enemyList.insert(0,i)
	enemies = [FastShip() for i in range(5)]
	for i in enemies:
		i.y = random.randrange(1,MAXY)
		enemyList.insert(0,i)
	enemies = [DestroyerShip() for i in range(3)]
	for i in enemies:
		i.y = random.randrange(1,MAXY)
		enemyList.insert(0,i)

	random.shuffle(enemyList)

	for en in enemyList:
		print "Y: " + str(en.y)


#	enemy1 = WarShip(1)
#	enemy2 = WarShip(2)

#	enemy1.set_x(1000)
#	enemy1.set_y(0)
	
#	enemy2.set_x(800)
#	enemy2.set_y(400)

#	enemyList.insert(0, enemy1)
#	enemyList.insert(0, enemy2)


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
						#COMECO
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
				print str(mouseX) + "   " + str(mouseY)
				#Adiciona torre na lista de torre
				towerList.insert(0, new_tower)	

			adiciona = 1
			for elem in towerList:
				if mouseX > elem.x+50 or mouseX < elem.x - 50 or mouseY > elem.y+ 50 or mouseY < elem.y - 50:
					new_tower = tower(mouseX, mouseY)
					adiciona = adiciona*1
				else:
					adiciona = 0

			if(adiciona == 1):
				#Adiciona torre na lista de torre
				towerList.insert(0, new_tower)
