#Yiwei Zhang & Weihang Chen & Sue Yang
import pygame
import math
import csv
import random
from helper_functions import *
from room import *
from item import *
from player import *
from minimap import *
import sys



#### ====================================================================================================================== ####
#############                                         INITIALIZE                                                   #############
#### ====================================================================================================================== ####


def initialize():
    ''' Initialization function - initializes various aspects of the game including settings, shop, and more.
    Input: None
    Output: game_data dictionary
    '''
    pygame.display.set_caption("Insomnia Dungeon-Yiwei, Weihang and Sue's")

    # Initialize game_data and return it
    game_data = { "screen": pygame.display.set_mode((800,600)),
                  "cur_currency": 50,
                  'cur_loc':1,
                  "stay_open": 1,
                  "map": {},
                  "player":Player(),
                  "Inventory":{},
                  'Hint':" You can drag the item onto your avatar or some interactive item in the Room to use it.  ",
	              'bag':[],
	              "clicked":False,
	              "selected_item":None,
                      "UI":pygame.Surface((800,200)),
	              "surface_player":pygame.Surface((300,200)),
	              "surface_bag":pygame.Surface((300,150)),
                      "surface_minimap":pygame.Surface((300,150)),
                      "BorM":"map",
                      "Event":"Room No.1"
                  }

    for aroom in Room.map_data:
    	game_data['map'][int(aroom)] = Room(aroom)
    Init_item(game_data['map'])

    return game_data
#### ====================================================================================================================== ####
#############                                           PROCESS                                                    #############
#### ====================================================================================================================== ####
def process(game_data):
    ''' Processing function - handles all form of user input. Raises flags to trigger certain actions in Update().
    Input: game_data dictionary
    Output: None
    '''
    for event in pygame.event.get():

        # Handle [X] press
        if event.type == pygame.QUIT:
            game_data["stay_open"] = 0

        # Handle Mouse Button Down
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_data["clicked"] = True
            #game_data["selected_tower"] = False

        # Handle Mouse Button Up
        if event.type == pygame.MOUSEBUTTONUP:
            game_data["clicked"] = False

#### ====================================================================================================================== ####
#############                                         UPDATE                                                 #############
#### ====================================================================================================================== ####


def coll_rect(loc, zone): 
 #loc :(x,y) the stating pos of the collision region;
 #zone :(w,h)  the width and height of the collision zone.
	(mX, mY) = pygame.mouse.get_pos()
	if loc[0]<=mX<=loc[0]+zone[0] and loc[1]<=mY<=loc[1]+zone[1]:
		return True
	else:
		return False

def update_exits(game_data,DirDic):
	'''
	DirDic: a dictionary including all information of a single exist.
           Eg: Room_Object.U,Room_Object.D,Room_Object.N,Room_Object.S,Room_Object.W,Room_Object.E. 
	'''
	#DirDic['open']=True
	if  DirDic['linked'] is not None:
		if  coll_rect(DirDic['render_loc'],DirDic['render_zone']):
			if game_data["clicked"]==True and DirDic['open']: 
				#game_data['map'][DirDic['linked']].D['open']=  True
				game_data['cur_loc']=DirDic['linked']
				game_data['Event']="Room No.{}".format(game_data['cur_loc'])
				game_data["clicked"]=False
			elif game_data["clicked"]==False and DirDic['open']:
				game_data['Hint']= "This path leads to Room No.{}.".format(DirDic['linked'])
			elif DirDic['open']==False:
				if DirDic['gear_type'][0]=='S':
					if game_data['player'].san>=DirDic['gear_value'] and game_data["clicked"]:
						DirDic['open']=True
						game_data["clicked"]=False
					else:
						game_data['Hint']= DirDic['Hint']
				if DirDic['gear_type'][0]=='I':
					if len(game_data['bag'])>=DirDic['gear_value'] and game_data["clicked"]:
						DirDic['open']=True
						game_data["clicked"]=False
					else:
						game_data['Hint']= DirDic['Hint']
				if DirDic['gear_type'][0]=='H':
					if game_data['player'].health>=DirDic['gear_value'] and game_data["clicked"]:
						DirDic['open']=True
						game_data["clicked"]=False
					else:
						game_data['Hint']= DirDic['Hint']
				else:
					game_data['Hint']= DirDic['Hint']
	
	return game_data,DirDic	


