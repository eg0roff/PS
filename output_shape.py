import out_circle
import out_rectangle


def out_shape(container, j):
    if container[j].index == '0':
        type = 'Круг'
        out_circle.out_circle(container, j, type)


    elif container[j].index == '1':
        type = 'Прямоугольник'
        out_rectangle.out_rectangle(container, j, type)
