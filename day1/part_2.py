with open('input') as input_file:
    max_groups = []
    current_group = 0

    for line in input_file:
        if line == '\n':
            max_groups.append(current_group)
            if len(max_groups) > 3:
                max_groups.sort()
                max_groups = max_groups[-3:]

            current_group = 0
            continue
        
        current_group += int(line)


print(sum(max_groups))
