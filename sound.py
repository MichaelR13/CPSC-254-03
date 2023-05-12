"""This file contains functions to play sound."""


import pygame


def jump_sound():
    """This function will play a sound."""
    jump = pygame.mixer.Sound(
        "assets/audio/zapsplat_cartoon_pop_mouth_mid_pitch_003_86613.mp3")
    pygame.mixer.Sound.play(jump)


def game_over_sound():
    """This function will play a game over sound."""
    game_over = pygame.mixer.Sound(
        "assets/audio/esm_8_bit_game_over_1_arcade_80s_simple_alert_notification_game.mp3")
    pygame.mixer.Sound.play(game_over)
