scores_b = {"X": 1, "Y": 2, "Z": 3}

game_logic = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}


def _calculate_score(player_a_choose: str, player_b_choose: str) -> int:
    return scores_b[player_b_choose] + game_logic[player_a_choose + player_b_choose]


with open("input") as input_file:
    total_score = 0
    for line in input_file:
        a_choose, b_choose = line.strip().split(" ")
        total_score += _calculate_score(a_choose, b_choose)

print(total_score)
