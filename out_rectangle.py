def out_rectangle(container, j, type):
    with open('out.txt', 'a', encoding='utf-8') as fout:
        fout.write(f'\n Это {type} \n Левый верхний угол({container[j].x1},{container[j].y1}) '
                   f'\n Правый нижний угол({container[j].x2},{container[j].y2})'
                   f'\n Цвет фигуры = {container[j].color}')