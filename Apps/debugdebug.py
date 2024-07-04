#import noise.perlin
#import noise.test
from api import average
from math import floor
import noise
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

#noise.perlin.SimplexNoise.

noise = PerlinNoise(octaves=10, seed=1)
#noise([-1, -1])
xpix, ypix = 100, 100
freq = 300
pic = [[noise([i/freq, j/freq]) for j in range(xpix)] for i in range(ypix)]

#for X in range(xpix):
#    pic[48][X] = 1.0
#    pic[49][X] = 1.0
#    pic[50][X] = 1.0
#    pic[51][X] = 1.0

#for X in range(xpix):
#    column = 0
#
#    for Y in range(ypix):
#        column += abs(floor(pic[Y][X]))
#    
#    for Y in range(ypix):
#        if Y == column:
#            pic[Y][X] = 1.0
#        else:
#            pic[Y][X] = 0.0

plt.imshow(pic, cmap='gray')
plt.show()
