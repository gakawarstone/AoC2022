def _find_share_character(group: list[str]) -> str:
    contains = list(set(group[0]))
    to_remove = []
    for line in group[1:]:
        for i in contains:
            if i not in line:
                to_remove.append(i)
        for i in set(to_remove):
            contains.remove(i)
        to_remove = []
    return contains[0]


def _calculate_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38


with open('input') as input_file:
    priority_sum = 0
    group = []
    for line in input_file:
        group.append(line.strip())
        if len(group) == 3:
            share_char = _find_share_character(group)
            priority_sum += _calculate_priority(share_char)
            group = []

print(priority_sum)