def update(game_data, curRoom):
	if game_data['cur_loc']==100:
		game_data['stay_open']=2
		return
	check_equip(game_data['player'],game_data['bag'])
	if game_data["clicked"]:
		take_item(curRoom,game_data['bag'])
	game_data['Hint']=" Collect All keys to wake up from the nightmare. "
	game_data,curRoom.U=update_exits(game_data,curRoom.U)
	game_data,curRoom.D=update_exits(game_data,curRoom.D)
	game_data,curRoom.N=update_exits(game_data,curRoom.N)
	game_data,curRoom.S=update_exits(game_data,curRoom.S)
	game_data,curRoom.W=update_exits(game_data,curRoom.W)
	game_data,curRoom.E=update_exits(game_data,curRoom.E)


def render_exits(game_data,DirDic,curRoom):
	DirDic['open']==True
	if  DirDic['linked'] is not None:
		#DirDic['open']=True  #temp
		if DirDic['open']==True :
			game_data["screen"].blit( DirDic['open_sprite'], DirDic['render_loc'] )  
		else:
			game_data["screen"].blit( DirDic['close_sprite'], DirDic['render_loc'] )  


def render_hint(game_data):
	scorefont=pygame.font.Font(None,20)
	Ocolor=(250,10,20)
	#draw the name of socre 
	Hint=scorefont.render("Hint:{}".format(game_data['Hint']),1,Ocolor)                 
	game_data["screen"].blit(Hint, (100, 20))

def render_event(game_data):
	scorefont=pygame.font.Font(None,22)
	Ocolor=(200,100,20)
	#draw the name of socre 
	Event=scorefont.render("{}".format(game_data['Event']),1,Ocolor)                 
	game_data["screen"].blit(Event, (20, 350))


def render(game_data,curRoom):


	game_data["screen"].blit(curRoom.Sprite, (0, 0))  
	#game_data["screen"].blit(pygame.image.load("assets/room/Room_1.png").convert_alpha(), (0, 0)) 
	render_exits(game_data,curRoom.U,curRoom)
	render_exits(game_data,curRoom.D,curRoom)
	render_exits(game_data,curRoom.N,curRoom)
	render_exits(game_data,curRoom.W,curRoom)
	render_exits(game_data,curRoom.E,curRoom)
	render_exits(game_data,curRoom.S,curRoom)

	render_hint(game_data)
	render_event(game_data)
	render_item(curRoom,game_data['screen'])
	game_data["UI"].blit(pygame.image.load("assets/UI.png"),(0,0))	
	game_data["screen"].blit(game_data['UI'],(0,400))
	render_player(game_data['player'],game_data['screen'])
	if game_data['BorM'] == 'map':
		game_data['surface_minimap'] = minimap(game_data['cur_loc'],curRoom.Layer,game_data['surface_minimap'])
	game_data["screen"].blit(game_data['surface_minimap'],(412,415))
	


	render_bag(game_data['bag'],game_data['surface_bag'],game_data['screen'])

def ending1(game_data):

	pic = pygame.image.load('assets/ending.png')
	game_data['screen'].blit(pic,(0,0))

def music(game_data,curRoom):
	if curRoom.Layer==1:
		pygame.mixer.music.load('sound/Layer1.mp3')
	elif curRoom.Layer==2:
		pygame.mixer.music.load('sound/Layer2.mp3')
	else:
		pygame.mixer.music.load('sound/Layer3.mp3')
	pygame.mixer.music.play(-1)

#### ====================================================================================================================== ####
#############                                       Main Function                                             #############
#### ====================================================================================================================== ####
def main():
    ''' Main function - initializes everything and then enters the primary game loop.
    Input: None
    Output: None
    '''
    # Initialize all required variables and objects
    pygame.init()
    game_data = initialize()
    music(game_data,game_data['map'][game_data['cur_loc']])
    # Begin Central Game Loop
    while game_data["stay_open"]!=0:
        if game_data["stay_open"]==1:
            process(game_data)
            update(game_data,game_data['map'][game_data['cur_loc']])
            render(game_data,game_data['map'][game_data['cur_loc']])
        elif game_data["stay_open"]==2:
            break
        pygame.display.update()
    pygame.mixer.music.load('sound/ending.mp3')
    pygame.mixer.music.play(-1)
    while game_data["stay_open"]!=0:
        	process(game_data)
        	ending1(game_data)
        	pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    main()
