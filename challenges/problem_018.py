# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by
# trying every route. However, Problem 67, is the same challenge with a triangle
# containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# NOTES
#
# This screams decision tree. so make a class of nodes, and calculate the sum of the paths? How not to brute-force that?
#
# class Node {
#   id: string (guid?)
#   left: string
#   right: string
#   addBelow
#   greatestSum below
# }
#
# This is drawn as a pyramid. But that might be a lie. What if this is a reverse dykstra problem domain, wherein we are
# trying to find the LONGEST path through? note that these are ints (could be floats, whatever) these are _edges_, not
# nodes!
#
# Rules:
# - Path must consist of unique members
# - each member must only be visited once.
# - cannot travel "backwards"
#
# for row_idx, 0_0 connects to 1_0, 1_1
#     n_n connects to (n+1)_(n) and (n+1)_(n+1)... easy
#
# remember to feed it a start value (the distance to 0_0)
#
# class Node {
#     idx: int
#     row: int
#     dist0: (n) int
#     dist1: (n+1) int
# }
#
# The next weirdness is how to not brute force it... how about rows at a time? batch from the bottom up in groups of
# 4? 5? only focus on the highest 4? 5?
#
# This is recursive at its heart, because we calculate a triangle into 2 numbers and take the higher of the two
#
# for rows r, start at row r-1, and coalesce each member into to values.
# for each above row, do the same thing.
# batch every 4 rows? take the largest x (4 or 5 or few) to continue.

import time

start = time.time()
small_tree = ['75',
              '95', '64',
              '17', '47', '82',
              '18', '35', '87', '10',
              '20', '04', '82', '47', '65',
              '19', '01', '23', '75', '03', '34',
              '88', '02', '77', '73', '07', '63', '67',
              '99', '65', '04', '28', '06', '16', '70', '92',
              '41', '41', '26', '56', '83', '40', '80', '70', '33',
              '41', '48', '72', '33', '47', '32', '37', '16', '94', '29',
              '53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14',
              '70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17', '57',
              '91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29', '48',
              '63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87', '40', '31',
              '04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53', '60', '04', '23']


class BruteForceNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_row = None if not left else left[0]
        self.left_index = None if not left else left[1]
        self.right_row = None if not right else right[0]
        self.right_index = None if not right else right[1]

    def __repr__(self):
        return f'{self.value} => ({getattr(self, "left_row", "None")}, {getattr(self, "left_index", "None")}) ' \
               f'and ({getattr(self, "right_row", "None")}, {getattr(self, "right_index", "None")})'


def create_structure(tree: list[str]):
    row_num = 0
    start = 0
    rows = []
    while True:
        finish = start + row_num + 1
        row = tree[start:finish]
        if not row:
            break
        rows.append(row)
        row_num += 1
        start = finish
    return rows


def create_map(structure: list[list[str]]):
    # Now assign to the node and link them up node (row,idx) left is (row+1, idx) right is (row+1, idx+1)
    node_map = []
    for row_num, row in enumerate(structure):
        new_row = []
        for idx, node in enumerate(row):
            if row_num != len(structure) - 1:
                new_row.append(BruteForceNode(int(node), left=(row_num + 1, idx), right=(row_num + 1, idx + 1)))
            else:
                new_row.append(BruteForceNode(int(node)))
        node_map.append(new_row)
    return node_map


counter = 0


def get_largest_sum(graph, node):
    global counter
    counter += 1
    if node.left_row and node.right_row:
        print(f'getting sum from ({node.left_row}, {node.left_index}) and ({node.left_row}, {node.right_index})')
    return max(get_node_total_left(graph, node), get_node_total_right(graph, node))


def get_node_total_left(graph: list[list[BruteForceNode]], node: BruteForceNode):
    if node.left_index and node.left_row:
        return node.value + get_largest_sum(graph, graph[node.left_row][node.left_index])
    return node.value


def get_node_total_right(graph: list[list[BruteForceNode]], node: BruteForceNode):
    if node.right_row and node.right_index:
        return node.value + get_largest_sum(graph, graph[node.right_row][node.right_index])
    return node.value


node_map = create_map(create_structure(small_tree))


answer = get_largest_sum(node_map, node_map[0][0])
end = time.time()
print(f'visited {counter} nodes in {end-start} sec')
print(f"the answer is {answer}")
