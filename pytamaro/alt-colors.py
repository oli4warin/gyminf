from pytamaro import show_graphic, blue, red, ellipse, empty_graphic, beside

my_graphic=empty_graphic()
diameter_list=range(10,150,10)

for index in range(len(diameter_list)):
    my_graphic = beside(my_graphic, 
            ellipse(diameter_list[index], diameter_list[index],
                blue if index%2==0 else red
            )
    )


show_graphic(my_graphic)

