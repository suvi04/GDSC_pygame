import pygame
from pygame.locals import *
from pygame import mixer
import sys
import random

WIDTH, HEIGHT = 1366,768
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Rangers")
WHITE=(255,255,255)
FPS = 60
pygame.init()
PLAYER_IMAGE = pygame.image.load("youonlygetone/gfx/player.png").convert_alpha()
PLAYER_IMAGE = pygame.transform.rotozoom(PLAYER_IMAGE,0,0.25)
ENEMY_IMAGE = pygame.image.load("youonlygetone/gfx/enemy.png").convert_alpha()
ENEMY_IMAGE = pygame.transform.rotozoom(ENEMY_IMAGE,0,0.15)
START_BG = pygame.image.load("youonlygetone/gfx/strt.png").convert_alpha()
START_BG = pygame.transform.rotozoom(START_BG,0,0.9)
GAME_BG = pygame.image.load("youonlygetone/gfx/bg.png").convert_alpha() 
GAME_BG = pygame.transform.rotozoom(GAME_BG,0,1.48)
PLAYER_GUN_IMAGE = pygame.image.load("youonlygetone/gfx/player_gun.png").convert_alpha()
PLAYER_GUN_IMAGE = pygame.transform.rotozoom(PLAYER_GUN_IMAGE,0,0.025)
END_BG = pygame.image.load("youonlygetone/gfx/end.png").convert_alpha()
END_BG=pygame.transform.rotozoom(END_BG,0,1.6)

score=0
game_active=0

# / to-do
#MAKE SCORE A BIT NON LINEAR
#gun sound
#replay shii
#enemy gun??
#enemy speedup


PLAYER_RECT=PLAYER_IMAGE.get_rect(center=(50,HEIGHT/2))
ENEMY_RECT=ENEMY_IMAGE.get_rect(center=(random.randint(700,1300),random.randint(100,700)))
PLAYER_GUN_RECT = PLAYER_GUN_IMAGE.get_rect(center=(1600,1600))


enemyMatrix=[ENEMY_RECT]
enemyMatrix.append(ENEMY_RECT)
ENEMY_RECT=ENEMY_IMAGE.get_rect(center=(random.randint(700,1300),random.randint(100,700)))
enemyMatrix.append(ENEMY_RECT)
ENEMY_RECT=ENEMY_IMAGE.get_rect(center=(random.randint(700,1300),random.randint(100,700)))
enemyMatrix.append(ENEMY_RECT)
e1=[]
for i in range(len(enemyMatrix)):
    e1.append(enemyMatrix[i])




a=2
new=0

START_FONT = pygame.font.Font("youonlygetone/gfx/font.otf",30)
HEAD_FONT = pygame.font.Font("youonlygetone/gfx/font.otf",80)
SCORE_FONT = pygame.font.Font(None,30)


def end_game_pop():
    screen.blit(END_BG,(0,0))
    screen.blit(START_FONT.render("The enemies were faar too many ",True,"white"),(1000,300))
    screen.blit(START_FONT.render("You couldnt save us all",True,"white"),(1000,350))
    screen.blit(HEAD_FONT.render("You loose ",True,"white"),(WIDTH/2-200,HEIGHT/2-300))
    pygame.display.update()

def end_game_crash():
    screen.blit(END_BG,(0,0))
    screen.blit(START_FONT.render("Your spaceship was destroyed ",True,"white"),(1000,300))
    screen.blit(START_FONT.render("You couldnt save us all",True,"white"),(1000,350))
    screen.blit(HEAD_FONT.render("You loose ",True,"white"),(WIDTH/2-200,HEIGHT/2-300))
    pygame.display.update()




def start_screen():
    
    screen.blit(START_BG,(0,0))
    screen.blit(START_FONT.render("You only Get One ",True,"white"),(1000,300))
    screen.blit(START_FONT.render("Give Your life for it!",True,"white"),(1000,350))
    screen.blit(HEAD_FONT.render("Space Rangers ~ ",True,"white"),(WIDTH/2-200,HEIGHT/2-300))
    pygame.display.update()



