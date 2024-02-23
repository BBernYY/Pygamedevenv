import os

def get_asset(name, *folders):
    return os.path.join('assets', *folders, name)

def unpack_animation(img):
    out = []
    for i in range(img.get_width()//32-1):
        out.append(img.subsurface((i*32, 0, 32, 32)))
    return out