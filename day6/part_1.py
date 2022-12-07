with open('input') as input_file:
    line = [l for l in input_file][0]

    ch_buffer = []
    for n, ch in enumerate(line):
        if len(ch_buffer) == 4:
            if len(set(ch_buffer)) == 4:
                print(n)
                break
            ch_buffer.pop(0)
        ch_buffer.append(ch)
