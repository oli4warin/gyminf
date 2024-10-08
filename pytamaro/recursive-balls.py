from pytamaro import show_graphic, blue, ellipse, empty_graphic, beside

def balls(size):
    if size <= 10:
        return ellipse(size, size, blue)
    else:
        return beside(balls(size-10), ellipse(size, size, blue))

show_graphic(balls(140))
