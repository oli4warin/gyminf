from pytamaro import compose, pin, show_graphic, save_graphic, rectangle, top_left, top_center, blue, red, top_right, center, bottom_center, bottom_left, bottom_right, center_left, green

wide = rectangle(200, 80, blue)
tall = rectangle(80, 200, green)



save_graphic(
        "../../../images/pytamaro-compose-example1.svg",
compose(
    pin(top_left, wide),
    pin(top_left, tall),
)
)


save_graphic(
        "../../../images/pytamaro-compose-example2.svg",
compose(
    pin(top_left, wide),
    pin(top_right, tall),
)
)

save_graphic(
        "../../../images/pytamaro-compose-example3.svg",
compose(
    pin(bottom_right, wide),
    pin(top_center, tall),
)
)

save_graphic(
        "../../../images/pytamaro-compose-example4.svg",
compose(
    pin(top_right, wide),
    pin(center_left, tall),
)
)


save_graphic(
        "../../../images/pytamaro-compose-example1-pin.svg",
        compose(
            pin(top_left, wide),
            pin(top_left, tall),
        ), True
)


save_graphic(
        "../../../images/pytamaro-compose-example2-pin.svg",
        compose(
            pin(top_left, wide),
            pin(top_right, tall),
        ), True
)

save_graphic(
        "../../../images/pytamaro-compose-example3-pin.svg",
        compose(
            pin(bottom_right, wide),
            pin(top_center, tall),
        ), True
)

save_graphic(
        "../../../images/pytamaro-compose-example4-pin.svg",
        compose(
            pin(top_right, wide),
            pin(center_left, tall),
        ), True
)
