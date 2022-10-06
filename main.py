from collections import deque


# represents element from matrix
class Node:
    def __init__(self, pos_x, pos_y, dist):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dist = dist

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_dist(self):
        return self.dist


# checks whether the element belongs to the matrix and whether it`s value is correct
def is_in_range(x, y, width, height):
    if height > x >= 0 and width > y >= 0:
        return True
    else:
        return False


# provides four main directions - up->down->left->right
row_move = [-1, 1, 0, 0]
col_move = [0, 0, -1, 1]


class SafeRoute:
    def __init__(self, matrix_file):
        with open(matrix_file, 'r') as file:
            graph = [[int(num) for num in line.split(' ')] for line in file]
        self.graph = graph
        self.height = len(self.graph)
        self.width = len(self.graph[0])

    @property
    def find_bfs(self):
        # means that sensor will be triggered (number doesn't really matters, should be just neither 1 nor 0)
        death_flag = 13

        # main algorithm to check every single element of matrix and put death flags around sensors
        for x in range(self.height):
            for y in range(self.width):
                if self.graph[x][y] == 0:
                    for i in range(len(row_move)):
                        if is_in_range(x + row_move[i], y + col_move[i], self.width, self.height):
                            self.graph[x + row_move[i]][y + col_move[i]] = death_flag

        is_visited = [[False for x in range(self.width)] for y in range(self.height)]

        queue = deque()

        # going through the first column for a places to start and adding them to the queue
        for x in range(self.height):
            if self.graph[x][0] == 1:
                queue.append(Node(x, 0, 0))
                is_visited[x][0] = True

        while queue:
            curr_node = queue.popleft()
            x = curr_node.get_pos_x()
            y = curr_node.get_pos_y()
            d = curr_node.get_dist()

            for i in range(len(row_move)):
                if is_in_range(x + row_move[i], y + col_move[i], self.width, self.height) and \
                        self.graph[x + row_move[i]][y + col_move[i]] == 1:
                    is_visited[x + row_move[i]][y + col_move[i]] = True
                    queue.append(Node(x + row_move[i], y + col_move[i], d + 1))
            if y == self.width - 1:
                return d


matrix = SafeRoute("input.txt")
shortest_route = matrix.find_bfs
f = open("output.txt", "w")
f.write(str(shortest_route))
