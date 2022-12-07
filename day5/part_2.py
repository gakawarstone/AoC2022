from dataclasses import dataclass


@dataclass
class _GameTurn:
    num_of_items: int
    from_column: int
    to_column: int


def _serialize_game_space_input(input_: list[str]) -> list[list[str]]:
    game_space = [_get_line_chars(l) for l in input_]
    game_space = [*zip(*game_space)]
    game_space = [
        list(reversed(line))
        for line in game_space
    ]
    game_space = list(map(
        lambda a: list(filter(lambda k: k != ' ', a)),
        [l for l in game_space]
    ))
    return game_space


def _get_line_chars(line: str) -> list[str]:
    return [
        line[i]
        for i in _get_char_indexes(len(line))
    ]


def _get_char_indexes(line_length: int) -> list[int]:
    return list(range(1, line_length, 4))


def _play_turn(game_space: list[list[str]], turn: _GameTurn) -> None:
    items = []
    for _ in range(turn.num_of_items):
        items.append(game_space[turn.from_column - 1].pop())
    [game_space[turn.to_column - 1].append(i) for i in reversed(items)]


def _serialize_game_turn(input_: str) -> _GameTurn:
    return _GameTurn(
        num_of_items=int((
            expr := input_.split(
                'move ')[1].split(
                ' from ')
        )[0]),
        from_column=int((
            expr := expr[1].split(
                ' to ')
        )[0]),
        to_column=int(expr[1])
    )


def _get_answer_string_from_game_space(game_space: list[list[str]]) -> str:
    return ''.join([l[-1] for l in game_space])


with open('input') as input_file:
    input_ = []
    for line in input_file:
        if line == '\n' or line.startswith(' 1'):
            break
        input_.append(line)

    game_space = _serialize_game_space_input(input_)

    for line in input_file:
        if not line.strip():
            continue
        game_turn = _serialize_game_turn(line)
        _play_turn(game_space, game_turn)

    print(_get_answer_string_from_game_space(game_space))
