from pytamaro import show_graphic, blue, red, ellipse, empty_graphic, beside

my_graphic=empty_graphic()

for diameter in range(10,150,10):
    my_graphic = beside(my_graphic, 
            ellipse(diameter, diameter,
                blue if diameter<100 else red
            )
    )


show_graphic(my_graphic)
