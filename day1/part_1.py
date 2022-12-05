with open('input') as input_file:
    max_group = 0
    current_group = 0

    for line in input_file:
        if line == '\n':
            if current_group > max_group:
                max_group = current_group
            current_group = 0
            continue
        
        current_group += int(line)


print(max_group)
