import pygame
from helper_functions import *

def minimap(room_num,map_num,sur_minimap):
	map_name = 'map' + str(map_num) + '.csv' 
	Map = csv_loader(map_name)
	room_num = str(room_num)
	sur_minimap.fill((0,0,0))
	player_loc = [200,200]
	sur_minimap.fill((51,42,31))
	for r in range(len(Map)):
		for c in range(len(Map[r])):
			if Map[r][c] == room_num:
				player_loc = [c,r]
				break
	#print(room_num,map_num)
	for row in range(len(Map)):
		for col in range(len(Map[row])):
			if Map[row][col] != '0':
				pygame.draw.rect(sur_minimap,(255,255,255),(20+col*35,20+row*35,30,30))
				try:
					if Map[row][col-1] != '0' and col >= 1:
						pygame.draw.line(sur_minimap,(255,255,255),(20+col*35+15,20+row*35+15),(20+(col-1)*35+15,20+row*35+15),3)
				except:
					pass
				try:
					if Map[row][col+1] != '0' and col <= 2:
						pygame.draw.line(sur_minimap,(255,255,255),(20+col*35+15,20+row*35+15),(20+(col+1)*35+15,20+row*35+15),3)
				except:
					pass
				try:
					if Map[row-1][col] != '0' and row >= 1:
						pygame.draw.line(sur_minimap,(255,255,255),(20+col*35+15,20+row*35+15),(20+col*35+15,20+(row-1)*35+15),3)
				except:
					pass
				try:

					if Map[row+1][col] != '0' and row <= 2:
						pygame.draw.line(sur_minimap,(255,255,255),(20+col*35+15,20+row*35+15),(20+col*35+15,20+(row+1)*35+15),3)
				except:
					pass
	pygame.draw.circle(sur_minimap,(255,0,0),(35+player_loc[0]*35,35+player_loc[1]*35),8)
	return sur_minimap


