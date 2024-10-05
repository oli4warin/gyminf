from pytamaro import rgb_color, white, empty_graphic, circular_sector, show_graphic, pin, compose, bottom_center

rainbow_red = rgb_color(255, 0, 0) 
rainbow_orange = rgb_color(255, 140, 0) 
rainbow_yellow = rgb_color(255, 240, 0) 
rainbow_green = rgb_color(0, 138, 40) 
rainbow_blue = rgb_color(0, 80, 255) 
rainbow_purple = rgb_color(120, 0, 140) 

color_list=[rainbow_red, rainbow_orange, rainbow_yellow, rainbow_green, rainbow_blue, rainbow_purple, white]
radius_list=range(200, 60, -20)

rainbow = empty_graphic()

for index in range(len(color_list)):
    rainbow = pin(bottom_center,compose(circular_sector(radius_list[index],180,color_list[index]),rainbow))

show_graphic(rainbow)
