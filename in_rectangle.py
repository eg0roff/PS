import class_construct


def rectangle_in(container, i, part):
    container[i] = class_construct.Circle()

    container[i].index = part[0]
    container[i].x1 = part[1]
    container[i].y1 = part[2]

    container[i].x2 = part[3]
    container[i].y2 = part[4]

    container[i].color = part[5]