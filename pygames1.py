import pygame
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit (score_surf, score_rect)

pygame.init() #initializes the things needed from pygames (sound etc.)
screen = pygame.display.set_mode((800, 400)) #sets the world boundaries
pygame.display.set_caption('Rustyland')
clock = pygame.time.Clock() #sets the frame rate for the game
test_font = pygame.font.Font('Pixeltype.ttf',50)
game_active = True

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('Ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64,64)) #the last tuple is rgb coloring scheme
# score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('snail1.png').convert_alpha() #.convert_aplha() makes the game smoother and makes pygames run the snail faster/easier
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300)) #the difference between rectangle and surface is that surface is always grabbing the top left, while in rectangle, the 'pointer' can be changed
player_gravity = 0 
#if you run (all) the above code alone, then the computer will run it for a split second then close it quickly
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: #the code after the 'and' makes sure that you can jump if you are touching the ground
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        screen.blit(ground_surface,(0,300))
        screen.blit(sky_surface,(0,0)) #fancy way of saying you want to put one surface on another surface. Arugments it takes are the surface itself and the position 
        # pygame.draw.rect(screen, '#c0e8ec', score_rect) #include what you want to draw on, the color (the color here is # c0e8ec), and the actual rectangle
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10) #adding the extra number at the end helps make a thick boundary for the colored rectangle
        # screen.blit(score_surf, score_rect)

        display_score()

        snail_rect.x -= 4 #we are moving the sail by 4
        if snail_rect.right <= 0: #if the right side of the snail's x position is less than 0 (goes off the left side), then return the snail to the right side of the screen
            snail_rect.left = 800


        screen.blit(snail_surf, snail_rect)

        #Player
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill('Yellow')

    

    pygame.display.update() #updates line 4 (the screen)
    clock.tick(60) #sets the maximum frame rate for the game
