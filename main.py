import container_construct
import container_in
import container_out
import container_clean


container = container_construct.cont_construct()
container_in.container_filling(container)
container_out.print_container(container)

container_clean.container_delete(container)

container_out.print_container(container)



