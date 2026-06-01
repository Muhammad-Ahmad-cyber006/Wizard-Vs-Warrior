import pygame

class Fighter():
    def __init__(self,x,y):
        self.flip=False
        self.rect=pygame.Rect((x,y, 70,180))
        self.vel_y=0
        self.jump=False
        self.attacking=False
        self.attack_type=0
        self.health=100
        
    def move(self,screen_width,screen_height,surface,target):
        SPEED=10
        GRAVITY=2
        dx=0
        dy=0
        
        #get key press
        key=pygame.key.get_pressed()
        #can only perfrom other stuff if not attacking
        if self.attacking==False:
            #movment
            if key[pygame.K_a]:
                dx=-SPEED
            if key[pygame.K_d]:
                dx=SPEED
            #jump
            if key[pygame.K_w] and self.jump==False:
                self.vel_y=-30 
                self.jump=True
            #attacking keys    
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface,target)
                
                #determin the type of attack
                if key[pygame.K_r]:
                    self.attack_type=1
                if key[pygame.K_t]:
                    self.attack_type=2
            
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
        #esure player faces each other
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True
        
        #update player movement
        self.rect.x+=dx 
        self.rect.y+=dy           
        

    def attack(self,surface,traget):
        self.attacking=True
        
        attacking_rect=pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip),self.rect.y,2*self.rect.width,self.rect.height)  
        if attacking_rect.colliderect(traget.rect):
            traget.health-=10;
            
            
        pygame.draw.rect(surface,(0,255,0),attacking_rect)      
        
        
    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)