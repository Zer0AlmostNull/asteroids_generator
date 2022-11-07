from PIL import Image, ImageDraw
from point import Point

import math
import random

# IMAGE properties
IMG_SIZE = 400
IMG_MARGIN = 20

# ASTEROID properties
MAX_ANGLE_DIST = math.pi/2 # 90°
MIN_ANGLE_DIST = 5 * math.pi/18 # 50°

RADIUS = IMG_SIZE // 2 - IMG_MARGIN
COLOR_RANGE = (40, 90)

def generate_asteroid(path: str = None):
    # pick random color
    COLOR = random.randrange(COLOR_RANGE[0], COLOR_RANGE[1])
    
    # create image
    image = Image.new("RGBA",(IMG_SIZE, IMG_SIZE), (0,0,0,0))
    draw = ImageDraw.Draw(image)
    
    # generate random angles aross the circle
    points = [0,]
    while  points[-1] < 2 * math.pi:
        points.append(points[-1] + random.uniform(MIN_ANGLE_DIST, MAX_ANGLE_DIST))
    points.pop()
    
    # convert angle to point on the circle
    points = [Point(IMG_SIZE//2 + RADIUS * math.cos(point),
                    IMG_SIZE//2 + RADIUS * math.sin(point))
                    for point in points]

    # add randomness
    for i in range(0, len(points)):
        points[i] += Point(IMG_MARGIN * random.random(), IMG_MARGIN * random.random())
    
    
    # draw polygon - asteroid
    draw.polygon([*map(tuple, points)], fill = tuple(3*[COLOR]))

    if path == None:
        image.show()
    else:
        image.save(path)

if __name__ == "__main__":
    generate_asteroid()
