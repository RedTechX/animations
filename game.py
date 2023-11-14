from pgzrun import *
from pgzhelper import *

WIDTH = 1000
HEIGHT = 500
speed = 1.7


move_anim = [
    'fxdash/tile000',
    'fxdash/tile001',
    'fxdash/tile002',
    'fxdash/tile003',
    'fxdash/tile004',
    'fxdash/tile005',
    'fxdash/tile006',
]
walk_anim = [
    'fxwalk/tile000',
    'fxwalk/tile003',
    'fxwalk/tile006',
    'fxwalk/tile009',
    'fxwalk/tile012',
    'fxwalk/tile015',
    'fxwalk/tile018',
    'fxwalk/tile021',
]

player  = Actor(walk_anim[0])
player.images = walk_anim
player.fps = 6.5
player.scale = 2.5


def move_input():
    if keyboard.w:
        player.y -= speed
    if keyboard.s:
        player.y += speed
    if keyboard.a:
        player.x -= speed
        if player.flip_x == False:
            player.flip_x = True
    if keyboard.d:
        player.x += speed
        if player.flip_x == True:
            player.flip_x = False


def draw():
    screen.clear()
    player.draw()


def update():
    player.animate()
    move_input()


go()