def game():
    global score
    global a
    global new
    global game_active
    global enemyMatrix

    new+=0.001
    ENEMY_RECT=ENEMY_IMAGE.get_rect(center=(random.randint(700,1300),random.randint(100,700)))
    screen.blit(GAME_BG,(0,0))
    screen.blit(PLAYER_IMAGE,PLAYER_RECT)
    screen.blit(SCORE_FONT.render(f'SCORE: {int(score)}',True,"White"),(WIDTH-300,70))
    global PLAYER_GUN_RECT
    screen.blit(PLAYER_GUN_IMAGE,PLAYER_GUN_RECT)
    
    

    for i in range(len(enemyMatrix)):
        screen.blit(ENEMY_IMAGE,enemyMatrix[i])

    if(new>=1):
        enemyMatrix.append(ENEMY_RECT)
        new=0
    print(enemyMatrix)
    for i in range(len(enemyMatrix)):
        enemyMatrix[i].y+=2
        enemyMatrix[i].x-=0.5
        if enemyMatrix[i].y>=WIDTH-400:
            enemyMatrix[i].y=random.randint(0,150)
        if(PLAYER_GUN_RECT.colliderect(enemyMatrix[i])):
            enemyMatrix[i].x=1600
            enemyMatrix.pop(i)
            score+=10
            PLAYER_GUN_RECT.x=1600
            for i in range(random.randint(1,a)):
                enemyMatrix.append(ENEMY_RECT)
        
        if PLAYER_RECT.colliderect(enemyMatrix[i]):
            game_active=3
            PLAYER_RECT.x=100
            score=0
            
            
                
    
    if(len(enemyMatrix)>25):
        game_active=2
        PLAYER_RECT.x=100
        score=0
        a=2
    else:
        if score>=30:
            a=3
        if score>=100:
            a=4
        if score>=150:
            a=5


    
    # if len(enemyMatrix)>30:
    #     game_active=2
    #     PLAYER_RECT.x=100
        


    # -- PLAYER MOVEMENT --

    keys=pygame.key.get_pressed()
    if(PLAYER_RECT.y>10):
        if keys[pygame.K_UP]:
            PLAYER_RECT.y-=6
    if(PLAYER_RECT.y<HEIGHT-100):
        if keys[pygame.K_DOWN]:
            PLAYER_RECT.y+=6
    if(PLAYER_RECT.x>10):
        if keys[pygame.K_LEFT]:
            PLAYER_RECT.x-=6
    if(PLAYER_RECT.x<WIDTH-80):
        if keys[pygame.K_RIGHT]:
            PLAYER_RECT.x+=6


    # -- GUN
    if PLAYER_GUN_RECT.x>WIDTH:
        if keys[pygame.K_LSHIFT]:
            PLAYER_GUN_RECT=PLAYER_GUN_IMAGE.get_rect(center=(PLAYER_RECT.x+80,PLAYER_RECT.y+48))
    PLAYER_GUN_RECT.x+=9
    

    pygame.display.update()

    



def main():
    clock = pygame.time.Clock()
    run=True
    global game_active
    global enemyMatrix
    global e1
    keys=pygame.key.get_pressed()
    mixer.init()
    mixer.music.load('youonlygetone/gfx/bgm.mp3')
    #mixer.music.play(10,0,100)
    PLAYER_GUN_RECT = PLAYER_GUN_IMAGE.get_rect(center=(-600,-600))

    while run:
        clock.tick(FPS)
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                run=False
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_SPACE:
                    game_active=True

        
        if game_active==2:
            end_game_pop()
            del enemyMatrix[4:]
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_SPACE:
                    game_active=1
                    

        if game_active==3:
            end_game_crash()
            
            
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_SPACE:
                    game_active=1  
                    


        if game_active==1:
            game()
            
            


        if game_active==0:
            start_screen()
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_SPACE:
                    game_active=1
                    

    pygame.quit()

if __name__== "__main__":
    main()