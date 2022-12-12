def _get_scenic_score(game_space: list[list[int]], x: int, y: int) -> int:
    scenic_score = 1

    for i in range(y - 1, -1, -1):
        if game_space[x][y] <= game_space[x][i]:
            scenic_score *= y - i
            break
    else:
        scenic_score *= y

    for i in range(y + 1, len(game_space[x])):
        if game_space[x][y] <= game_space[x][i]:
            scenic_score *= i - y
            break
    else:
        scenic_score *= len(game_space[x]) - y - 1

    for i in range(x - 1, -1, -1):
        if game_space[x][y] <= game_space[i][y]:
            scenic_score *= x - i
            break
    else:
        scenic_score *= x

    for i in range(x + 1, len(game_space)):
        if game_space[x][y] <= game_space[i][y]:
            scenic_score *= i - x
            break
    else:
        scenic_score *= len(game_space) - x - 1

    return scenic_score


with open('input') as input_file:
    game_space = []
    for line in input_file:
        game_space.append([int(i) for i in line.strip()])

    max_scenic_score = 0
    for i in range(1, len(game_space) - 1):
        for j in range(1, len(game_space[i]) - 1):
            if (score := _get_scenic_score(game_space, i, j)) > max_scenic_score:
                max_scenic_score = score

    print(max_scenic_score)
