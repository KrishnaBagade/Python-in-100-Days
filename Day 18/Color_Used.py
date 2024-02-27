import turtle
import colorgram
import random

def making_colour_list(colour_used,colors_to_extract):
  color_to_use = []
  for color in range (colors_to_extract):
    color_set = colour_used[color]
    color_captured = color_set.rgb
    color_to_add = (color_captured[0],color_captured[1],color_captured[2])
    color_to_use.append(color_to_add)
  print(color_to_use)

colors_to_extract = 35
colour_used = colorgram.extract("HP.jpeg",colors_to_extract)
making_colour_list(colour_used,colors_to_extract)
v = [(192, 165, 118), (140, 165, 190), (58, 100, 140), (139, 93, 53),
     (220, 207, 125), (12, 20, 54), (183, 148, 169), (143, 177, 153), 
     (178, 153, 44), (57, 21, 9), (52, 13, 27), (71, 117, 84), (126, 79, 101),
     (11, 34, 19), (177, 185, 220), (27, 50, 126), (128, 33, 20), (165, 102, 131),
     (117, 32, 50), (170, 206, 182), (102, 120, 172), (93, 153, 104),
     (215, 176, 198), (86, 80, 17), (23, 89, 57), (178, 106, 90), (72, 151, 168),
     (161, 204, 214), (218, 179, 172), (24, 82, 94), (224, 204, 21)]