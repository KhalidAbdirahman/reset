import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))  #sets the world boundaries
pygame.display.set_caption('space invader-like game')
clock = pygame.time.Clock()

bullet = pygame.image.load('bullet.png')#loading in the bullet
world_background = pygame.image.load('space.png') #loading in the background
space_ship = pygame.image.load('spaceship.png')#loading in the space ship
alien = pygame.image.load('alien.png')#loading in the alien

ship_movement = 0 


game_ongoing = True

while True:
    #leave comments
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if game_ongoing:
            if event.type == pygame.KEYDOWN: #if the wanted key is pressed
                if event.key == pygame.K_UP: #if the wanted key is the up arrow
                    if space_ship_rect.y >= -30:
                        ship_movement -= 20     
                    
                if event.key == pygame.K_DOWN: #if the wanted key is the down arrow
                    if space_ship_rect.y <= 340: 
                        ship_movement += 20
                
                


    if game_ongoing:
        '''WORLD'''
        world_back_scaled = pygame.transform.scale(world_background, (800, 400)) #updating the size of the background
        screen.blit(world_back_scaled, (0, 0)) #adding the fixed background onto the screen

        '''BULLET'''
        bullet_scaled =  pygame.transform.scale(bullet, (65,70)) #updating the size of the bullet
        bullet_rect = bullet_scaled.get_rect(midbottom = (90,93)) #making a rectangle around the scaled alien
        bullet_rect.y += ship_movement #making sure that the bullet goes whereever the ship goes
        screen.blit(bullet_scaled, bullet_rect) #adding the fixed alien onto the screen

        '''SPACE SHIP'''
        space_ship_scaled = pygame.transform.scale(space_ship, (200,100)) #updating the size of the space ship
        space_ship_rect = space_ship_scaled.get_rect(midbottom = (50,100)) #making a rectangle around the scaled space ship
        space_ship_rect.y += ship_movement
        screen.blit(space_ship_scaled, space_ship_rect) #adding the fixed space ship onto the screen
        
        '''ALIEN'''
        alien_scaled = pygame.transform.scale(alien, (65,70)) #updating the size of the aliens
        alien_rect = alien_scaled.get_rect(midbottom = (810,80)) #making a rectangle around the scaled alien
        screen.blit(alien_scaled, alien_rect) #adding the fixed alien onto the screen

        if alien_rect.x < 0:
            alien_rect.y = random.randint(10,350)
            alien_rect.x = 800
            alien_rect.x -= 2
        
    

    pygame.display.update()  #second last line of code
    clock.tick(60)  #last line of code