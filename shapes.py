# a spot to hold some shapes
import pygame

def draw_line1(screen, shape):
    pygame.draw.line(screen, shape['color'], shape['start_pos'], shape['end_pos'], shape['width'])

def draw_rect1(screen, shape):
    pygame.draw.rect(screen, shape['color'], (shape['position'][0], shape['position'][1], shape['width'], shape['height']))

def draw_circle1(screen, shape):
    pygame.draw.circle(screen, shape['color'], shape['position'], shape['radius'])