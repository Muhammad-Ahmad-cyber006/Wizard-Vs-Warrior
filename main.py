import pygame
pygame.init()

#create the game window
SCREEN_WIDTH=1000
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Wizard Vs Warrior")

#load bg
bg_iamge=pygame.image.load("images/background/background.jpg").convert_alpha()
#function for background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_iamge,(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))



#game loop 
run = True
while run:
    #draw bg
    draw_bg()
    
    
    
    #event handler
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False


#update dispaly
    pygame.display.update()            


pygame.quit()            