import sys

data = [line.rstrip() for line in sys.stdin.readlines()][0]

img_width = 25
img_height = 6
img_pixels = img_width * img_height

layers = list(map(''.join, zip(*[iter(data)]*img_pixels)))
final_img_data = ['.'] * img_pixels
for layer in layers:
    for i in range(len(layer)):
        if final_img_data[i] in [' ', '*']:
            continue
        final_img_data[i] = [' ', '*', '.'][int(layer[i])]

final_img_lines = list(map(''.join, zip(*[iter(final_img_data)]*img_width)))
for line in final_img_lines:
    print(line)