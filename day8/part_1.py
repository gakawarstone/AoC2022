def _check_visability(game_space: list[list[int]], x: int, y: int) -> bool:
    not_vis_score = 0

    for i in range(0, y):
        if game_space[x][y] <= game_space[x][i]:
            not_vis_score += 1
            break

    for i in range(y + 1, len(game_space[x])):
        if game_space[x][y] <= game_space[x][i]:
            not_vis_score += 1
            break

    for i in range(0, x):
        if game_space[x][y] <= game_space[i][y]:
            not_vis_score += 1
            break

    for i in range(x + 1, len(game_space)):
        if game_space[x][y] <= game_space[i][y]:
            not_vis_score += 1
            break

    return not_vis_score < 4


with open('input') as input_file:
    game_space = []
    for line in input_file:
        game_space.append([int(i) for i in line.strip()])

    visability_map = [[1 for _ in range(len(line))] for line in game_space]

    for i in range(1, len(game_space) - 1):
        for j in range(1, len(game_space[i]) - 1):
            if not _check_visability(game_space, i, j):
                visability_map[i][j] = 0

    print(sum([sum(line) for line in visability_map]))
