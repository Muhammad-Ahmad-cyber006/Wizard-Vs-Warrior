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
#define game var

intro_count=0
last_count_update=pygame.time.get_ticks()
score=[0,0]# player sorces [player1 and player2]
round_over =False
ROUND_OVER_COOL_DOWN=2000 #2sec


#define fighter var
WARRIOR_SIZE=162
WARRIOR_SCALE=4
WARRIOR_OFFSET=[72,56]
WARRIOR_DATA=[WARRIOR_SIZE,WARRIOR_SCALE,WARRIOR_OFFSET]
WIZARD_SIZE=250
WIZARD_SCALE=3
WIZARD_OFFSET=[112,107]
WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Wizard Vs Warrior")

#set framerate
clock=pygame.time.Clock()
FPS=60

#load bg
bg_iamge=pygame.image.load("images/background/background.jpg").convert_alpha()
#load spriteSheets
warrior_sheet=pygame.image.load("images/warrior/warrior.png").convert_alpha()
wizard_sheet=pygame.image.load("images/wizard/wizard.png").convert_alpha()
#loading victory img
victory_img=pygame.image.load("victory.png")


#number of steps in each animation
WARRIOR_ANIMATION=[10,8,1,7,7,3,7]
WIZARD_ANIMATION=[8,8,1,8,8,3,7]
#loading font
count_fount=pygame.font.Font("Turok.ttf",80)
score_font=pygame.font.Font("Reign Beats.otf",30)

#function for darwing text
def draw_text(text,font,text_colour,x,y):
    img=font.render(text,True,text_colour)
    screen.blit(img,(x,y))

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
fighter_1=Fighter(1,100,340,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION)
fighter_2=Fighter(2,800,340,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION)

#game loop 
run = True
while run:
    clock.tick(FPS)
    #draw bg
    draw_bg()
    draw_text("P1: "+str(score[0]),score_font,White,20,60)
    draw_text("P2: "+str(score[1]),score_font,White,580,60)
    
    #show health bar
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,580,20)
    #update intro count
    if intro_count<=0:
    
        #move fighter
        fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2,round_over)
        fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1,round_over)
    else:
        #display timer
        draw_text(str(intro_count),count_fount,Red,SCREEN_WIDTH/2,SCREEN_HEIGHT/3)
        if pygame.time.get_ticks()-last_count_update>=1000:
            intro_count-=1
            last_count_update=pygame.time.get_ticks()
            
            
    #update fighter
    fighter_1.update()
    fighter_2.update()   
    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    #check for player defeat
    if round_over==False:
        if fighter_1.alive==False:
            score[1]+=1 #player 2 scores
            round_over=True
            round_over_time=pygame.time.get_ticks()
            #print(score)
        elif fighter_2.alive==False:
            score[0]+=1 #player 1 scores
            round_over=True
            round_over_time=pygame.time.get_ticks() 
    else:
        #display victory img
        screen.blit(victory_img,(360,150))
        if pygame.time.get_ticks() -round_over_time>ROUND_OVER_COOL_DOWN:
            round_over=False
            intro_count=3
            fighter_1=Fighter(1,100,340,False,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION)
            fighter_2=Fighter(2,800,340,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION)
               
    
    
    #event handler
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False


#update dispaly
    pygame.display.update()            


pygame.quit()            