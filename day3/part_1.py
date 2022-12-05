def _split_line_in_half(line: str) -> tuple[str, str]:
    index = len(line) // 2
    return (line[:index], line[index:])


def _find_share_character(line_a: str, line_b: str) -> str:
    return [i for i in line_a if i in line_b][0]


def _calculate_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38


with open('input') as input_file:
    priority_sum = 0
    for line in input_file:
        a, b = _split_line_in_half(line)
        share_item = _find_share_character(a, b)
        priority_sum += _calculate_priority(share_item)

print(priority_sum)
