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
ground = 448-48

# gravity
gravity = 4

# mario
mario_height = 32
mario_facing_right = True
mario_on_the_ground = True
mario_jumping = False
mario_jump_height = 4
mario_jump_height_max = 164
mario_jump_variable = 0
mario_speed = 4
mario = pygame.image.load("./static_images/mario.png")
mario_hitbox = mario.get_rect(topleft = (50, ground - mario_height))
mario_jump_animation = pygame.image.load("./static_images/mario_jump.png")
mario_left = pygame.image.load("./static_images/mario_left.png")

# goomba
goomba_alive = True
goomba_animation_i = 0
goomba_animation_list = []
goomba_animation_list.append(pygame.image.load("./animate_images/goomba0.png"))
goomba_animation_list.append(pygame.image.load("./animate_images/goomba1.png"))
goomba_hitbox = goomba_animation_list[0].get_rect(topleft = (700, ground - 32))
goomba_death_ani = pygame.image.load("./static_images/goomba_died.png")

# brick
brick_destroyed = False
brick = pygame.image.load("./static_images/brick.png")
brick_hitbox = brick.get_rect(topleft = (672, ground - 128))

# import fonts here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # get mario events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if mario_on_the_ground == True:
                    mario_on_the_ground = False
                    mario_jumping = True
                    mario_jump_variable = mario_jump_height_max

    # get keys held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        mario_facing_right = True
        if (mario_hitbox.x <= 500) and ((mario_hitbox.x + mario_speed) <= 500):
            mario_hitbox.x += mario_speed
        else:
            mario_hitbox.x = 500
            # universal object speed deduction
            bg_x -= mario_speed
            goomba_hitbox.x -= mario_speed
            brick_hitbox.x -= mario_speed
    if keys[pygame.K_a]:
        mario_facing_right = False
        if (mario_hitbox.x >= 0) and ((mario_hitbox.x - mario_speed) > 0):
            mario_hitbox.x -= mario_speed
        else: 
            mario_hitbox.x = 0

    # mario
    if mario_hitbox.colliderect(brick_hitbox) == True and not (mario_hitbox.y < brick_hitbox.y):
        if mario_on_the_ground == False:
            mario_hitbox.y += mario_jump_height
            mario_jumping = False
        elif mario_facing_right == True:
            mario_hitbox.x -= mario_speed
        else:
            mario_hitbox.x += mario_speed

    # mario jump
    if (mario_on_the_ground == False) and (mario_jump_variable > 0) and (mario_jumping == True):
        mario_hitbox.y -= mario_jump_height
        mario_jump_variable -= mario_jump_height
    # need to create a function to check if that is okay to be
    elif (mario_hitbox.y < (ground - mario_height)) and not (mario_hitbox.colliderect(brick_hitbox)) and mario_jumping == False:
        mario_hitbox.y += gravity
    else:
        mario_on_the_ground = True
        mario_jumping = False

    # goomba
    # goomba move
    # if goomba_alive == True:
    #     goomba_hitbox.x -= 2

    # check collsion
    if (mario_hitbox.collidepoint((goomba_hitbox.x + 4, goomba_hitbox.y - 1)) or mario_hitbox.collidepoint((goomba_hitbox.x + goomba_hitbox.width - 4, goomba_hitbox.y - 1)) or mario_hitbox.collidepoint(goomba_hitbox.x + (int(goomba_hitbox.width / 2)), goomba_hitbox.y - 1)) == True:
        goomba_alive = False
    elif (mario_hitbox.colliderect(goomba_hitbox) and goomba_alive) == True:
        print("Game over!", goomba_animation_i)
        sys.exit()

    # background
    screen.blit(bg, (bg_x, bg_y))

    # brick render
    if brick_destroyed == False:
        screen.blit(brick, brick_hitbox)

    # mario render
    if mario_on_the_ground == False:
        screen.blit(mario_jump_animation, (mario_hitbox.x - 4, mario_hitbox.y))
    elif mario_facing_right == True:
        screen.blit(mario, mario_hitbox)
    elif mario_facing_right == False:
        screen.blit(mario_left, mario_hitbox)

    # goomba animation
    goomba_animation_i += 0.1
    if goomba_animation_i >= 2:
        goomba_animation_i = 0

    # goomba render
    if goomba_alive == True:
        screen.blit(goomba_animation_list[int(goomba_animation_i)], goomba_hitbox)
    else:
        screen.blit(goomba_death_ani, (goomba_hitbox.x, (goomba_hitbox.y + int(goomba_hitbox.height / 2))))

    pygame.display.update()
    clock.tick(60) #limit our game to 60 fps no matter what