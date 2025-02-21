from pytamaro import pin, compose, center

def my_overlay(front: Graphic, back: Graphic) -> Graphic:
    return pin(center,
        compose(
            pin(center, front),
            pin(center, back)
        )
    )
