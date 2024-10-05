from pytamaro import rectangle, black, show_graphic, overlay, rotate, yellow

def square(size: float):
    return overlay(
        rectangle(
            size-10,
            size-10,
            yellow,
        ),
        rectangle(
            size,
            size,
            black
        )
    )

def fractal(size: float):
    if size<20:
        return square(size)
    else: return overlay(
            rotate(10,
                   fractal(size-10)
            ),
            square(size)
        )

show_graphic(fractal(500));
