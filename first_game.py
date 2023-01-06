import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))  #sets the world boundaries
pygame.display.set_caption('space invader-like game')
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)

bullet = pygame.image.load('bullet.png')#loading in the bullet
world_background = pygame.image.load('space.png')#loading in the background
space_ship = pygame.image.load('spaceship.png')#loading in the space ship
alien = pygame.image.load('alien.png') #loading in the alien


'''WORLD'''
world_back_scaled = pygame.transform.scale(world_background, (800, 400)) #updating t he size of the background
screen.blit(world_back_scaled, (0, 0)) #adding the fixed background onto the screen

'''BULLET'''
bullet_scaled =  pygame.transform.scale(bullet, (40,35)) #updating the size of the bullet
bullet_rect = bullet_scaled.get_rect(midbottom = (90,93)) #making a rectangle around the scaled alien
 #making sure that the bullet goes whereever the ship goes
 #adding the fixed alien onto the screen

'''SPACE SHIP'''
space_ship_scaled = pygame.transform.scale(space_ship, (150,75)) #updating the size of the space ship
space_ship_rect = space_ship_scaled.get_rect(midbottom = (60,100)) #making a rectangle around the scaled space ship
screen.blit(space_ship_scaled, space_ship_rect) #adding the fixed space ship onto the screen

'''ALIEN'''
alien_scaled = pygame.transform.scale(alien, (45,50)) #updating the size of the aliens
alien_rect = alien_scaled.get_rect(midbottom = (500,300)) #making a rectangle around the scaled alien
screen.blit(alien_scaled, alien_rect) #adding the fixed alien onto the screen

"SCORE"
score = 0
score_board = font.render(f"Score: {score}",None,'Green')
score_rec = score_board.get_rect(midbottom = (300,50))
#screen.blit(score_board,score_rec)

"Game over"
Game_over = font.render("Game over",None,'Red')
Game_over_rec = Game_over.get_rect(midbottom = (400,200))
#screen.blit(Game_over,Game_over_rec)

ship_movement = 0 #ship movement 
bullet_movement = 0 #bullet speed 
alien_movement = 0 #Alien


game_ongoing = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_ongoing:
            if event.type == pygame.KEYDOWN: #if the wanted key is pressed
                if event.key == pygame.K_UP: #if the wanted key is the up arrow
                    if space_ship_rect.y >= -30:
                        space_ship_rect.y  -= 20  
                if event.key == pygame.K_DOWN: #if the wanted key is the down arrow
                    if space_ship_rect.y <= 340: 
                        space_ship_rect.y  += 20
                #space_ship_rect.y += ship_movement

                if event.key == pygame.K_SPACE:
                    if bullet_rect.x <= 800:
                        bullet_movement = 10
                        
                    if bullet_rect.x > 800:
                        bullet_rect.x = space_ship_rect.x + 87
                        bullet_rect.y = space_ship_rect.y + 25
               
                #making the alien appear from a random x-axis 
                if alien_rect.x < 0:
                    alien_rect.y = random.randint(10,350)
                    alien_rect.x = 800
                
    

    if alien_rect.collidepoint(bullet_rect.midright):
        score += 0.25
    
    if game_ongoing:
        bullet_rect.x += bullet_movement #we need this hear becasue we don't want it to depend on an event 
        screen.blit(Game_over,Game_over_rec) #game over text
        screen.blit(world_back_scaled, (0, 0)) #background
        screen.blit(bullet_scaled, bullet_rect) #bullet 
        screen.blit(space_ship_scaled, space_ship_rect) #Ship
        screen.blit(alien_scaled,alien_rect)# Alien 
        screen.blit(score_board,score_rec) #Score board
        # pygame.draw.rect(world_back_scaled ,'Red',pygame.Rect(space_ship_rect))
        # pygame.draw.rect(world_back_scaled ,'Red',pygame.Rect(alien_rect))
        # pygame.display.flip()
        score_board = font.render(f"Score: {score}",None,'Red')#updating score board

        alien_rect.x -=2 #alien speed

    #speed and alien colliding to make game over 
    if space_ship_rect.collidepoint(alien_rect.midright):
        screen.blit(Game_over,Game_over_rec)
        game_ongoing = False


    




    pygame.display.update()  #second last line of code
    clock.tick(60)  #last line of code