import pygame, sys
import pygame.midi
from pygame.locals import *

DISPLAY=pygame.display.set_mode((500, 400), 0, 32)
NOTES = [];


def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()

def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
               (i, interf, name, opened, in_out))
        

def draw_keyboard(notes):
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    for i, val in enumerate(notes):
        color = RED if val == True else BLUE
        x = 10 + i * 20
        y = (i + 1 ) % 2 * 20
        pygame.draw.rect(DISPLAY, color, (x, y, 10, 10))

def main():
    pygame.init()
    print_device_info()
    WHITE = (255, 255, 255)
    DISPLAY.fill(WHITE)

    while True:
        a_key = False
        s_key = False
        d_key = False
        f_key = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                NOTES.clear()
            if event.type == KEYDOWN and event.unicode == 'a':
                a_key = True
                NOTES.append('a')
            if event.type == KEYDOWN and event.unicode == 's':
                s_key = True
                NOTES.append('s')
            if event.type == KEYDOWN and event.unicode == 'd':
                d_key = True
                NOTES.append('d')
            if event.type == KEYDOWN and event.unicode == 'f':
                f_key = True
                NOTES.append('f')

        draw_keyboard([a_key, s_key, d_key, f_key])
        pygame.display.update()

main()
