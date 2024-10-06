from pytamaro import beside,empty_graphic, Graphic

def beside_list(graphic_list: list[Graphic]) -> Graphic:
    result=empty_graphic()
    for graphic in graphic_list:
            result=beside(result, graphic)
    return result
