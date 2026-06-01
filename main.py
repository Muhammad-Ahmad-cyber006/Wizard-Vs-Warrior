import pygame
from fighter import Fighter
pygame.init()

#create the game window
SCREEN_WIDTH=1000
SCREEN_HEIGHT=600
#Define colours
Yellow=(255,255,0)
Red=(255,0,0)
White=(255,255,255)
Green=(0,255,0)

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
    
#function to draw health
def draw_health_bar(health,x,y):
    ratio=health/100
    pygame.draw.rect(screen,Yellow,(x-2,y-2,404,34))
    pygame.draw.rect(screen,Red,(x,y,400,30))
    pygame.draw.rect(screen,Green,(x,y,400*ratio,30))

#create instances of fighters
fighter_1=Fighter(100,340)
fighter_2=Fighter(800,340)

#game loop 
run = True
while run:
    clock.tick(FPS)
    #draw bg
    draw_bg()
    
    #show health bar
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,580,20)
    
    #move fighter
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
    #fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1)
    
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