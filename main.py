import pygame	#importa modulo pygame
import sys		#importa modulo sys pra nao dar erro ao fechar a janela

from datetime import date			#importa funcoes relacionadas com tempo para registro de highscores
from pygame.locals import *			#importa as constantes do pygame, entre elas o QUIT

from classes.player import *		#importa modulo da classe jogador
from classes.enemy import *			#importa modulo da classe jogador
from classes.tower import *
from classes.bullet import *
from classes.entity import *
from classes.explosion import *

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
bullet = pygame.image.load("images/ball2.png")
lifebar = pygame.image.load("images/lifebar.png")
fast_ship_explosion_image = pygame.image.load("images/expl1.png")
war_ship_explosion_image = pygame.image.load("images/expl2.png")
destroyer_ship_explosion_image = pygame.image.load("images/expl3.png") 
coin = pygame.image.load("images/coin.png") 

surface.fill(BLACK)
menu = Menu()
menu.set_colors(WHITE, BLUE, BLACK)
menu.set_fontsize(64)
menu.init(['Earth Defense', 'Start','Name', 'Difficulty','Exit'], surface)
menu.draw()

menuContinue = True

player = Player()
scoreFont = pygame.font.SysFont("purisa", 30, bold=True)
moneyFont = pygame.font.SysFont("purisa", 30, bold=True)


#################################################
# FUNCOES PARA IMPRIMIR ANIMACAO NO MENU INICIAL#
#################################################
#												#
#												#

#Usa recursao com funcao de maior ordem
def animate_menu(fun, e_list):
	if len(e_list) == 0:
		return []
	else:
		return fun(e_list[0]) + animate_menu(fun, e_list[1:])



def change_position(enemy):
	enemy.Move()
	surface.blit(enemy.image, (enemy.x, enemy.y))
	return [enemy]


w_enemy = [WarShip() for i in range(4)]
f_enemy = [FastShip() for i in range(5)]
d_enemy = [DestroyerShip() for i in range(3)]
enemies = w_enemy+f_enemy+d_enemy
for i in enemies:
	i.ResetStats()

#												#
#												#
#################################################

while menuContinue:											#loop do menu

	surface.blit(space, (0, 0))
	surface.blit(earth, (-300, 20))
	enemies = animate_menu(change_position, enemies)
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
def draw_explosion(enemy):
	if(  type(enemy) is FastShip):
		surface.blit(fast_ship_explosion_image, enemy.get_explosion_coordinate())
	elif(type(enemy) is WarShip):
		surface.blit(war_ship_explosion_image, enemy.get_explosion_coordinate())
	elif(type(enemy) is DestroyerShip):
		surface.blit(destroyer_ship_explosion_image, enemy.get_explosion_coordinate())

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
				if ((enemy.x - PLANET_EARTH_POSX) < shortest_distance): #Se eh o mais proximo do planeta
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
			if(bullet_x >= enemy.x-DAMAGE_AREAX and bullet_x <= enemy.x+DAMAGE_AREAX):
					if(bullet_y >= enemy.y-DAMAGE_AREAY and bullet_y <= enemy.y+DAMAGE_AREAY):
						enemy.hit(1)  #Tira 1 de HP (coloquei um valor pequeno na classe enemy para teste)	
						print "HIT!"
						a_tower.stop_shoot() #Torre acertou o inimigo, por isso, mesmo projetil nao continua trajetoria na tela
						if(enemy.hp <= 0):
							#Morreu
							enemy.self_destruct()
							enemy.ResetStats()
							###enemyList.remove(enemy)    #Agora inimigos sempre revivem   
							player.score=player.score+1	#Contabiliza pontos para jogador	
			elif(enemy.hp <= 0): #Repete a verificacao da morte do inimigo pq outras torres podem ter destruido
				#Morreu
				enemy.self_destruc()
				enemy.ResetStats()
				##enemyList.remove(enemy)   #Agora inimigos sempre revivem
			if(enemy.exploding()):	
				draw_explosion(enemy)


def move_enemy(a_enemy):
	surface.blit(a_enemy.image, (a_enemy.x, a_enemy.y))
	if a_enemy.x !=0 and a_enemy.x < PLANET_EARTH_POSX:
		player.hp = player.hp - a_enemy.damage
		print "EXPLODE! Vida restante:" + str(player.hp)
	a_enemy.Move()


def insert_enemies():

	enemies = [WarShip() for i in range(player.difficulty*4 + 2)]
	for i in enemies:
		i.y = random.randrange(1,MAXY)
		enemyList.insert(0,i)
	enemies = [FastShip() for i in range(player.difficulty*4 + 2)]
	for i in enemies:
		i.y = random.randrange(1,MAXY)
		enemyList.insert(0,i)
	enemies = [DestroyerShip() for i in range(player.difficulty*3 + 2)]
	for i in enemies:
		i.y = random.randrange(1,MAXY)
		enemyList.insert(0,i)

	random.shuffle(enemyList)

	for en in enemyList:
		print "Y: " + str(en.y)

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

	##############################################
	#			ATUALIZACAO DA TELA 			 #
	##############################################
	#											 #
	#											 #


	#######################
	#APLICA AS FUNCOES MAP#
	#######################
	#Atualiza projetil para todas as torres
	#map(attack_earth, enemyList)
	map(attack_enemy, towerList)
	#Imprime inimigos
	#map(lambda a_enemy: a_enemy.Move(), enemyList)

 	map(lambda a_enemy: move_enemy(a_enemy), enemyList)


	##################################
	#DESENHA BARRA DA VIDA DO JOGADOR#
	##################################
	pygame.draw.rect(surface, player.get_hp_status(), [10, 600, 10+ player.hp*2, 14])

	###################################################
	#IMPRIME LABEL COM OS PONTOS E DINHEIRO DO JOGADOR#
	###################################################
	surface.blit(scoreFont.render(str(player.score) + " Points", 0, WHITE), (12, 8))
	surface.blit(moneyFont.render(str(player.get_money()) + " Money", 0, YELLOW), (875, 8))


	if(player.score >= 10):
		surface.blit(coin, (185, 15))

	pygame.display.update()

	#											 #
	#											 #
	##############################################

	for event in pygame.event.get():			#se ocorrer um evento

		if event.type == QUIT:					#se for o evento de fechar a janela ou apertar ESC
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
				print str(mouseX) + "   " + str(mouseY)
				#Cria nova torre na poiscao do mouse
				#Se nao tem nenhuma torre nos vizinhos...
				if(mouseX > PLANET_EARTH_POSX):
					if towerList == []:
						new_tower = tower(mouseX, mouseY)
						print str(mouseX) + "   " + str(mouseY)
						#Adiciona torre na lista de torre
						player.buy_tower()
						towerList.insert(0, new_tower)	
					else:
						adiciona = 1
						for elem in towerList:
							if mouseX > elem.x + 27 or mouseX < elem.x - 27 or mouseY > elem.y + 47 or mouseY < elem.y - 47:
								new_tower = tower(mouseX, mouseY)
								#if(player.buy_tower() is True):
								adiciona = adiciona*1

							else:
								adiciona = 0
								#Remove torre!
								player.lose_score()
								player.sell_tower()
								towerList.remove(elem)

						if(adiciona == 1):
							if(player.have_money() is True):
								player.buy_tower()
								print str(mouseX) + "   " + str(mouseY)
								#Adiciona torre na lista de torre
								towerList.insert(0, new_tower)
				elif(mouseY > 10 and mouseY < 50):
					if(mouseX > 180):
						if(player.score >=10):
							#Converter para moeda
							player.score = player.score -10
							player.money = player.money + 1

