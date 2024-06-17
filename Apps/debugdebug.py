from api import color_with_light

print(color_with_light("#FFFFFF", 15, 15))
assert color_with_light("#FFFFFF", 15, 15) == "#ffffff"

print(color_with_light("#000000", 0, 15))
assert color_with_light("#000000", 0, 15) == "#000000"

#assert color_with_light("#00FF00)