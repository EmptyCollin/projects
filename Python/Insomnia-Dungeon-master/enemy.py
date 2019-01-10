import pygame
from helper_functions import *


def battle (player,enemy,screen):
	enemy.health -= player.attack
	enemy.be_attacked = True
	enmey.b_a_time = pygame.time.get_ticks()
	if enemy.health <= 0:
		return 'PLAYER'
	else:
		player.health -= enemy.attack
		screen_blink(screen)
		if player.health <= 0:
			return 'ENEMY'
		else:
			return 'DRAW'



def screen_blink(screen):
	surf = pygame.Surface((2000,2000))
	surf.fill((255,0,0))
	surf.set_alpha(153)
	screen.blit(surf,(0,0))


##################################################################################################

def render_enemy(enemy,screen):
	if enemy.be_attacked:
		if pygame.time.get_ticks() - enemy.b_a_time > 500:
			spr = enemy.sprite
		else:
			spr = enemy.sprite.set_alpha((235))
	screen.blit(spr,enemy.location)

##################################################################################################

class Enemy:
	enem_data = {}
	for enemy in csv_loader('Enemy.csv'):
		enemy_data[enemy[0]] = {'name': enemy[1],'sprite':enemy[2],'Size_x':enemy[3],'Size_y':enemy[4],'attack': int(enemy[5]),'health':enemy[6],'Loot_chance':int(enemy[7]),'Loot_item':enemy[8],'Desc':enemy[9],'Brief_Desc':enemy[10]}
	
	def __init__(self, enemy_id):
		self.id = enemy_id
		self.sprite = pygame.transform.scale(pygame.image.load(Enemy.enemy_data[enemy_id]['sprite']).convert(), (Enemy.enemy_data[enemy_id]['Size_x'],Enemy.enemy_data[enemy_id]['Size_y'])
		self.size = (Enemy.enemy_data[enemy_id]['Size_x'],Enemy.enemy_data[enemy_id]['Size_y'])
		self.attack = Enemy.enemy_data[enemy_id]['attack']
		self.health = Enemy.enemy_data[enemy_id]['health']
		self.Loot_item = Enemy.enemy_data[enemy_id]['Loot_item']
		self.Loot_chance = Enemy.enemy_data[enemy_id]['Loot_chance']
		self.Desc = Enemy.enemy_data[enemy_id]['Desc']
		self.Brief_Desc = Enemy.enemy_data[enemy_id]['Brief_Desc']
		self.be_attacked = False
		self.b_a_time = 0
		self.location = (0,0)

##################################################################################################

