from pytamaro import circular_sector,rotate,yellow,show_graphic

show_graphic(
    rotate(45/2,
        circular_sector(100,360-45,yellow)
    )
)
