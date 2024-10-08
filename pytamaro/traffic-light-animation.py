from pytamaro import show_animation
from traffic_light import traffic_light

show_animation(
    [
        traffic_light(120, True, False, False),
        traffic_light(120, True, True, False),
        traffic_light(120, False, False, True),
        traffic_light(120, False, True, False)
    ], 
    duration=1000
)
