import ctypes


class LinkedList:
    def __init__(self) -> None:
        self.node_numbers = 0
        self.current_node_index = 0
        self.node_addresses = {}

    def add_node(self, **kwargs):
        self.new_node = Node(kwargs=kwargs)
        self.node_addresses[self.current_node_index] = {
            'node_id': self.new_node.node_id,
            'node_index': self.current_node_index
        }
        self.current_node_index += 1
        self.node_numbers += 1

    def get_data(self):
        for element in self.node_addresses:
            print(ctypes.cast(element.get('node_id'), ctypes.py_object).value)


class Node:
    def __init__(self, **kwargs):
        self.node_id = id(self)
        self.data = kwargs
        self.next = None


l1 = LinkedList()
l1.add_node(kwargs={'User_id': 987931561, 'Name': 'Hamze'})
l1.add_node(kwargs={'User_id': 789756936, 'Name': 'Sami'})
l2 = LinkedList()
l2.add_node(kwargs={'student_id': 12369855, 'Name': 'Khaldon'})
l2.add_node(kwargs={'student_id': 12367778, 'Name': 'Ahmad'})
l1.get_data()
l2.get_data()


# class LinkedList:
#     # Class variables
#     number_of_nodes = 0
#     node_index = 0
#     node_addresses = {}
#     # Constructor

#     def __init__(self, **kwargs) -> None:
#         LinkedList.number_of_nodes += 1
#         self.data = kwargs
#         self.node_id = id(self)
#         self.index = LinkedList.node_index
#         LinkedList.node_addresses[self.index] = {
#             'id': self.node_id,
#             'index': self.node_index
#         }
#         LinkedList.node_index += 1


# node1 = LinkedList()
# node2 = LinkedList()
# print(LinkedList.number_of_nodes)
# print(LinkedList.node_addresses)
