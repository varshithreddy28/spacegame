import pygame

pygame.init()

#creating window
root=pygame.display.set_mode((700,600))
#adding icon:
icon=pygame.image.load(r"C:\Users\DELL\OneDrive\Desktop\python\python\pygame\spaceship.png")
pygame.display.set_icon(icon)
#to add image:
player_image=pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\python\python\pygame\space-invaders.png')
x_cor=310
y_cor=480#height  
#to display ro draw image(blit):
def dispimage():
    root.blit(player_image,(x_cor,y_cor))


pygame.display.set_caption('game')
#to stabilize without  moving
running=True
while running:

    root.fill((0,0,0))# to add colour in background
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
#to create a window and to keep it on screen
    dispimage()
    pygame.display.update() #this is used to update our sceern/root
pygame.quit()
#quit()