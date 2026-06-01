import pygame

class Fighter():
    def __init__(self,x,y):
        self.rect=pygame.Rect((x,y, 70,180))
        self.vel_y=0
        self.jump=False
        
    def move(self,screen_width,screen_height):
        SPEED=10
        GRAVITY=2
        dx=0
        dy=0
        
        #get key press
        key=pygame.key.get_pressed()
        
        #movment
        if key[pygame.K_a]:
            dx=-SPEED
        if key[pygame.K_d]:
            dx=SPEED
        #jump
        if key[pygame.K_w] and self.jump==False:
            self.vel_y=-30 
            self.jump=True
            
        #Apply garvi
        self.vel_y+=GRAVITY
            
        dy+=self.vel_y      
        
        #ensuring fighter remain on screen
        #left side ensure
        if self.rect.left + dx < 0:
             dx = 0 - self.rect.left
        #right side ensure
        if self.rect.right + dx > screen_width:
             dx = screen_width - self.rect.right
        #no double jump and not false to doom       
        if self.rect.bottom +dy > screen_height - 90:
            self.vel_y=0
            self.jump=False
            dy=screen_height- 90 - self.rect.bottom         
        #update player movement
        self.rect.x+=dx 
        self.rect.y+=dy           
        
        
        
        
    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)