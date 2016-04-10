import string

from graph import Node, Edge, Graph


def build_multiple_edges(node, iterable):
    return [Edge(node, value) for value in iterable]


def build_graph():
    numbers = "0123456789"
    ascii_upper = string.ascii_uppercase
    ascii_upper_and_numbers = ascii_upper + numbers

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node1_edges = build_multiple_edges(node2, ascii_upper)
    node1.edges = node1_edges

    node2_edges = build_multiple_edges(node3, ascii_upper)
    node2.edges = node2_edges

    node3_edges = build_multiple_edges(node5, ascii_upper_and_numbers) + [Edge(node4, ' ')]
    node3.edges = node3_edges

    node4_edges = build_multiple_edges(node5, ascii_upper_and_numbers)
    node4.edges = node4_edges

    node5_edges = build_multiple_edges(node6, ascii_upper_and_numbers)
    node5.edges = node5_edges

    node6_edges = build_multiple_edges(node7, ascii_upper_and_numbers)
    node6.edges = node6_edges

    node7_edges = build_multiple_edges(node8, ascii_upper_and_numbers)
    node7.edges = node7_edges

    node8_edges = build_multiple_edges(node9, ascii_upper_and_numbers)
    node8.edges = node8_edges

    graph = Graph()
    graph.nodes = [node1, node2, node3, node4, node5, node6, node7, node8]

    graph.start_node = node1
    graph.end_node = node9
    graph.current_node = graph.start_node

    return graph


def find_plates(input_string):
    graph = build_graph()
    start_plate_index = 0
    plates = []

    for i, sign in enumerate(input_string):
        next_node = graph.get_next_node(sign)
        if graph.current_node == graph.start_node:
            start_plate_index = i
        if not next_node:
            graph.reset_current_node()
        elif next_node == graph.end_node:
            plates.append((start_plate_index, i))
            graph.reset_current_node()
        else:
            graph.current_node = next_node

    return plates


def replace_plates(input_string):
    plates = find_plates(input_string)
    input_string_growth = 0

    for plate in plates:
        replace_length = len("<TABLICA REJ>")
        delta = plate[1] - plate[0] + 1
        replace_start_index = plate[0] + input_string_growth
        replace_end_index = plate[1] + input_string_growth + 1

        input_string = input_string.replace(input_string[replace_start_index: replace_end_index], "<TABLICA REJ>")
        input_string_growth += replace_length - delta

    return input_string
