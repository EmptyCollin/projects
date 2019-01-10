import pygame
from helper_functions import *



##################################################################################################

class Item:
	item_data = {}
	for item in csv_loader('item.csv'):
		item_data[item[0]] = {'function':item[1],'name': item[2],'sprite':item[3],'Desc':item[4]}
	
	def __init__(self, item_id,location):
		self.id = item_id
		self.name = Item.item_data[str(item_id)]['name']
		self.sprite = pygame.image.load(Item.item_data[str(item_id)]['sprite']).convert_alpha()
		self.icon = pygame.transform.scale(pygame.image.load(Item.item_data[str(item_id)]['sprite']).convert_alpha(),(50,50))
		self.size = pygame.image.load(Item.item_data[str(item_id)]['sprite']).convert_alpha().get_size()
		self.function = Item.item_data[str(item_id)]['function']
		self.Desc = Item.item_data[str(item_id)]['Desc']
		self.Brief_Desc = None
		self.location = location	

##################################################################################################


def take_item(room,bag):
	x = pygame.mouse.get_pos()[0]
	y = pygame.mouse.get_pos()[1]
	item = None
	for Item in room.Items:
		if Item.location[0] <= x <= Item.location[0]+Item.size[0] and Item.location[1] <= y <= Item.location[1]+Item.size[1]:
			item = Item
			break
	
	if item != None:
		add_item = item
		bag.append(add_item)
		room.Items.remove(item)
	
##################################################################################################

def render_bag(bag,sur_bag,screen):
	line = -1
	sur_bag.fill((51,42,31))

	for col in range(len(bag)):
		c = col%3
		if c == 0:
			line += 1
		sur_bag.blit(bag[col].icon,(c*60,60*line))
	screen.blit(sur_bag,(620,420))

def render_item(room,screen):
	for i in room.Items:
		screen.blit(i.sprite,i.location)
				
