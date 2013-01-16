# Gumowski-Mira Strange Attractor Map
# http://en.wikipedia.org/wiki/Attractor
# FB - 20130115
import random
import math
from PIL import Image
imgx = 800; imgy = 800
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()
maxIt = 40
size = 20.0
xa = -size; xb = size
ya = -size; yb = size
a = random.random() * 1.5 - 1.0
b = random.random() * 0.1 + 0.9

def f(x):
    return a * x + 2.0 * (1.0 - a) * x * x / (1.0 + x * x)

def gm(x, y):
    xnew = b * y + f(x)
    y = f(xnew) - x
    x = xnew
    return (x, y)

percent = 0
for ky in range(imgy):
    pc = 100 * ky / (imgy - 1)
    if pc > percent: percent = pc; print '%' + str(percent)
    y0 = ya + (yb - ya) * ky / (imgy - 1)
    for kx in range(imgx):
        x0 = xa + (xb - xa) * kx / (imgx - 1)
        (x, y) = (x0, y0)
        for i in range(maxIt):
            (x, y) = gm(x, y)
        v0 = int(255 * (x - xa) / (xb - xa))
        v1 = int(255 * (y - ya) / (yb - ya))
        v2 = int(255 * abs(math.atan2(y, x)) / math.pi)
        v3 = int(255 * math.hypot(x, y) / math.hypot(size, size))
        v = v3 * 256 ** 3 + v2 * 256 ** 2 + v1 * 256 + v0
        colorRGB = int(16777215 * v / 256 ** 4)
        red = int(colorRGB / 65536)
        grn = int(colorRGB / 256) % 256
        blu = colorRGB % 256        
        pixels[kx, ky] = (red, grn, blu)
image.save("AttractorMap.png", "PNG")
