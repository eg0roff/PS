import in_rectangle
import in_circle

def fill_container(container, i, part):
    if part[0]=='0':
        in_circle.circle_in(container, i, part)

    elif part[0] == '1':
        in_rectangle.rectangle_in(container, i, part)

    i = i + 1
