from pytamaro import rectangle, black, show_graphic, overlay, rotate, white

def square(size: float):
    return overlay(
        rectangle(size-10, size-10, white),
        rectangle(size, size, black))

def fractal(size: float):
    if size<20:
        return square(size)
    else: return overlay(
            rotate(45, fractal(size/2**0.5)),
            square(size)
        )

show_graphic(fractal(500));
