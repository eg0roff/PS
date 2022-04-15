def out_circle(container, j, type):
    with open('out.txt', 'a', encoding='utf-8') as fout:
        fout.write(f'\n Это {type} \n Центр с координатами центра({container[j].x},{container[j].y}) '
                   f'\n Радиус = {container[j].r} \n Цвет фигуры = {container[j].color}')