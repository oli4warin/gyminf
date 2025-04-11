from pytamaro import (
        circular_sector, rectangle, compose, rotate,
        yellow,black,
        show_animation,
    )

def pacman(angle):
    return compose(
               rotate(angle/2,
                      circular_sector(100,360-angle,yellow)
                ),
               rectangle(210,210,black)
            )

frames=[]
for angle in range(0,80,5):
    frames.append(pacman(angle))
for angle in range(80,0,-5):
    frames.append(pacman(angle))
show_animation(frames)

show_animation([pacman(angle) for angle in [*range(0,80,5),*range(80,0,-5)]])
