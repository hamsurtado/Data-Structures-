from LinkedList import LinkedList
from Node import Node 

my_node = Node(27)
my_linked_list = LinkedList(my_node)
my_other_node = Node(32)
my_third_node = Node(112)

my_linked_list.add_node(my_other_node)
my_linked_list.add_node(my_third_node)


print(my_linked_list)
my_linked_list.reverse_list()
print(my_linked_list)