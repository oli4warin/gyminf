from pytamaro import pin, compose, center, center_left, center_right

def my_beside(left: Graphic, right: Graphic) -> Graphic:
    return pin(center,
        compose(
            pin(center_right, left),
            pin(center_left, right)
        )
    )
