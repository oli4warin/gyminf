from pytamaro import *

def svg(filename,graphic):
    save_graphic("../../../images/"+filename+".svg",graphic,True)
)
    

def wide():
    return rectangle(200, 80, blue)
def tall():
    return rectangle(80, 200, green)

save_graphic(
        "../../../images/pytamaro-compose-example1.svg",
compose(
    pin(top_left, wide()),
    pin(top_left, tall()),
)
)


save_graphic(
        "../../../images/pytamaro-compose-example2.svg",
compose(
    pin(top_left, wide()),
    pin(top_right, tall()),
)
)

save_graphic(
        "../../../images/pytamaro-compose-example3.svg",
compose(
    pin(bottom_right, wide()),
    pin(top_center, tall()),
)
)

save_graphic(
        "../../../images/pytamaro-compose-example4.svg",
compose(
    pin(top_right, wide()),
    pin(center_left, tall()),
)
)


save_graphic(
        "../../../images/pytamaro-compose-example1-pin.svg",
        compose(
            pin(top_left, wide()),
            pin(top_left, tall()),
        ), True
)


save_graphic(
        "../../../images/pytamaro-compose-example2-pin.svg",
        compose(
            pin(top_left, wide()),
            pin(top_right, tall()),
        ), True
)

save_graphic(
        "../../../images/pytamaro-compose-example3-pin.svg",
        compose(
            pin(bottom_right, wide()),
            pin(top_center, tall()),
        ), True
)

save_graphic(
        "../../../images/pytamaro-compose-example4-pin.svg",
        compose(
            pin(top_right, wide()),
            pin(center_left, tall()),
        ), True
)


save_graphic("../../../images/pytamaro-pincompose-triangle.svg", triangle(100,100,60,red), True)
save_graphic("../../../images/pytamaro-pincompose-triangle-pin.svg", pin(top_center,triangle(100,100,60,red)), True)
save_graphic("../../../images/pytamaro-pincompose-circle.svg", ellipse(50,50,magenta), True)
save_graphic("../../../images/pytamaro-pincompose-composed.svg", compose( pin(top_center,triangle(100, 100, 60, red)), ellipse(50,50,magenta)), True)
save_graphic("../../../images/pytamaro-pincompose-example.svg", compose( pin(top_center,triangle(100, 100, 60, red)), ellipse(50,50,magenta)))

save_graphic("../../../images/pytamaro-pin-rectangle.svg", rectangle(200,100,red),True)
save_graphic("../../../images/pytamaro-pin-ellipse.svg", ellipse(200,100,red),True)
save_graphic("../../../images/pytamaro-pin-triangle.svg", triangle(200,100,90,red),True)
save_graphic("../../../images/pytamaro-pin-triangle.svg", triangle(200,100,90,red),True)
save_graphic("../../../images/pytamaro-pin-text.svg", text("Gym","Roboto",100,red),True)
save_graphic("../../../images/pytamaro-pin-circular-section.svg", circular_sector(100,210,red),True)
save_graphic("../../../images/pytamaro-pin-raute.svg", 
						pin(top_center,
							rotate(45,
								rectangle(100, 100, red)
								)
							),
             True
             )

save_graphic("../../../images/pytamaro-circular-sector.svg", 
						pin(center,
							rotate(210,
								circular_sector(200,120,cyan)
								)
							),
             True
             )


