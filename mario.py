import pygame
import sys

pygame.init()
# create a screen instance/object with 
# 1000px width and 448px height

screen = pygame.display.set_mode((1000, 448))

# I forgot to mention 'Clock'
# the 'clock' instance help us to control the FPS
# see below - clock.tick(60) makes the fps to be 60 
clock = pygame.time.Clock()

# import images & animation here
# Tips: The bricks (floor) is 48px height

# background
bg_x = 0
bg_y = 0
bg = pygame.image.load("./static_images/background.png")

# mario
mario_speed = 25
mario = pygame.image.load("./static_images/mario.png")
mario_hitbox = mario.get_rect(topleft = (10, 448-48-32))

# goomba
goomba_alive = True
goomba_animation_i = 0
goomba_animation_list = []
goomba_animation_list.append(pygame.image.load("./animate_images/goomba0.png"))
goomba_animation_list.append(pygame.image.load("./animate_images/goomba1.png"))
goomba_hitbox = goomba_animation_list[0].get_rect(topleft = (700, 448-48-32))
goomba_death_ani = pygame.image.load("./static_images/goomba_died.png")

# import fonts here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # get mario events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if mario_hitbox.x <= 500:
                    mario_hitbox.x += mario_speed
                else:
                    bg_x -= 2
            if event.key == pygame.K_a:
                if mario_hitbox.x >= 0 and ((mario_hitbox.x - mario_speed) > 0):
                    mario_hitbox.x -= mario_speed
                else: 
                    mario_hitbox.x = 0

    # background
    screen.blit(bg, (bg_x, bg_y))

    # mario
    # mario control
    (x, y) = pygame.mouse.get_pos()
    (mario_hitbox.x, mario_hitbox.y) = (x, y)

    # mario render
    screen.blit(mario, mario_hitbox)


    # goomba
    # goomba move
    # if goomba_alive == True:
    #     goomba_hitbox.x -= 2

    # goomba animation
    goomba_animation_i += 0.1
    if goomba_animation_i >= 2:
        goomba_animation_i = 0

    # goomba render
    if goomba_alive == True:
        screen.blit(goomba_animation_list[int(goomba_animation_i)], goomba_hitbox)
    else:
        screen.blit(goomba_death_ani, (goomba_hitbox.x, (goomba_hitbox.y + int(goomba_hitbox.height / 2))))

    # check collsion
    if (mario_hitbox.collidepoint((goomba_hitbox.x + 4, goomba_hitbox.y - 1)) or mario_hitbox.collidepoint((goomba_hitbox.x + goomba_hitbox.width - 4, goomba_hitbox.y - 1)) or mario_hitbox.collidepoint(goomba_hitbox.x + (int(goomba_hitbox.width / 2)), goomba_hitbox.y - 1)) == True:
        goomba_alive = False
    elif (mario_hitbox.colliderect(goomba_hitbox) and goomba_alive) == True:
        print("Game over!", goomba_animation_i)
        sys.exit()

    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what