################################################
#
# Program created by Peter Nguyen and Alexis Torres
# Date: 11/30/19
# Description: This program uses the mixer feature
# in the pygame libraries to give us sound functions
# that we can implement into our game
#
################################################
# Libraries imported
import pygame
from pygame import mixer # for music functions

###############################################
# Background music
def background_music():
    mixer.music.load('background.wav')
    mixer.music.play(-1) #-1 makes it play on loop


###############################################
# Collision sound effect

def collision_sound():
    explosion_sound = mixer.Sound('explosion.wav')
    explosion_sound.play()

###############################################
# Laser sound effect
def laser_sound():
    bullet_sound = mixer.Sound('laser.wav')
    bullet_sound.play()