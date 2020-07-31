import pygame
import random
import threading
import math


pygame.init()

#creating window
root=pygame.display.set_mode((800,600))
#adding icon:
icon=pygame.image.load(r"C:\Users\DELL\github\spacegame\game\spaceship.png")
pygame.display.set_icon(icon)
#adding background image:
back=pygame.image.load(r'C:\Users\DELL\github\spacegame\game\back.jpg')

#to add player image:
player_image=pygame.image.load(r'C:\Users\DELL\github\spacegame\game\space-invaders.png')
player_x=310
player_y=480#height
x_change=0
y_change=0

#MULTIPLE ENEMYS:
enemy_image=[]
enemy_x=[]
enemy_y=[]
enemyx_change=[]
enemyy_change=[]
noofenemys=6#no.of enemys
#to add enemy image:
y=450
for i in range(noofenemys):
    y-=50
    enemy_image.append(pygame.image.load(r'C:\Users\DELL\github\spacegame\game\monster.png'))
    enemy_x.append(random.randint(0,730))
    enemy_y.append(random.randint(20,y))#height
    enemyx_change.append(4)
    enemyy_change.append(40)

#to add bullet:
bullet_image=pygame.image.load(r'C:\Users\DELL\github\spacegame\game\bullet.png')
bullet_x=0
bullet_y=480#height
bulletx_change=4
bullety_change=10
bullet_state='ready' #menas it is ready to shoot,fire means it is in movement

#score:
score_val=0
font=pygame.font.Font('freesansbold.ttf',32) #which shows the font
score_x=10
score_y=10
#game over which shows the font:
over=pygame.font.Font('freesansbold.ttf',64)
over1=pygame.font.Font('freesansbold.ttf',50) 


def scoredisp(x,y):
    score=font.render('Score : '+str(score_val),True,(255,0,0))
    root.blit(score,(x,y))

def gameover(score_val):
    game=over.render('GAME OVER !',True,(255,0,0))
    root.blit(game,(200,250))
    score=over1.render('Score : '+str(score_val),True,(255,0,0))
    root.blit(score,(200,310))


#to display ro draw image(blit):
def dispimage(x,y):
    root.blit(player_image,(player_x,player_y))

def dispenemyimage(x,y,i):
        root.blit(enemy_image[i],(enemy_x[i],enemy_y[i]))

def dispbullet(x,y):
    global bullet_state
    bullet_state='fired'#in while loop if we call the function then the stste is changed
    root.blit(bullet_image,(x+16,y+10))
def collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=math.sqrt(pow((enemy_x-bullet_x),2)+(pow((enemy_y-bullet_y),2)))
    if distance<27:
        return True
    else :
        return False


pygame.display.set_caption('game')
#pygame.display.set_backround(back,(0,0))
#to stabilize without  moving
running=True
while running:

    root.fill((0,0,0))# to add colour in background
    #adding background
    root.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #key movements:
        if event.type==pygame.KEYDOWN:#if key is pressed
            #for  spaceship movement
            if event.key==pygame.K_LEFT:
                x_change-=3
            if event.key==pygame.K_RIGHT:
                x_change+=3
                #for bullet
            if event.key==pygame.K_SPACE:
                if bullet_state=='ready':
                    bullet_x=player_x
                    dispbullet(bullet_x,bullet_y)#state is changed
        if event.type==pygame.KEYUP: #key is relesed
            if event.key==pygame.K_LEFT:
                x_change=0
            if event.key==pygame.K_RIGHT:
                x_change=0
    player_x+=x_change #to change in x cordinate
    if player_x>=736: 
        player_x=736
    elif player_x<=0:
        player_x=0
    #to enemy movement:
    for i in range(noofenemys):

        if enemy_y[i]>300:
            for j in range(noofenemys):
                enemy_y[j]=2000
                gameover(score_val)

            break
        enemy_x[i]+=enemyx_change[i]
        if enemy_x[i]>=736: 
            enemyx_change[i]-=1
            enemy_y[i]=enemy_y[i]+1
        elif enemy_x[i]<=0:
            enemyx_change[i]+=1
            enemy_y[i]=enemy_y[i]+1
            #collision
        colide=collision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
        if colide:
            bullet_y=480
            bullet_state='ready'
            score_val+=1
            enemy_x[i]=random.randint(0,730)#for enemy respaw of enenmy
            enemy_y[i]=random.randint(50,200)
        dispenemyimage(enemy_x[i],enemy_y[i],i)
    #reenter of bullet
    if bullet_y<=0:
        bullet_y=480
        bullet_state='ready'
    #bullet movement
    if bullet_state is'fired': 
                dispbullet(bullet_x,bullet_y)          
                bullet_y-=bullety_change
    #score calculation if bullet hits
    dispimage(player_x,player_y)
    scoredisp(score_x,score_y)
    pygame.display.update() #this is used to update our sceern/root
pygame.quit()
#quit()