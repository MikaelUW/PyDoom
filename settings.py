import math

WIDTH = 1900
HEIGHT = 1040
HALF_WIDTH = WIDTH // 2
HALF_HEIGTH = HEIGHT // 2


FPS = 120 #fps limit

PLAYER_START_POS = (2, 9)
PLAYER_ANGLE = 11
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_FAT = 60

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE / 2