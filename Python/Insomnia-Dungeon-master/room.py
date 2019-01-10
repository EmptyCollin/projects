#### ====================================================================================================================== ####
#############                                           IMPORTS                                                    #############
#### ====================================================================================================================== ####

import csv
from helper_functions import *
from main import *

#### ====================================================================================================================== ####
#############                                           ROOM_Class                                                 #############
#### ====================================================================================================================== ####

class Room:
    ''' Enemy Class - represents a single Enemy Object. '''
    # Represents common data for all enemies - only loaded once, not per new Enemy (Class Variable)
    map_data = {}
    for row in csv_loader("Map.csv"):
        map_data[int(row[0])] = {"Name": row[1], 
                                  "Overlook": row[2],
                                  "Desc": row[3],
                                  'U':int(row[4]),
                                  'U_type':row[5],
                                  'D':int(row[6]),
                                  "D_type":row[7],
                                  'N':int(row[8]),
                                  "N_type":row[9],
                                  'S':int(row[10]),
                                  "S_type":row[11],
                                  'W':int(row[12]),
                                  "W_type":row[13],
                                  'E':int(row[14]),
                                  "E_type":row[15],
                                  "Item1":row[16].split(','),
                                  "Item2":row[17].split(','),
                                  "Item3":row[18].split(','),
                                  'Enemy':row[19].split(',')[:3],
                                  'Buff':row[20].split(),
                                  'Buff_Desc':row[21],
                                  'Layer':int(row[22])}
    gear_type={"Money1":[10,'Raise your atk to unlock'],
                "SAN>":[105,'Be sober. It only allows you to go through with at least 105 SAN.'],
                "SAN115":[115,'Be sober. It only allows you to go through with at least 115 SAN.'],
                "SAN130":[130,'Be sober. It only allows you to go through with at least 130 SAN.'],
                "SAN165":[160,'Be sober. It only allows you to go through with at least 160 SAN.'],
                "HP>":[105,"Crazier Nightmare, which only allows you to go through with at least 105 HP."],
                "HP115":[115,"Crazier Nightmare, which only allows you to go through with at least 115 HP."],
                "HP130":[130,"Crazier Nightmare, which only allows you to go through with at least 135 HP."],
                "HP165":[160,"Crazier Nightmare, which only allows you to go through with at least 160 HP."],
                "Item2":[2,"You need to carry 2 items to go through."],
                "Item4":[4,"You need to carry 4 items to go through."],
                "Item6":[6,"You need to carry 6 items to go through."],
                "Item9":[9,"You need to carry 9 items to Wake Up."],
                "0":None
                }
    nul_dic={"linked":None,
                    "render_zone":None,
                    "render_loc":None,
                    "gear_type":"0",
                    "gear_value":None,
                    'open':False,
                    'close_sprite':None,
                    'open_sprite':None,
                    'Hint':None}            

    item_loc=[(100,200),(200,200),(200,100),(100,100)]
                                  
    def __init__(self, room_No):
        self.room_No=room_No,
        self.Name=Room.map_data[room_No]["Name"],
        self.Brief_Desc=Room.map_data[room_No]["Overlook"],
        self.Desc= Room.map_data[room_No]["Desc"],
        # Up entrance data
        if Room.map_data[room_No]["U"]==0:
            self.U=Room.nul_dic
        else:
            self.U={"linked":Room.map_data[room_No]["U"],
                    "render_zone":(140,200),
                    "render_loc":(244,97),
                    "gear_type":Room.map_data[room_No]["U_type"],
                    "gear_value":Room.gear_type[Room.map_data[room_No]["U_type"]][0],
                    'open':False,
                    'close_sprite':pygame.image.load("assets/room/Exit_U_close.png").convert_alpha(),
                    'open_sprite':pygame.image.load("assets/room/Exit_U_open.png").convert_alpha(),
                    'Hint':Room.gear_type[Room.map_data[room_No]["U_type"]][1]}
        
        # Down entrance data
        if Room.map_data[room_No]["D"]==0:
            self.D=Room.nul_dic
        else:
            self.D={"linked":Room.map_data[room_No]["D"],
                    "render_zone":(260,60),
                    "render_loc":(265,285),
                    "gear_type":Room.map_data[room_No]["D_type"],
                    "gear_value":Room.gear_type[Room.map_data[room_No]["D_type"]][0],
                    'open':False,
                    'close_sprite':pygame.image.load("assets/room/Exit_D_close.png").convert_alpha(),
                    'open_sprite':pygame.image.load("assets/room/Exit_D_open.png").convert_alpha(),
                    'Hint':Room.gear_type[Room.map_data[room_No]["D_type"]][1]}
        
        #  North entrance data
        if Room.map_data[room_No]["N"]==0:
            self.N=Room.nul_dic
        else:
            self.N={"linked":Room.map_data[room_No]["N"],
                    "render_zone":(88,158),
                    "render_loc":(463,144),
                    "gear_type":Room.map_data[room_No]["N_type"],
                    "gear_value":Room.gear_type[Room.map_data[room_No]["N_type"]][0],
                    'open':False,
                    'close_sprite':pygame.image.load("assets/room/Exit_N_close.png").convert_alpha(),
                    'open_sprite':pygame.image.load("assets/room/Exit_N_open.png").convert_alpha(),
                    'Hint':Room.gear_type[Room.map_data[room_No]["N_type"]][1]}    
        #  South entrance data
        if Room.map_data[room_No]["S"]==0:
            self.S=Room.nul_dic
        else:
            self.S={"linked":Room.map_data[room_No]["S"],
                    "render_zone":(138,30),
                    "render_loc":(331,373),
                    "gear_type":Room.map_data[room_No]["S_type"],
                    "gear_value":Room.gear_type[Room.map_data[room_No]["S_type"]][0],
                    'open':False,
                    'close_sprite':pygame.image.load("assets/room/Exit_S_close.png").convert_alpha(),
                    'open_sprite':pygame.image.load("assets/room/Exit_S_open.png").convert_alpha(),
                    'Hint':Room.gear_type[Room.map_data[room_No]["S_type"]][1]}    

        #  West entrance data
        if Room.map_data[room_No]["W"]==0:
            self.W=Room.nul_dic
        else:
            self.W={"linked":Room.map_data[room_No]["W"],
                    "render_zone":(61,234),
                    "render_loc":(86,130),
                    "gear_type":Room.map_data[room_No]["W_type"],
                    "gear_value":Room.gear_type[Room.map_data[room_No]["W_type"]][0],
                    'open':False,
                    'close_sprite':pygame.image.load("assets/room/Exit_W_close.png").convert_alpha(),
                    'open_sprite':pygame.image.load("assets/room/Exit_W_open.png").convert_alpha(),
                    'Hint':Room.gear_type[Room.map_data[room_No]["W_type"]][1]}    
        #  East entrance data
        if Room.map_data[room_No]["E"]==0:
            self.E=Room.nul_dic
        else:
            self.E={"linked":Room.map_data[room_No]["E"],
                    "render_zone":(61,234),
                    "render_loc":(649,122),
                    "gear_type":Room.map_data[room_No]["E_type"],
                    "gear_value":Room.gear_type[Room.map_data[room_No]["E_type"]][0],
                    'open':False,
                    'close_sprite':pygame.image.load("assets/room/Exit_E_close.png").convert_alpha(),
                    'open_sprite':pygame.image.load("assets/room/Exit_E_open.png").convert_alpha(),
                    'Hint':Room.gear_type[Room.map_data[room_No]["E_type"]][1]}                    

        self.Layer=Room.map_data[room_No]["Layer"]
        if Room.map_data[room_No]["Layer"]==1:
            self.Sprite=pygame.image.load("assets/room/Room_1.png").convert_alpha()
        elif Room.map_data[room_No]["Layer"]==2:
            self.Sprite=pygame.image.load("assets/room/Room_3.png").convert_alpha()
        else :
            self.Sprite=pygame.image.load("assets/room/Room_2.png").convert_alpha()
        self.Enemy=Room.map_data[room_No]["Enemy"],
        self.Buff_Desc=Room.map_data[room_No]["Buff_Desc"],
        self.Buff=Room.map_data[room_No]["Buff"],
        self.Enemy={}  
        self.Items=[] # items in this room


def Init_item(map0):
    for room_num in range(1,len(map0)):
        if map0[int(room_num)].room_No[0] == 1:
            map0[int(room_num)].Items.append(Item(3,(100,100)))
        if map0[int(room_num)].room_No[0] == 2:
            map0[int(room_num)].Items.append(Item(1,(600,300)))
        if map0[int(room_num)].room_No[0] == 8:
            map0[int(room_num)].Items.append(Item(2,(460,290)))
        if map0[int(room_num)].room_No[0] == 4:
            map0[int(room_num)].Items.append(Item(4,(100,350)))
        if map0[int(room_num)].room_No[0] == 15:
            map0[int(room_num)].Items.append(Item(5,(200,200)))
        if map0[int(room_num)].room_No[0] == 6:
            map0[int(room_num)].Items.append(Item(6,(170,230)))
        if map0[int(room_num)].room_No[0] == 14:
            map0[int(room_num)].Items.append(Item(7,(300,280)))
        if map0[int(room_num)].room_No[0] == 12:
            map0[int(room_num)].Items.append(Item(8,(720,210)))
        if map0[int(room_num)].room_No[0] == 3:
            map0[int(room_num)].Items.append(Item(9,(500,370)))
