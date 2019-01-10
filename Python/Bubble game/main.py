import pygame
import random
import math

from pygame.locals import *


# the window is the actual window onto which the camera view is resized and blitted
window_wid = 1200
window_hgt = 700
Gravity = 0.1



# the frame rate is the number of frames per second that will be displayed and although
# we could (and should) measure the amount of time elapsed, for the sake of simplicity
# we will make the (not unreasonable) assumption that this "delta time" is always 1/fps
frame_rate = 40
delta_time = 1 / frame_rate


# constants for designating the different games states
STATE_TITLE = 0
STATE_PAUSE = 1
STATE_READY = 2
STATE_OVER = 3



def detect_collision_line_circ(u, v):

	# unpack u; a line is an ordered pair of points and a point is an ordered pair of co-ordinates
	(u_sol, u_eol) = u
	(u_sol_x, u_sol_y) = u_sol
	(u_eol_x, u_eol_y) = u_eol

	# unpack v; a circle is a center point and a radius (and a point is still an ordered pair of co-ordinates)
	(v_ctr, v_rad) = v
	(v_ctr_x, v_ctr_y) = v_ctr

	# the equation for all points on the line segment u can be considered u = u_sol + t * (u_eol - u_sol), for t in [0, 1]
	# the center of the circle and the nearest point on the line segment (that which we are trying to find) define a line 
	# that is is perpendicular to the line segment u (i.e., the dot product will be 0); in other words, it suffices to take
	# the equation v_ctr - (u_sol + t * (u_eol - u_sol)) · (u_evol - u_sol) and solve for t
	
	t = ((v_ctr_x - u_sol_x) * (u_eol_x - u_sol_x) + (v_ctr_y - u_sol_y) * (u_eol_y - u_sol_y)) / ((u_eol_x - u_sol_x) ** 2 + (u_eol_y - u_sol_y) ** 2)

	# this t can be used to find the nearest point w on the infinite line between u_sol and u_sol, but the line is not 
	# infinite so it is necessary to restrict t to a value in [0, 1]
	t = max(min(t, 1), 0)
	
	# so the nearest point on the line segment, w, is defined as
	w_x = u_sol_x + t * (u_eol_x - u_sol_x)
	w_y = u_sol_y + t * (u_eol_y - u_sol_y)
	
	# Euclidean distance squared between w and v_ctr
	d_sqr = (w_x - v_ctr_x) ** 2 + (w_y - v_ctr_y) ** 2
	
	# if the Eucliean distance squared is less than the radius squared
	if (d_sqr <= v_rad ** 2):
	
		# the line collides
		return True  # the point of collision is (int(w_x), int(w_y))
		
	else:
	
		# the line does not collide
		return False

	# visit http://ericleong.me/research/circle-line/ for a good supplementary resource on collision detection


	
def game_loop_inputs(gameData,circle_hitbox):

	# look in the event queue for the quit event

	for evnt in pygame.event.get():
		if evnt.type == QUIT:
			gameData['isopen'] = False
		if pygame.key.get_pressed()[pygame.K_ESCAPE]:
			gameData['isopen'] = False
		if gameData['STATE'] == STATE_READY:
			if evnt.type == KEYDOWN:
				if gameData['hasshooted'] == True:
					if pygame.key.get_pressed()[pygame.K_LEFT]:
						circle_hitbox['ismoving'] = 'left'
					if pygame.key.get_pressed()[pygame.K_RIGHT]:
						circle_hitbox['ismoving'] = 'right'
					if pygame.key.get_pressed()[pygame.K_DOWN]:
		                 	       circle_hitbox['ismoving'] = 'down'

				else:
					if pygame.key.get_pressed()[pygame.K_LEFT]:
						gameData['launcher']['rotation'] = 'left'
					if pygame.key.get_pressed()[pygame.K_RIGHT]:
						gameData['launcher']['rotation'] = 'right'
					if pygame.key.get_pressed()[pygame.K_KP_ENTER] or pygame.key.get_pressed()[pygame.K_RETURN]:
						gameData['hasshooted'] = True
					if pygame.key.get_pressed()[pygame.K_SPACE]:
						gameData['STATE'] = STATE_PAUSE
			if evnt.type == KEYUP:
				circle_hitbox['ismoving'] = False
				gameData['launcher']['rotation'] = False
		elif gameData['STATE'] == STATE_PAUSE:
			if evnt.type == KEYDOWN:
				if pygame.key.get_pressed()[pygame.K_SPACE]:
					gameData['STATE'] = STATE_READY
	
		elif gameData['STATE'] == STATE_TITLE:
			if evnt.type == KEYDOWN:
				if pygame.key.get_pressed()[pygame.K_KP_ENTER] or pygame.key.get_pressed()[pygame.K_RETURN]:
					gameData['STATE'] = STATE_READY

		elif gameData['STATE'] == STATE_OVER:
			if evnt.type == KEYDOWN:
				if pygame.key.get_pressed()[pygame.K_KP_ENTER] or pygame.key.get_pressed()[pygame.K_RETURN]:
					gameData['STATE'] = STATE_READY
					gameData['restar'] = True
		
	return 

	
