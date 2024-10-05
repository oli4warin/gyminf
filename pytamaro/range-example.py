from pytamaro import show_graphic, blue, ellipse, empty_graphic, beside

my_graphic=empty_graphic()

for diameter in range(10,150,10):
    my_graphic = beside(my_graphic, ellipse(diameter,diameter,blue))

show_graphic(my_graphic)
