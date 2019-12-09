import sys

data = [line.rstrip() for line in sys.stdin.readlines()][0]

#data = '123456789012'
#img_width=3
#img_height=2

img_width = 25
img_height = 6
img_pixels = img_width * img_height

layers = list(map(''.join, zip(*[iter(data)]*img_pixels)))
layers.sort(key=lambda layer: layer.count('0'))
layer = layers[0]
print(layer.count('1') * layer.count('2'))