def game_loop_update(rotating_line, circle_hitbox,gameData):
	up_ACC = 0
	position=[window_wid/5,(window_wid/5)*4]
	
	if gameData['restar']:
		gameData['reload'] = True
		gameData['timer'] = 120
		gameData['life'] = 4
		gameData['restar'] = False
		gameData['score'] = 0
	
	if gameData['life'] <= 0:
		gameData['STATE'] = STATE_OVER
		return

	if gameData['reload'] and gameData['launcher']['left_top'][1] >=900:
		gameData['timer'] = 120
		gameData['launcher']['angle'] = 0
		gameData['hasshooted'] = False
		gameData['launcher']['left_top'] = [window_wid//2-100,window_hgt+150]
		gameData['tran_cir1']['color'] = [255,255,255]
		gameData['tran_cir2']['color'] = [255,255,255]
		gameData['tran_cir1']['color'] = [255,255,255]
		gameData['tran_cir1']['haschanged'] = False
		gameData['tran_cir1']['separate'] = True
		gameData['tran_cir2']['haschanged'] = False
		gameData['tran_cir2']['separate'] = True
		gameData['target']['hassetted'] = False
		circle_hitbox['color'] = [255,255,255]
		circle_hitbox['ismoving'] = False
		circle_hitbox['speed'] = [0,0]
		circle_hitbox['hasmoved'] = False
		circle_hitbox['ACC'] = [0,0]
		circle_hitbox['separate'] = True
		circle_hitbox['pos'] = [window_wid // 2, window_hgt + 170]




	if circle_hitbox['pos'][1] > window_hgt -130 and gameData['reload'] :
		circle_hitbox['pos'][1] -= 8
		gameData['launcher']['left_top'][1] -=8
		gameData['target']['location'][1] +=8
	else:
		gameData['reload'] = False


	if circle_hitbox['pos'][1] >= window_hgt and not gameData['reload']:
		gameData['life'] -= 1
		gameData['reload'] = True


	if not gameData['target']['hassetted'] and not gameData['reload'] :
		if gameData['score']//10 <= 3:
			ran_color = [0,255]
			a = random.randint(0,1)
			b = random.randint(0,1)
			c = random.randint(0,1)
		else:
			ran_color = [0,255//2,255]
			a = random.randint(0,2)
			b = random.randint(0,2)
			c = random.randint(0,2)
		gameData['target']['color'] = [ran_color[a],ran_color[b],ran_color[c]]
		if gameData['target']['color'] == [0,0,0]:
			gameData['target']['color'] = [255,0,0]
		if gameData['target']['color'] == [255,255,255]:
			gameData['target']['color'] = [0,0,255]
		if gameData['target']['color'] == [127,127,127]:
			gameData['target']['color'] = [127,0,127]
		gameData['target']['hassetted'] = True
	

	for line in gameData['lines']:
		line['start'][1] -= 10
		if line['start'][1]<= (window_hgt/4)*3:
			line['start'][1] = window_hgt
			line['start'][0] = random.randint(-50,50)+position[random.randint(0,1)]

	if circle_hitbox['pos'][0] <= 30:
		circle_hitbox['speed'][0] = circle_hitbox['speed'][0]*-1 + 1 
	if circle_hitbox['pos'][0] >= window_wid - 30:
		circle_hitbox['speed'][0] = circle_hitbox['speed'][0]*-1 - 1
	if circle_hitbox['pos'][1] <= 30:
		if circle_hitbox['pos'][0] <= window_wid/3:
			circle_hitbox['color'][0] = 255
			circle_hitbox['color'][1] = 0
			circle_hitbox['color'][2] = 0
		elif window_wid/3 < circle_hitbox['pos'][0] <= 2*window_wid/3:
			circle_hitbox['color'][0] = 0
			circle_hitbox['color'][1] = 255
			circle_hitbox['color'][2] = 0
		elif 2*window_wid/3 < circle_hitbox['pos'][0] <= window_wid:
			circle_hitbox['color'][0] = 0
			circle_hitbox['color'][1] = 0
			circle_hitbox['color'][2] = 255
		circle_hitbox['speed'][1] = circle_hitbox['speed'][1]*-1
	if not gameData['hasshooted'] and not gameData['reload']:
		if  gameData['launcher']['angle'] < 90:
			if gameData['launcher']['rotation'] == 'right':
				gameData['launcher']['angle'] += 2
		if  gameData['launcher']['angle'] > -90:
			if gameData['launcher']['rotation'] == 'left':
				gameData['launcher']['angle'] -= 2

		x0 = -1*math.sin((gameData['launcher']['angle']/180)*math.pi)*(75 - 130) + window_wid//2
		y0 = math.cos((gameData['launcher']['angle']/180)*math.pi)*(75 - 130) + window_hgt -75
		circle_hitbox['pos'] = [int(x0),int(y0)]


	if gameData['hasshooted'] and not gameData['reload']:
		if gameData['timer'] <= 0:
			gameData['state'] = STATE_OVER
		else:
			gameData['timer'] -= (1 / frame_rate)
		
		if not gameData['launcher']['left_top'][1] >= 950:
			gameData['launcher']['left_top'][1] += 8
		if gameData['launcher']['left_top'][1] >= 850 and gameData['target']['location'][1] > window_hgt +100:
			gameData['target']['location'][1] -=8
		if circle_hitbox['speed'] == [0,0] and not circle_hitbox['hasmoved']:
			circle_hitbox['speed'] = [math.sin((gameData['launcher']['angle']/180)*math.pi)*16, -1*math.cos((gameData['launcher']['angle']/180)*math.pi)*16]
			circle_hitbox['hasmoved'] = True
		if circle_hitbox['ismoving'] == 'left':
			circle_hitbox['ACC'][0] = -0.5
		if circle_hitbox['ismoving'] == 'right':
			circle_hitbox['ACC'][0] = 0.5
		if circle_hitbox['ismoving'] == 'down':
			circle_hitbox['ACC'][1] = 0.5
		if circle_hitbox['ismoving'] == False:
			circle_hitbox['ACC'] = [0,0]

		if -20 <= circle_hitbox['speed'][0] <= 20:
			circle_hitbox['speed'][0] += circle_hitbox['ACC'][0]
		if circle_hitbox['speed'][0] > 0:
			circle_hitbox['speed'][0] -= 0.1
		if circle_hitbox['speed'][0] < 0:
			circle_hitbox['speed'][0] += 0.1
		if ((window_wid/5)-85 < circle_hitbox['pos'][0] < (window_wid/5) + 85 or (window_wid/5)*4 -85 < circle_hitbox['pos'][0] < (window_wid/5)*4 + 85) and circle_hitbox['pos'][1] > (window_hgt/5)*4:
			if window_hgt-circle_hitbox['pos'][1]-15 >= 0:
				up_ACC = (((window_hgt-circle_hitbox['pos'][1]-15)/window_hgt)**0.0001)*-1.5
		

		circle_hitbox['speed'][1] += (circle_hitbox['ACC'][1] + Gravity + up_ACC)
		circle_hitbox['pos'][0] += int(circle_hitbox['speed'][0])
		circle_hitbox['pos'][1] += int(circle_hitbox['speed'][1])

		distance1 = int(((circle_hitbox['pos'][0]-gameData['tran_cir1']['location'][0])**2 + (circle_hitbox['pos'][1]-gameData['tran_cir1']['location'][1])**2)**0.5)
		distance2 = int(((circle_hitbox['pos'][0]-gameData['tran_cir2']['location'][0])**2 + (circle_hitbox['pos'][1]-gameData['tran_cir2']['location'][1])**2)**0.5)
		distance3 = int(((circle_hitbox['pos'][0]-gameData['target']['location'][0])**2 + (circle_hitbox['pos'][1]-gameData['target']['location'][1])**2)**0.5)
		if distance1 <= circle_hitbox['rad'] + gameData['tran_cir1']['radius'] and gameData['tran_cir1']['separate']:
			if gameData['tran_cir1']['haschanged'] :
				if circle_hitbox['color'] == [255,255,255]:
					circle_hitbox['color'][0] =0
					circle_hitbox['color'][1] =0
					circle_hitbox['color'][2] =0
				circle_hitbox['color'][0] += gameData['tran_cir1']['color'][0]
				circle_hitbox['color'][1] += gameData['tran_cir1']['color'][1]
				circle_hitbox['color'][2] += gameData['tran_cir1']['color'][2]
				
				
				if circle_hitbox['color'][0] >= 254:
					circle_hitbox['color'][0] =255
				if circle_hitbox['color'][1] >= 254:
					circle_hitbox['color'][1] =255
				if circle_hitbox['color'][2] >= 254:
					circle_hitbox['color'][2] =255
				
				gameData['tran_cir1']['color'] = [255,255,255]
				gameData['tran_cir1']['haschanged'] = False
			else:
				gameData['tran_cir1']['color'] = circle_hitbox['color']
				circle_hitbox['color'] = [255,255,255]
				gameData['tran_cir1']['haschanged'] = True

			gameData['tran_cir1']['separate'] = False

		if distance1 > circle_hitbox['rad'] + gameData['tran_cir1']['radius'] and not gameData['tran_cir1']['separate'] :
			gameData['tran_cir1']['separate'] = True

			
		
		if distance2 <= circle_hitbox['rad'] + gameData['tran_cir2']['radius'] and gameData['tran_cir2']['separate']:
			if gameData['tran_cir2']['haschanged'] :
				if circle_hitbox['color'][0] == 254:
					circle_hitbox['color'][0] =0
				if circle_hitbox['color'][1] == 254:
					circle_hitbox['color'][1] =0
				if circle_hitbox['color'][2] == 254:
					circle_hitbox['color'][2] =0
				circle_hitbox['color'][0] += gameData['tran_cir2']['color'][0]
				circle_hitbox['color'][1] += gameData['tran_cir2']['color'][1]
				circle_hitbox['color'][2] += gameData['tran_cir2']['color'][2]
				
				
				if circle_hitbox['color'][0] >= 255:
					circle_hitbox['color'][0] =255
				if circle_hitbox['color'][1] >= 255:
					circle_hitbox['color'][1] =255
				if circle_hitbox['color'][2] >= 255:
						circle_hitbox['color'][2] =255
				
				gameData['tran_cir2']['color'] = [255,255,255]
				gameData['tran_cir2']['haschanged'] = False
			else:
				gameData['tran_cir2']['color'] = circle_hitbox['color']
				circle_hitbox['color'] = [255,255,255]
				gameData['tran_cir2']['haschanged'] = True

			gameData['tran_cir2']['separate'] = False

		if distance2 > circle_hitbox['rad'] + gameData['tran_cir2']['radius'] and not gameData['tran_cir2']['separate']:
			gameData['tran_cir2']['separate'] = True

		if distance3 <= circle_hitbox['rad'] + gameData['target']['radius']:
			if circle_hitbox['color'] == gameData['target']['color']:
				gameData['score'] += 10
			
			else:
				gameData['life'] -= 1
			gameData['reload'] = True
	


	# increase the angle of the rotating line
	dA = (gameData['score']//10)**2/10+0.2
	if dA <= 2:
		rotating_line["ang"] = (rotating_line["ang"] + dA)
	else:
		rotating_line["ang"] = (rotating_line["ang"] + 2)


		
	# the points associated with each line segment must be recalculated as the angle changes
	rotating_line["seg"] = []
	
	# consider every line segment length
	for len in rotating_line["len"]:
	
		# compute the start of the line...
		sol_x = rotating_line["ori"][0] + math.cos(math.radians(rotating_line["ang"])) * window_wid/2 * len[0]
		sol_y = rotating_line["ori"][1] + math.sin(math.radians(rotating_line["ang"])) * window_wid/2 * len[0]
		
		# ...and the end of the line...
		eol_x = rotating_line["ori"][0] + math.cos(math.radians(rotating_line["ang"])) * window_wid/2 * len[1]
		eol_y = rotating_line["ori"][1] + math.sin(math.radians(rotating_line["ang"])) * window_wid/2 * len[1]
		
		# ...and then add that line to the list
		rotating_line["seg"].append( ((sol_x, sol_y), (eol_x, eol_y)) )

	# start by assuming that no collisions have occurred
	circle_hitbox["col"] = False
	
	# consider possible collisions between the circle hitbox and each line segment
	for seg in rotating_line["seg"]:
	
		# if there is any collision at all, the circle hitbox flag is set
		if detect_collision_line_circ(seg, (circle_hitbox["pos"], circle_hitbox["rad"])):
			circle_hitbox["col"] = True
			break
		

	if circle_hitbox["col"] and circle_hitbox['separate']:
		if circle_hitbox['color'] != [255,255,255]:
			circle_hitbox['color'][0] = circle_hitbox['color'][0]//2
			circle_hitbox['color'][1] = circle_hitbox['color'][1]//2
			circle_hitbox['color'][2] = circle_hitbox['color'][2]//2

		circle_hitbox['separate'] = False
	if not circle_hitbox["col"]:
		circle_hitbox['separate'] = True
	# return the new state of the rotating line and the circle hitbox
	return 

	
def game_loop_render(rotating_line, circle_hitbox, gameData):


	if gameData['STATE'] == STATE_TITLE:

		text1 = 'This is a prototype game of colorable bubbles'
		text2 = [
			'1.Using Left or Right key to control the angle of launcher and pressing Return or Enter key',
			'    to shoot the bubble.', 
			'2.Now,Left, Right and Down key are available to give a accelerated velocity to bubble on',
			'    direction of left,right or down.',
			'3.Gravity affects the whole mechanic, while the two jets will provide a lift force to the',
			'    bubble if they are close enough.',
			'4.The bubble will bounce off to the left, right and top, but if it falls to the bottom, it',
			'    will be judged to be a failure.',
			'5.If bubble touch the Color-blocks on the top, it will become the same color.',
			'6.Bubble can transfer its color by touch the blank bubbles for the first, and the color',
			'    transferred will be added to the buble when they touch for the second time.',
			'7.If bubble touch the scaning line, it will lose half value of RGB.',
			'8.To get scores, you need to carry the same color as the buttom bubble in your bubble and',
			'    get in touch with it.',
			'9.The status bar will give you more information.',
			'10.You can press Space bar to pause the game whenever you want.']

		text3 = 'Press Enter or Return to play. Or Escape to Exit.'


		t1 = pygame.font.SysFont("monospace", 36)
		t1_ima = t1.render(text1,1,(255,255,255))
		gameData['drawing_surface'].blit(t1_ima,(window_wid//2-t1_ima.get_size()[0]/2,80))

		for i in range(len(text2)):
			t2 = pygame.font.SysFont("monospace", 20)
			t2_ima = t2.render(text2[i],1,(255,255,255))
			gameData['drawing_surface'].blit(t2_ima,(50,190+i*30))

		t3 = pygame.font.SysFont("monospace", 28)
		t3_ima = t3.render(text3,1,(255,255,255))
		gameData['drawing_surface'].blit(t3_ima,(window_wid//2-t3_ima.get_size()[0]/2,710))


	if gameData['STATE'] == STATE_OVER:
		
		gameData['drawing_surface'].fill((0,0,0))
				
		text1 = 'Your Scores: '+str(gameData['score'])
		text2 = 'Press Enter or Return to retry. Or Escape to Exit.'

		t1 = pygame.font.SysFont("monospace", 36)
		t1_ima = t1.render(text1,1,(255,255,255))
		gameData['drawing_surface'].blit(t1_ima,(window_wid//2-t1_ima.get_size()[0]/2,280))

		t2 = pygame.font.SysFont("monospace", 28)
		t2_ima = t2.render(text2,1,(255,255,255))
		gameData['drawing_surface'].blit(t2_ima,(window_wid//2-t2_ima.get_size()[0]/2,400))




	if gameData['STATE'] == STATE_READY:
		gameData['screen'].fill( (255,255,255) )
		gameData['drawing_surface'].fill( (0,0,0) )

		pygame.draw.rect(gameData['drawing_surface'],(255,0,0),(0,80,window_wid/3,20))
		pygame.draw.rect(gameData['drawing_surface'],(0,255,0),(window_wid/3,80,window_wid/3,20))	
		pygame.draw.rect(gameData['drawing_surface'],(0,0,255),(2*window_wid/3,80,window_wid/3,20))




		# draw each of the rotating line segments
		for seg in rotating_line["seg"]:
	
			pygame.draw.aaline(gameData['screen'], (0, 0, 0), seg[0], seg[1])

		for line in gameData['lines']:
		
			pygame.draw.aaline(gameData['screen'], (0, 0, 0),(line['start'][0],line['start'][1]),(line['start'][0],line['start'][1]+line['lenth']))

		for noz in gameData['nozzles']['location']:
			gameData['screen'].blit(gameData['nozzles']['sprite'],noz)

		pygame.draw.circle(gameData['screen'], circle_hitbox['color'], circle_hitbox["pos"], circle_hitbox["rad"])
	
	
		# draw the circle hitbox, in red if there has been a collision or in white otherwise
		if circle_hitbox["col"]:
	
			pygame.draw.circle(gameData['screen'], (255, 0, 0), circle_hitbox["pos"], circle_hitbox["rad"])
		
		else:
	
			pygame.draw.circle(gameData['screen'], circle_hitbox['color'], circle_hitbox["pos"], circle_hitbox["rad"])


		image = pygame.transform.rotate(gameData['launcher']['sprite'],-1*gameData['launcher']['angle'])
		left_top = (gameData['launcher']['left_top'][0]+100-image.get_size()[0]/2,gameData['launcher']['left_top'][1]+75-image.get_size()[1]/2,)
		gameData['screen'].blit(image,left_top)

		pygame.draw.circle(gameData['screen'],gameData['tran_cir1']['color'],gameData['tran_cir1']['location'],gameData['tran_cir1']['radius'])
		pygame.draw.circle(gameData['screen'],gameData['tran_cir2']['color'],gameData['tran_cir2']['location'],gameData['tran_cir2']['radius'])
		pygame.draw.circle(gameData['screen'],gameData['target']['color'],gameData['target']['location'],gameData['target']['radius'])

		if gameData['tran_cir1']['haschanged']:
			gameData['screen'].blit(gameData['locked'],(5,window_hgt//2-15))
		else:
			gameData['screen'].blit(gameData['unlocked'],(5,window_hgt//2-15))

		if gameData['tran_cir2']['haschanged']:
			gameData['screen'].blit(gameData['locked'],(window_wid-30,window_hgt//2-15))
		else:
			gameData['screen'].blit(gameData['unlocked'],(window_wid-30,window_hgt//2-15))

		pygame.draw.circle(gameData['screen'],(0,0,0),circle_hitbox['pos'],circle_hitbox["rad"],3)
		pygame.draw.circle(gameData['screen'],(0,0,0),gameData['tran_cir1']['location'],gameData['tran_cir1']['radius'],3)
		pygame.draw.circle(gameData['screen'],(0,0,0),gameData['tran_cir2']['location'],gameData['tran_cir2']['radius'],3)
	
		pygame.draw.circle(gameData['screen'],(0,0,0),gameData['target']['location'],gameData['target']['radius'],3)

		gameData['drawing_surface'].blit(gameData['screen'],(0,100))

		score = pygame.font.SysFont("monospace", 32)
		text_score = score.render("You Scores: "+str(int(gameData['score'])), 1, (255,255,255))
		gameData['drawing_surface'].blit(text_score,(10,20))
	
		excess_time = pygame.font.SysFont("monospace", 32)
		text_time = score.render(str(int(gameData['timer'])), 1, (255,255,255))
		gameData['drawing_surface'].blit(text_time,(1120,20))
	
		
		color = pygame.font.SysFont("monospace", 32)
		text_color = color.render(' = '+str(gameData['target']['color']),1,(255,255,255))
		gameData['drawing_surface'].blit(text_color,(window_wid/2-text_color.get_size()[0]/2-50,20))
		pygame.draw.rect(gameData['drawing_surface'],gameData['target']['color'],(window_wid/2-text_color.get_size()[0]/2-80,20,30,30))
		for i in range(gameData['life']):
			gameData['drawing_surface'].blit(gameData['redCrystal'],(window_wid/2+240+i*30,20))

	# update the display
	pygame.display.update()

	

def main():
	
	# initialize pygame
	pygame.init()
	
	# create the window and set the caption of the window
	screen = pygame.Surface( (window_wid, window_hgt) )
	drawing_surface = pygame.display.set_mode((window_wid, window_hgt+100))
	pygame.display.set_caption('"Toy" for the MDA Exercise')
	
	# create a clock
	clock = pygame.time.Clock()

	# this is the initial game state
	lines = []
	for i in range(20):
		if i<10:
			lines.append({'start':[random.randint(-50,50)+window_wid/5, window_hgt-random.randint(50,200)],'lenth':random.randint(0,window_wid/4)})
		else:
			lines.append({'start':[random.randint(-50,50)+(window_wid/5)*4,window_hgt - random.randint(0,50)],'lenth':random.randint(0,window_wid/4)})

	nozzles = {'sprite':pygame.transform.scale(pygame.image.load("nozzle.png").convert_alpha(),(140,40)),'location':[(window_wid/5-70,window_hgt-30),((window_wid/5)*4-70,window_hgt-30)]}

	launcher = {'sprite':pygame.transform.scale(pygame.image.load("launcher.png").convert_alpha(),(200,150)),'left_top':[window_wid/2-100,window_hgt-150],'rotation':False, 'angle': 0}

	
	gameData = {}
	gameData['STATE'] = STATE_TITLE
	gameData['reload'] = False
	gameData['screen'] = screen
	gameData['drawing_surface'] = drawing_surface
	gameData['isopen'] = True
	gameData['hasshooted'] = False
	gameData['lines'] = lines
	gameData['nozzles'] = nozzles
	gameData['launcher'] = launcher
	gameData['life'] = 4
	gameData['restar'] = False
	gameData['locked'] = pygame.transform.scale(pygame.image.load("locked.png").convert_alpha(),(30,30))
	gameData['unlocked'] = pygame.transform.scale(pygame.image.load("unlocked.png").convert_alpha(),(30,30))
	gameData['redCrystal'] = pygame.transform.scale(pygame.image.load("redCrystal.png").convert_alpha(),(30,30))
	gameData['score'] = 0
	gameData['timer'] = 120
	gameData['tran_cir1'] = {'location':[-20,window_hgt//2],'color':[255,255,255],'radius':80,'haschanged': False,'separate': True}
	gameData['tran_cir2'] = {'location':[window_wid+20,window_hgt//2],'color':[255,255,255],'radius':80,'haschanged': False,'separate': True}
	gameData['target'] = {'location':[window_wid//2,window_hgt+170],'color':[255,255,255],'radius':160,'hassetted': False}

	#####################################################################################################
	# these are the initial game objects that are required (in some form) for the core mechanic provided
	#####################################################################################################

	# this game object is a line segment, with a single gap, rotating around a point
	rotating_line = {}
	rotating_line["ori"] = (window_wid//2, window_hgt//2)               # the "origin" around which the line rotates 
	rotating_line["ang"] = 135                             # the current "angle" of the line
	rotating_line["len"] = [ (0.00, 0.20), (0.45,0.55),(0.80, 1.00) ]  # the "length" intervals that specify the gap(s)
	rotating_line["seg"] = [ ]                             # the individual "segments" (i.e., non-gaps)

	# this game object is a circulr
	circle_hitbox = {}
	circle_hitbox["pos"] = [window_wid // 2, window_hgt - 130]
	circle_hitbox["rad"] = 30
	circle_hitbox["col"] = False
	circle_hitbox['color'] = [255,255,255]
	circle_hitbox['ismoving'] = False
	circle_hitbox['speed'] = [0,0]
	circle_hitbox['hasmoved'] = False
	circle_hitbox['ACC'] = [0,0]
	circle_hitbox['separate'] = True
	
	# the game loop is a postcondition loop controlled using a Boolean flag

	while gameData['isopen']:

		
	
		game_loop_inputs(gameData,circle_hitbox)
		

		if gameData['STATE'] == STATE_PAUSE:
			continue

		
		game_loop_update(rotating_line, circle_hitbox,gameData) 
		


		game_loop_render(rotating_line, circle_hitbox, gameData)
		
			# enforce the minimum frame rate
		clock.tick(frame_rate)
		
		
if __name__ == "__main__":
	main()
