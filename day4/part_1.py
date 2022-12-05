_Range = tuple[int, int]


def _parse_ranges(line: str) -> tuple[_Range, _Range]:
    a, b = line.strip().split(',')
    range_a, range_b = [
        _Range(map(int, i.split('-')))
        for i in (a, b)
    ]
    return range_a, range_b


def _is_range_contains_range(a: _Range, b: _Range) -> bool:
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    if b[0] >= a[0] and b[1] <= a[1]:
        return True
    return False


with open('input') as input_file:
    cnt = 0
    for line in input_file:
        a, b = _parse_ranges(line)
        if _is_range_contains_range(a, b):
            cnt += 1

print(cnt)
