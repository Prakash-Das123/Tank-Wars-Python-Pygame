import pygame
import time
import random
import math
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("TANK STARS BY DODO")
#background
background=pygame.image.load("C:/Users/Bidyut/Desktop/TANK WARS/bg.png")

#background sound
pygame.mixer.music.load("C:/Users/Bidyut/Desktop/TANK WARS/music.mp3")
pygame.mixer.music.play(-1)

#player
playerImg=pygame.image.load("C:/Users/Bidyut/Desktop/TANK WARS/tank.png")
playerX= 370
playerY= 480
playerX_change =0

#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change =[]
enemyY_change =[]
num_of_enemies = 3                                       #no if enimes
                                                                
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("C:/Users/Bidyut/Desktop/TANK WARS/taxi.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(0)
    enemyX_change.append(0)
    enemyY_change.append(1)
                                                            #enemy speed
#bullet
#ready- you cant see the bullet on screen
#fire -bullet is currently moving
bulletImg=pygame.image.load("C:/Users/Bidyut/Desktop/TANK WARS/bullet.png") 
bulletX= 0
bulletY= 480
bulletX_change =0
bulletY_change = 20
bullet_state="ready"

#score 
score_value=0
font = pygame.font.Font("freesansbold.ttf",32)
#game over text
over_font =pygame.font.Font('freesansbold.ttf',64)

def show_score():
    score =font.render("SCORE:"+str(score_value),True,(0,255,0))
    score.blit(score,(50,50))

def game_over_text():
    over_text =over_font.render('GAME OVER!',True,(255,0,0))
    screen.blit(over_text,(200,250))
    score =font.render("SCORE: " + str(score_value),True,(0,255,0))
    score.blit(score,(50,50))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance <30:
        return True
    else:
        return False

running = True

while running:

    screen.fill((0, 255, 0))
    #background image
    screen.blit(background,(0,0))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change =-5
            if event.key == pygame.K_RIGHT:
                playerX_change =5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound=mixer.Sound("C:/Users/Bidyut/Desktop/TANK WARS/gun.wav")
                    bullet_sound.play()
                    #gets the current x coordinate of tank
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    
    if playerX <=0:
        playerX=0
    elif playerX >=736:
        playerX=736

    #bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state ="ready"
        
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    for i in range(num_of_enemies):

        #game over
        if enemyY[i] >400:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
                
        enemyY[i] += enemyY_change[i]

        if enemyY[i] >=536:
            enemyY[i]=536

        #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_sound=mixer.Sound('C:/Users/Bidyut/Desktop/TANK WARS/explosion.wav')
            collision_sound.play()
            score_value+=1
            print(score_value)
            bulletY =480
            bullet_state ="ready"
            enemyX[i]= random.randint(0, 736)
            enemyY[i]= 0
        enemy(enemyX[i],enemyY[i],i)
    show_score()
    player(playerX,playerY)
    
    pygame.display.update()


pygame.display.quit()
pygame.quit()
quit()