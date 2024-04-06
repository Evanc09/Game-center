from random import randint as r
import sys
import pygame
import tkinter as tk
pygame.mixer.init()
def astroids():
    import tkinter as tk
    from tkinter import Button
    import sys  
    root.destroy()
    
    try:
        from utils2 import main, TWO_player_Free_play, lives
    except ImportError as ie:
        print(f"Could not import(E: {ie})")
        sys.exit()
    root1 = tk.Tk()
    def destroy(root1):
            root1.destroy()
    b1=Button(text="normal", command=lambda:[destroy(root1), main(lives)])
    testButton = Button(text="Free Play", command=lambda:[destroy(root1),TWO_player_Free_play.Free_play() ])
    testButton.pack()
    b1.pack()
    root1.mainloop()
    
def game():
	root.destroy()
	pygame.init()
	level = 1
	speed = [r(0, 2), r(0 ,2)]

	win = pygame.display.set_mode((1000, 600))


	pygame.display.set_caption("Go fishing")


	def mainloop(level, speed):
		def blit_text_center(win, font, text):
						render = font.render(text, 1, (200, 200, 200))
						win.blit(render, (win.get_width()/2 - render.get_width() /
										2, win.get_height()/2 - render.get_height()/2))
		def blit_text_center2(win, font, text):
						render = font.render(text, 1, (200, 200, 200))
						win.blit(render, (win.get_width()/2 - render.get_width() /
										2, win.get_height()/1 - render.get_height()/1))
		MAIN_FONT = pygame.font.SysFont("comicsans", 44)
		run = True
		x = 500
		y = 50
		x2 = 600
		y2 = 50
		red = (165, 42, 42)
		ball_obj = pygame.draw.circle(
			surface=win, color=red, center=[100, 100], radius=20)
		
		width = 20
		height = 20
		width2 = 1000
		height2 = 600
		
		vel = 2
		text = "To procced to the next level,"
		text2 = "touch the red ball and press space"
		blit_text_center(win, MAIN_FONT, f"{text}")
		blit_text_center2(win, MAIN_FONT, f"{text2}")
		pygame.display.update()
		pygame.time.delay(4000)
		while run:
			
			
			pygame.time.delay(10)
			
			
				
			
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					
					# it will make exit the while loop
					exit()
			# stores keys pressed
			keys = pygame.key.get_pressed()
			
			# if left arrow key is pressed
			
				
			
			if keys[pygame.K_LEFT] and x>0:
				
				# decrement in x co-ordinate
				x -= vel
				
			# if left arrow key is pressed
			if keys[pygame.K_RIGHT] and x<1000-width:
				
				# increment in x co-ordinate
				x += vel
				
			# if left arrow key is pressed
			if keys[pygame.K_UP] and y>0:
				
				# decrement in y co-ordinate
				y -= vel
				
			# if left arrow key is pressed
			if keys[pygame.K_DOWN] and y<600-height:
				# increment in y co-ordinate
				y += vel
				
			if keys[pygame.K_a] and x2>0:
				x2 -= vel

			if keys[pygame.K_w] and y2>0:
					y2 -= vel
			if keys[pygame.K_s] and y2<600-height:
				y2 += vel
			if keys[pygame.K_d] and x2<1000-width:
				x2 += vel
			

			# completely fill the surface object
			# with black colour
			c3 = (165, 42, 42)
			c2= (165,42,42)
			# drawing object on screen which is rectangle here
			p1 = pygame.draw.rect(win, (c3), (x, y, width, height))
			p2 = pygame.draw.rect(win, (c2), (x2, y2, width, height))
			
			
			ball_obj = ball_obj.move(speed)		
		
			if ball_obj.left <= 0 or ball_obj.right >= width2:
				speed[0] = -speed[0]
			if ball_obj.top <= 0 or ball_obj.bottom >= height2:
				speed[1] = -speed[1]
			pygame.draw.circle(surface=win, color=red,
							center=ball_obj.center, radius=20)
			# it refreshes the window
			pygame.display.flip()
			pygame.display.update()
			collide = pygame.Rect.colliderect(p1, p2)
			if_win = pygame.Rect.colliderect(p1, ball_obj)
			if_win2 = pygame.Rect.colliderect(p2, ball_obj)
			
			if if_win or if_win2:
				if keys[pygame.K_SPACE]:
					win.fill(red)
					
					def blit_text_center3(win, font, text):
						render = font.render(text, 1, (200, 200, 200))
						win.blit(render, (win.get_width()/2 - render.get_width() /
										2, win.get_height()/3 - render.get_height()/2))
					MAIN_FONT = pygame.font.SysFont("comicsans", 44)
					mp3_up = open("up.mp3")
					pygame.mixer.music.load(mp3_up)
					pygame.mixer.music.play()
					if level == 10:
						blit_text_center(win, MAIN_FONT, f"YOU WON THE GAME!!!")
						pygame.display.update()
						mp3_win = open("win.mp3")
						pygame.mixer.music.load(mp3_win)
						pygame.mixer.music.play()
						pygame.time.delay(4000)
						sys.exit()
					
					next_level = level +1
					level = level +1
					if level == 2:
						speed = [r(2, 3)-1, r(2, 3)-1]
					if level == 3:
						speed = [r(3, 4)-1, r(3, 4)-1]
					if level == 4:
						speed = [r(4, 5)-1, r(4, 5)-1]
					if level == 5:
						speed = [r(5, 6)-1, r(5, 6)-1]
					if level == 6:
						speed = [r(6, 7)-1, r(6, 7)-1]
					if level == 7:
						speed = [r(7, 8)-1, r(7, 8)-1]
					if level == 8:
						speed = [r(8 ,9)-1, r(8, 9)-1]
					if level == 9:
						speed = [r(9, 10)-1, r(9, 10)-1]
					
					blit_text_center3(win , MAIN_FONT, f"YOU WON ! next level = {next_level} good luck")
					pygame.display.update()
					pygame.time.delay(4000)
					mainloop(level, speed)
				else:
					continue
		
				
					
			if collide:
				for i in range(1):
					y = y -1
					x = x -1
					y2 = y2 +1
					x2 = x2 + 1 
					break
			win.fill((0, 0, 255))
	mainloop(level, speed)
root = tk.Tk()
def exit():
	sys.exit()
def destroy():
	root.destroy()

b = tk.Button
b1 = b(text="Play Fishing", command=lambda:[game()])
b3 = b(text="Exit", command=lambda:[exit()])
b2 = b(text="Play astroids", command=lambda:[astroids()])

b1.pack()
b2.pack()
b3.pack()
root.mainloop()