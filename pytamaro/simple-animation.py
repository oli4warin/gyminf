from pytamaro import red, green, ellipse, show_animation

show_animation(
    [ellipse(300, 300, red), ellipse(300, 300, green)],
    duration=500
)
