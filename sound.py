"""This file contains functions to play sound."""


import pygame


def jump_sound():
    """This function will play a sound."""
    jump = pygame.mixer.Sound("assets/audio/zapsplat_cartoon_pop_mouth_mid_pitch_003_86613.mp3")
    pygame.mixer.Sound.play(jump)
