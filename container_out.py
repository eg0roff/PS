import output_shape

def print_container(container):
    fill_up = 0

    for i in range(len(container)):
        if container[i] == '':
            with open('out.txt', 'a', encoding='utf-8') as fout:
                fout.write(f'\n Контейнер содержит {i} элементов')
                fill_up = i
            break


    with open('out.txt', 'a', encoding='utf-8') as fout:
        if fill_up != 0:
            for j in range(fill_up):
                output_shape.out_shape(container, j)

        elif fill_up == 0:
            fout.write(f'\n\nКонтейнер содержит {fill_up} элементов \n Контейнер пуст')






