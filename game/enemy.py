import pygame
import random
import threading

pygame.init()

#creating window
root=pygame.display.set_mode((800,600))
#adding icon:
icon=pygame.image.load(r"C:\Users\DELL\OneDrive\Desktop\python\python\pygame\spaceship.png")
pygame.display.set_icon(icon)
#adding background image:
back=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\python\python\pygame\back.jpg')

#to add player image:
player_image=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\python\python\pygame\space-invaders.png')
player_x=310
player_y=480#height
x_change=0
y_change=0

#to add enemy image:
enemy_image=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\python\python\pygame\monster.png')
enemy_x=random.randint(0,800)
enemy_y=random.randint(50,200)#height
enemyx_change=4
enemyy_change=40

#to add bullet:
bullet_image=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\python\python\pygame\monster.png')
bullet_x=0
bullet_y=480#height
bulletx_change=4
bullety_change=10
bullet_state='ready' #menas it is ready to shoot,fire means it is in movement



#to display ro draw image(blit):
def dispimage(x,y):
    root.blit(player_image,(player_x,player_y))

def dispenemyimage(x,y):
    root.blit(enemy_image,(enemy_x,enemy_y))

def dispbullet(x,y):
    global bullet_state
    bullet_state='fired'#in while loop if we call the function then the stste is changed
    root.blit(bullet_image,(x+16,y+10))


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
#to create a window and to keep it on screen
    player_x+=x_change #to change in x cordinate
    if player_x>=736: 
        player_x=736
    elif player_x<=0:
        player_x=0
    #to enemy movement:

    enemy_x+=enemyx_change
    if enemy_x>=736: 
        enemyx_change-=1
        enemy_y=enemy_y+1
    elif enemy_x<=0:
        enemyx_change+=1
        enemy_y=enemy_y+1
    #reenter of bullet
    if bullet_y<=0:
        bullet_y=480
        bullet_state='ready'
    #bullet movement
    if bullet_state is'fired': 
                dispbullet(bullet_x,bullet_y)          
                bullet_y-=bullety_change

    dispimage(player_x,player_y)
    dispenemyimage(enemy_x,enemy_y)
    pygame.display.update() #this is used to update our sceern/root
pygame.quit()
#quit()