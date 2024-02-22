import os
import pygame

def get_asset(name, *folders):
    return os.path.join('assets', *folders, name)

def unpack_animation(img):
    out = []
    for i in range(img.get_width()//32-1):
        out.append(img.subsurface((i*32, 0, 32, 32)))
    return out

a = pygame.image.load(get_asset('Idle (32x32).png', 'Main Characters', 'Mask Dude'))
b = unpack_animation(a)