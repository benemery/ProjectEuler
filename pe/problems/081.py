from pe.toolbox import get_data

def find_shortest_path(matrix):
    """Traverse the matrix, finding the smallest summed path

    Let's do a breadth first search. We want to find the minimum path,
    so if we reach a point that we've already visited (all comparable
    points are reached in the same number of steps) with a lower sum,
    we know to stick with that one.
    """
    paths = {}
    lim = len(matrix)
    # There are N - 1 steps in each direction
    step_limit = 2 * (lim - 1)

    # initialise our paths
    paths[(0, 0)] = matrix[0][0]
    steps = [(0, 1), (1, 0)]
    for _ in range(step_limit):
        current_paths = paths.keys()
        for path in current_paths:
            i, j = path
            for step in steps:
                i_new = i + step[0]
                j_new = j + step[1]

                if i_new <= lim - 1 and j_new <= lim - 1:
                    point = (i_new, j_new)
                    tmp = matrix[i_new][j_new] + paths[path]
                    if point not in paths or tmp < paths[point]:
                        paths[point] = tmp

            # We don't need to keep any of the older steps as their
            # information is combined in the next step.
            del paths[path]

    # As we prune our dict as we go, there should only be a single value
    # at the end
    return paths.values()[0]



def test():
    m = [
        [131, 673, 232, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 11],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    return find_shortest_path(m) == 2427

def main():
    data = get_data('081_matrix.txt')
    matrix = [map(int, line.split(',')) for line in data.strip().split('\n')]

    return find_shortest_path(matrix)

if __name__ == '__main__':
    print "Passes test? ", test()
    print "Answer: ", main()

