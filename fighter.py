import pygame

class Fighter():
    def __init__(self,x,y,flip,data,sprite_sheets,animation_steps):
        self.size=data[0]
        self.image_scale=data[1]
        self.offset=data[2]
        self.flip=flip
        self.animation_list=self.load_iamges(sprite_sheets,animation_steps)
        self.action=0#0=idle,1=run,2=jump,3=attack1,4=attack2,5=HIT6=DEATH
        self.frame_index=0
        self.image=self.animation_list[self.action][self.frame_index]
        self.rect=pygame.Rect((x,y, 70,180))
        self.vel_y=0
        self.jump=False
        self.attacking=False
        self.attack_type=0
        self.health=100
    
    def load_iamges(self,sprite_sheet,animation_steps):
        #extract iamges
        animation_list=[]
        for y, animation in enumerate(animation_steps):
            temp_img_list=[]
            for x in range(animation):
                temp_img=sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.image_scale,self.size*self.image_scale))) 
            animation_list.append(temp_img_list)
        return animation_list
        
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
        img=pygame.transform.flip(self.image,self.flip,False)
        pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))