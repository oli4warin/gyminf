from pytamaro import empty_graphic, rectangle, beside, show_graphic, blue, white, red

width=300
height=3/5*width
french_flag = empty_graphic()

french_flag = beside(french_flag, rectangle(width/3, height, blue))
french_flag = beside(french_flag, rectangle(width/3, height, white))
french_flag = beside(french_flag, rectangle(width/3, height, red))

show_graphic(french_flag)
