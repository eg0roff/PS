import input_shape

def container_filling(container):
    line_number = 0
    i=0
    with open('in.txt', 'r', encoding='utf-8') as fin:
        with open('out.txt', 'w', encoding='utf-8') as fout:
            for line in fin.readlines():
                if line_number < 100:
                    part = line.split('|')
                    print(part)

                    input_shape.fill_container(container, i, part)
                    i = i + 1

            fout.write("Контейнер заполнен\n")