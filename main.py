import pygame
from fighter import Fighter
pygame.init()

#create the game window
SCREEN_WIDTH=1000
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Wizard Vs Warrior")

#set framerate
clock=pygame.time.Clock()
FPS=60

#load bg
bg_iamge=pygame.image.load("images/background/background.jpg").convert_alpha()
#function for background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_iamge,(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#create instances of fighters
fighter_1=Fighter(100,340)
fighter_2=Fighter(800,340)

#game loop 
run = True
while run:
    clock.tick(FPS)
    #draw bg
    draw_bg()
    #move fighter
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    
    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    
    
    #event handler
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False


#update dispaly
    pygame.display.update()            


pygame.quit()            