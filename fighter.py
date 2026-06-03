import pygame

class Fighter():
    def __init__(self,player,x,y,flip,data,sprite_sheets,animation_steps):
        self.player=player
        self.size=data[0]
        self.image_scale=data[1]
        self.offset=data[2]
        self.flip=flip
        self.animation_list=self.load_iamges(sprite_sheets,animation_steps)
        self.action=0#0=idle,1=run,2=jump,3=attack1,4=attack2,5=HIT6=DEATH
        self.frame_index=0
        self.image=self.animation_list[self.action][self.frame_index]
        self.rect=pygame.Rect((x,y, 70,180))
        self.update_time=pygame.time.get_ticks()
        self.vel_y=0
        self.running=False
        self.jump=False
        self.attacking=False
        self.attack_type=0
        self.attack_cool_down=0
        self.hit=False
        self.health=10
        self.alive=True
    
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
        self.running=False
        self.attack_type=0
        
        #get key press
        key=pygame.key.get_pressed()
        #can only perfrom other stuff if not attacking
        if self.attacking==False and self.alive==True:
            #check player 1 controls
            if self.player==1:
            #movment
                if key[pygame.K_a]:
                    dx=-SPEED
                    self.running=True
                if key[pygame.K_d]:
                    dx=SPEED
                    self.running=True
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

            #check player 2 controls
            if self.player==2:
            #movment
                if key[pygame.K_RIGHT]:
                    dx=SPEED
                    self.running=True
                if key[pygame.K_LEFT]:
                    dx=-SPEED
                    self.running=True
                #jump
                if key[pygame.K_UP] and self.jump==False:
                    self.vel_y=-30 
                    self.jump=True
                #attacking keys    
                if key[pygame.K_m] or key[pygame.K_n]:
                    self.attack(surface,target)
                    
                    #determin the type of attack
                    if key[pygame.K_m]:
                        self.attack_type=1
                    if key[pygame.K_n]:
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
        #attack cool down
        if self.attack_cool_down>0:
            self.attack_cool_down-=1
        
        #update player movement
        self.rect.x+=dx 
        self.rect.y+=dy
               
    
    def update(self):
        #check which action is being done
        if self.health<=0:
            self.health=0
            self.alive=False
            self.update_action(6)
        elif self.hit==True:
            self.update_action(5)
        elif self.attacking==True:
            if self.attack_type==1:
                self.update_action(3)
            elif self.attack_type==2:
                self.update_action(4) 
                   
        elif self.jump==True:
            self.update_action(2)   
             
        elif self.running==True:
            self.update_action(1)
            
        else:
            self.update_action(0)
        
        
        animation_cooldown=45
        #update iamge
        self.image=self.animation_list[self.action][self.frame_index]
        #check if enough time is passed 
        if pygame.time.get_ticks() - self.update_time >animation_cooldown:
            self.frame_index+=1
            self.update_time=pygame.time.get_ticks()
        #check if animation is finished
        if self.frame_index>=len(self.animation_list[self.action])-1:
            #if player is dead
            if self.alive==False:
                self.frame_index=len(self.animation_list[self.action])-1
            else:
                self.frame_index=0
                if self.action==3 or self.action==4:
                    self.attacking=False
                    self.attack_cool_down=20
                #damage is taken
                if self.action==5:
                    self.hit=False
                    #if middle of attack then attack is stop
                    self.attacking=False
                    self.attack_cool_down=20
                

    def attack(self,surface,traget):
        if self.attack_cool_down==0:
        
            self.attacking=True
        
            attacking_rect=pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip),self.rect.y,2*self.rect.width,self.rect.height)  
            if attacking_rect.colliderect(traget.rect):
                
                traget.health-=10;
                traget.hit=True
                pygame.draw.rect(surface,(0,255,0),attacking_rect)      
        
        
    def draw(self, surface):
        img=pygame.transform.flip(self.image,self.flip,False)
        pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))
    
    def update_action(self,new_action):
        #check if new action is differ from perivous or current one
        if new_action!=self.action:
            self.action=new_action
            #update animation settings
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()