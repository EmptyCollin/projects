import pygame
import os

#################################################################################################################

class Player:

	def __init__(self):
		self.health =100
		self.attack = 20
		self.san =100
		self.room =0
		self.basic_hp = 100
		self.basic_san = 100
		
#################################################################################################################
def render_player(player,screen):
	text1 = 'Health:        ' + str(player.health)
	text2 = 'Attack:        ' + str(player.attack)
	text3 = 'San:           ' + str(player.san) 
	font = pygame.font.SysFont("monospace", 18,True)
	t1_render = font.render(text1,1,((254, 207, 0)))
	screen.blit(t1_render,(150,420))
	t2_render = font.render(text2,1,((254, 207, 0)))
	screen.blit(t2_render,(150,450))
	t3_render = font.render(text3,1,((254, 207, 0)))
	screen.blit(t3_render,(150,480))




def check_equip(player,bag):
	player.basic_hp = player.basic_san = 100
	for i in bag:
		if i.function == '1':
			player.basic_hp += 5
		if i.function == '2':
			player.basic_hp += 15
		if i.function == '3':
			player.basic_san += 5
		if i.function == '4':
			player.basic_san += 15
		if i.function == '0':
			player.basic_hp += 5
			player.basic_san += 5
	player.health = player.basic_hp
	player.san = player.basic_san


	
