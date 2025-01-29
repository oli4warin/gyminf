from pytamaro import circular_sector, yellow, rotate, show_graphic

show_graphic(
    rotate(
            22.5,
            circular_sector(100,360-45,yellow)
    )
)
