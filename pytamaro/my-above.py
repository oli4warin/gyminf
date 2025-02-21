from pytamaro import pin, compose, center, top_center, bottom_center

def my_above(top: Graphic, bottom: Graphic) -> Graphic:
    return pin(center,
        compose(
            pin(bottom_center, top),
            pin(top_center, bottom)
        )
    )
