################################################
#
# Program created by Peter Nguyen and Alexis Torres
# Date: 12/1/19
# Description: This program contains the classes
# and subclasses for the space invaders game.
# It contains every function our objects will need
# to perform their task
#
################################################

################################################
# Libraries used
import pygame
import random
import math

################################################
# Object parent class: Main class for all mobs
# in the game. It contains the screen update functions
class obj(object):
    def __init__(self, name, X_coord, Y_coord):
        self.image = pygame.image.load(name)
        self.X_coord = X_coord
        self.Y_coord = Y_coord
        # To obtain our image length and widths just in case
        self.width, self.length = self.image.get_size()

    # Update Screen Function
    def update_obj(self, screen):
        screen.blit(self.image,(self.X_coord,self.Y_coord))

        
################################################
# Player child class

class player(obj):
    def __init__(self, name, X_coord, Y_coord, X_change, Y_change):
        super().__init__(name, X_coord, Y_coord)
        self.X_change = X_change
        self.Y_change = Y_change

    # Checks boundary of the player ship
    def boundary(self):
        if self.X_coord <= 0:
            self.X_coord = 0
        elif self.X_coord >= 736:
            self.X_coord = 736

################################################
# Bullet child class
class bullet(obj):
    def __init__(self, name, X_coord, Y_coord, X_change, Y_change):
        super().__init__(name, X_coord, Y_coord)
        self.X_change = X_change
        self.Y_change = Y_change
        self.state = 'ready'

    # Fire function
    def fire(self, screen):
        self.state = 'fire'
        screen.blit(self.image,(self.X_coord+16, self.Y_coord+10))

    # For Bullet movement
    # If bullet reaches end of screen, it resets bullet attributes
    def movement(self, screen):
        if self.Y_coord <= 0:
            self.Y_coord = 480
            self.state = 'ready'
        if self.state is 'fire':
            self.fire(screen)
            self.Y_coord -= self.Y_change

    # Collision function to check if bullet collides with enemey
    def isCollision(self, enemy):
        distance = math.sqrt((math.pow(enemy.X_coord - self.X_coord, 2)) + (math.pow(enemy.Y_coord - self.Y_coord, 2)))
        if distance < 27:
            return True
        else:
            return False

    # When collision occurs, this function resets our bullet attributes
    def hit(self):
        self.Y_coord = 480
        self.state = 'ready'

        
################################################
# Enemy child class
class enemy(obj):
    def __init__(self, name, X_coord, Y_coord, X_change, Y_change):
        super().__init__( name, X_coord, Y_coord)
        self.X_change = X_change
        self.Y_change = Y_change

    # Enemy movement function
    # if enemy reaches edge of screen then it moves downwards towards the player
    def movement(self, screen):
        if self.X_coord <= 0:
            self.X_change = 4
            self.Y_coord += self.Y_change
        elif self.X_coord >= 735:
            self.X_change = - 4
            self.Y_coord += self.Y_change
        self.update_obj(screen)

    # When collision occurs, this function resets our current enemy attributes
    def hit(self):
        self.X_coord = random.randint(0,735)
        self.Y_coord = random.randint(50,150)