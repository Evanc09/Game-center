import random
import time
import tkinter as tk
import sys
import pickle
import pygame
from pygame import mixer
import time
pygame.font.init()
global elapsed_time
loadfile = open("data.dat", "rb")
loadeddata = pickle.load(loadfile)
loadfile.close()
mixer.init()
import os

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astroids")

try:
  BG=pygame.image.load(os.path.join('bg.jpeg')).convert()
except FileNotFoundError as ie:
    print("File Not found:", ie)
    sys.exit()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
lives = 3
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, stars):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"High Score:{loadeddata}", 1, "white")
    current_score = elapsed_time * 3
    current_score_text1 = f"Score: {round(current_score)} Points"
    current_score_text = FONT.render(current_score_text1, 1, "white")
    WIN.blit(current_score_text, (10, 39))
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()
lives = 3

   
def main(lives):
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                            PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        draw(player, stars)
        
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                    STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lives = lives -1
            print(lives)
            def destroy():
                root.destroy()
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            root = tk.Tk()
            label = tk.Label(root, text=f"Your lives are {lives}")
            if lives == 0:
                you_lost = tk.Label(text="You died")
                you_lost.pack()
                time.sleep(2)
                quit()
            continue_ = tk.Button(text="continue", command=lambda:[destroy(),main(lives)])
            continue_.pack()
            label.pack()
            root.mainloop()
        draw(player, stars)
################################################################################################################
class TWO_player_Free_play():
    def Free_play():
    
        info_textm = FONT.render("How To Play(Rules):", 1, "green")
        info_text1 = FONT.render("1. Use Arrow Keys To move ", 1, "green")
        info_text3 = FONT.render("3.HAVE FUN! ", 1, "green")
        info_text2 = FONT.render("2.Your Score is calculated by your time x 3 ", 1, "green")
        WIN.blit(info_textm, (WIDTH/2 - info_textm.get_width()/2, HEIGHT/5 - info_textm.get_height()/2))
        WIN.blit(info_text1, (WIDTH/2 - info_text1.get_width()/2, HEIGHT/4 - info_text1.get_height()/2))
        WIN.blit(info_text2, (WIDTH/2 - info_text2.get_width()/2, HEIGHT/3 - info_text2.get_height()/2))
        WIN.blit(info_text3, (WIDTH/2 - info_text3.get_width()/2, HEIGHT/2 - info_text3.get_height()/2))
        pygame.display.update()
        pygame.time.delay(4000)
        
        pygame.display.set_caption("Astroids(Free Play)")
       
        main_sound = pygame.mixer.Sound(os.path.join('main.mp3'))
        
        player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                            PLAYER_WIDTH, PLAYER_HEIGHT)
        
        global elapsed_time
        clock = pygame.time.Clock()
        #######################
        start_time = time.time()
        elapsed_time = 0
        #######################
        
        star_add_increment = 2000
        star_count = 0
        run = True
        stars = []
        hit = False
        
        
        zero = 0
        while run:
            zero = zero +1
            star_count += clock.tick(60)
            elapsed_time = time.time() - start_time
            current_score = elapsed_time * 3
            print(current_score)
            draw(player, stars)
            pygame.mixer.Sound.play(main_sound)
            time.sleep(0.01)
            pygame.display.update()
            if star_count > star_add_increment:
                for _ in range(3):
                    star_x = random.randint(0, WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x, -STAR_HEIGHT,
                                    STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)

                star_add_increment = max(200, star_add_increment - 50)
                star_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL
            
                
            for star in stars[:]:
                star.y += STAR_VEL
                if star.y > HEIGHT:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars.remove(star)
                    hit = True
                    
                    break
            
            if hit:
                
                global total_score
                total_score_exact = elapsed_time*3
                total_score_rounded = round(total_score_exact)
                total_score = total_score_rounded
            
                
                
                lost_text = FONT.render(f"You Lost!, Score:{total_score}", 1, "white")
                main_sound.stop()
                
                ouch = pygame.mixer.Sound(os.path.join('hit.mp3'))
                vol= 10.0
                ouch.set_volume(vol)
                def resetdata():
                    resetfile = open("data.dat", 'wb')
                    zerodata = 0
                    pickle.dump(zerodata, resetfile)
                    resetfile.close()
                def save():
                    if total_score > loadeddata:
                        savefile = open("data.dat", "wb")
                        pickle.dump(total_score, savefile)
                        savefile.close()
                    else:
                        pass
                pygame.mixer.Sound.play(ouch)
                def stop():
                    sys.exit()
                WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
                pygame.display.update()
                root = tk.Tk()
                def destroy(root):
                    root.destroy()
                b1=tk.Button(text="Play again(yes)", command=lambda: [destroy(root),save(), TWO_player_Free_play.Free_play()])
                b2=tk.Button(text="exit", command=lambda:[save(),stop()])
                b3=tk.Button(text="Play Normal Mode",command=lambda:[destroy(root), main(lives)])
                b4=tk.Button(text="reset high score to 0 and exit", command=lambda:[resetdata(), stop()])
                tk.Button.pack(b1)
                tk.Button.pack(b2)
                tk.Button.pack(b3) 
                tk.Button.pack(b4)
                root.mainloop()
                
                
                
            draw(player, stars)
          





    
