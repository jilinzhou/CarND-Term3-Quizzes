# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],   # go down
         [0, 1]]   # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    value = [[99 for col in range(len(grid[0])+2)] for row in range(len(grid)+2)]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    x = goal[0]
    y = goal[1]
    v = 0

    value[x+1][y+1] = v
    closed[x][y] = 1
    policy[x][y] = '*'

    opened = []
    opened.append([v, x, y])

    finished = False

    while finished is not True:
        if len(opened) == 0:
            finished = True
        else:
            next = opened.pop()
            # v = next[0]
            x = next[1]
            y = next[2]

            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        # find minimum value around (x2, y2)
                        list = [value[x2][y2+1], value[x2+1][y2],  value[x2+2][y2+1], value[x2+1][y2+2]]
                        (v, index) = min((v, index) for index, v in enumerate(list))
                        v2 = v + cost
                        value[x2+1][y2+1] = v2
                        policy[x2][y2] = delta_name[index]
                        opened.append([v2, x2, y2])
                        closed[x2][y2] = 1

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return [value[i][1:len(grid[0])+1] for i in range(1, len(grid)+1)]

value = compute_value(grid, goal, cost)
for i in range(len(value)):
    print(value[i])
