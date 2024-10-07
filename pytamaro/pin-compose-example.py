from pytamaro import ellipse, triangle, blue, magenta, pin, compose, show_graphic, top_center, save_graphic, show_graphic, save_graphic

compose(
        pin(
            top_center,
            triangle(100, 100, 60, blue)
            ),
        ellipse(50,50,magenta)
)

save_graphic("../../../images/pytamaro-pincompose-triangle.svg", triangle(100,100,60,blue), True)
save_graphic("../../../images/pytamaro-pincompose-triangle-pin.svg", pin(top_center,triangle(100,100,60,blue)), True)
save_graphic("../../../images/pytamaro-pincompose-circle.svg", ellipse(50,50,magenta), True)
save_graphic("../../../images/pytamaro-pincompose-composed.svg", compose( pin(top_center,triangle(100, 100, 60, blue)), ellipse(50,50,magenta)), True)

