################################################
#
# Program created by Peter Nguyen and Alexis Torres
# Date: 11/30/19
# Description: This program simulates the space invaders
# game using pygame functions and modules from other files.
# Modules used: Sound.py, Mob.py
#
################################################

# libraries imported
import pygame
import random # random chance
import math # for calculating distance
from pygame import mixer # for music functions
#from Mob import player, obj
import Mob
import Sound

################################################
# initialize the pygame

pygame.init()
################################################
# width and length of game screen
width = 800
length = 600

################################################
# create the screen
screen = pygame.display.set_mode((width,length))

################################################
# Sets fps
clock = pygame.time.Clock()


################################################
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)



################################################
# background
background = Mob.obj('background.png',0,0)
Sound.background_music()

################################################
# Score
font = pygame.font.Font('freesansbold.ttf',32)
def show_score(score_value,x,y):
    score = font.render("Score :"+ str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

###############################################
# Gameover text
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = over_font.render(("GAME OVER!!"), True, (255,255,255))
    screen.blit(over_text, (200,250))
    
################################################
# player
ship = Mob.player('player.png',400,500,0,0)

################################################
# Enemy
num_of_enem = 15
enemy = []
for i in range(num_of_enem):
    enemy.append(Mob.enemy('enemy.png',random.randint(0,735),random.randint(50,150),4,40))

################################################
# bullet
projectile = Mob.bullet('bullet.png',0,500,0,20)

################################################
# GAME LOOP
def main():
    score_value = 0
    textX = 10
    textY = 10
    running = True
    while running:
        #clock.tick(240) # Time frames per second
        ########################################
        # RGB - red green blue
        screen.fill((255,255,255))
        # background image
        screen.blit(background.image,(0,0))

        ########################################
        # check for end of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ########################################
        # If keystroke is pressed
        if event.type == pygame.KEYDOWN:
            # left direction
            if event.key == pygame.K_LEFT:
                ship.X_change = -5
                
            # right direction
            if event.key == pygame.K_RIGHT:
                ship.X_change = 5

            # firing bullet
            if event.key == pygame.K_SPACE:
                # so that bullet finishes its path
                if projectile.state is 'ready':
                    Sound.laser_sound()
                    projectile.X_coord = ship.X_coord
                    projectile.fire(screen)

        # releasing key    
        if event.type == pygame.KEYUP:
            # for the ship to stop moving
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.X_change = 0

        # movement of ship
        ship.X_coord += ship.X_change

        #########################################
        # GAME OVER 
        for i in range(num_of_enem):
            if enemy[i].Y_coord > 440:
                for j in range(num_of_enem):
                    enemy[j].Y_coord = 2000
                game_over_text()
                
            if projectile.isCollision(enemy[i]):
                enemy[i].hit()
                projectile.hit()
                Sound.collision_sound()
                score_value+=1
            
            enemy[i].movement(screen)
            enemy[i].X_coord += enemy[i].X_change
        
        # Checks if ship is within the screen boundaries
        ship.boundary()
        # Updates ship position
        ship.update_obj(screen)
        # Updates projectile position
        projectile.movement(screen)
        # Shows score
        show_score(score_value,textX, textY)
        # Updates whole screen
        pygame.display.update()


################################################
# Main Function Call
main()