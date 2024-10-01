beside_same = beside(
    circular_sector(200, 90, black),
    circular_sector(200, 90, black)
)

beside_rotated = beside(
    rotate(0, circular_sector(200, 90, black)),
    rotate(90, circular_sector(200, 90, black))
)

two_by_two_same = above(
    beside(
            circular_sector(200, 90,black),
            circular_sector(200, 90,black)
    ),
    beside(
            circular_sector(200, 90, black),
            circular_sector(200, 90, black)
    )
)

two_by_two_rotated = above(
    beside(
            circular_sector(200, 90,black),
            rotate(90, circular_sector(200, 90,black))
    ),
    beside(
            rotate(180, circular_sector(200, 90, black)),
            rotate(270, circular_sector(200, 90, black))
    )
)
