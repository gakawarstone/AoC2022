game_logic = {
    "rock": {
        "lose": "paper",
        "win": "scissors",
    },
    "paper": {
        "lose": "scissors",
        "win": "rock",
    },
    "scissors": {
        "lose": "rock",
        "win": "paper",
    },
}

player_a_input_dict = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

result_input_dict = {"X": "lose", "Y": "draw", "Z": "win"}

type_score = {"rock": 1, "paper": 2, "scissors": 3}

result_score = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}


def _predict_item(opponent_item: str, result: str) -> str:
    if result == "draw":
        return opponent_item
    if result == "win":
        result = "lose"
    elif result == "lose":
        result = "win"
    return game_logic[opponent_item][result]


def _calculate_item_score(item: str) -> int:
    return type_score[item]


def _calculate_score(player_a_choose: str, predicted_result: str) -> int:
    opponent_item = player_a_input_dict[player_a_choose]
    result = result_input_dict[predicted_result]
    item = _predict_item(opponent_item, result)

    return _calculate_item_score(item) + result_score[result]


def calculate_score_from_input_file() -> int:
    with open("input") as input_file:
        total_score = 0
        for line in input_file:
            a_choose, b_choose = line.strip().split(" ")
            total_score += _calculate_score(a_choose, b_choose)
    return total_score


print(calculate_score_from_input_file())
