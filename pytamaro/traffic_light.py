from pytamaro import overlay, ellipse, rectangle, above, red, yellow, green, black, Color

def lamp(size: float, color: Color):
    return overlay(
            ellipse(0.75*size,0.75*size, color),
            rectangle(size, size, black)
        )

def traffic_light(size: float, red_on: bool, yellow_on: bool, green_on: bool):
    return above(
        above(
            lamp(size, red if red_on else black),
            lamp(size, yellow if yellow_on else black)
            ),
        lamp(size,green if green_on else black)
        )
