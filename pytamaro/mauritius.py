from pytamaro import empty_graphic, rectangle, above, show_graphic, rgb_color

mauritius_red = rgb_color(234,40,57) 
mauritius_blue = rgb_color(26,32,109) 
mauritius_yellow = rgb_color(255,212,0) 
mauritius_green = rgb_color(1,164,81) 

mauritius_red, mauritius_blue, mauritius_yellow, mauritius_green
 
width=300
height=2/3*width

mauritius_flag = empty_graphic()

for color in [mauritius_red, mauritius_blue, mauritius_yellow, mauritius_green]:
    mauritius_flag = above(mauritius_flag, rectangle(width, height/4, color))

show_graphic(mauritius_flag)
