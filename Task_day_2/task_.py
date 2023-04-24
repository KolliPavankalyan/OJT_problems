n = 3
simulated_values = ['CCRLU', 'CRLCUC', 'CCCC']


chairs_needed = 0

for val in simulated_values:
    chairs_count = 0
    for op in val:
        if op == 'C':
            chairs_count += 1
        elif op == 'R' or op == 'L':
            chairs_count -= 1
        elif op == 'U':
            if chairs_count < n:
                chairs_count += 1
            else:
                chairs_needed += 1

    print(chairs_count)
