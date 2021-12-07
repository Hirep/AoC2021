values = [
    [int(el) for el in line.strip()] for line in open('day_3').readlines()
]

test_values = [
    [0,0,1,0,0],
    [1,1,1,1,0],
    [1,0,1,1,0],
    [1,0,1,1,1],
    [1,0,1,0,1],
    [0,1,1,1,1],
    [0,0,1,1,1],
    [1,1,1,0,0],
    [1,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,1,0],
    [0,1,0,1,0],
]


def gamma(values, max_len):
    sums = [0 for _ in range(len(values[0]))]
    for i in range(len(sums)):
        for v in values:
            sums[i] += int(v[i])
    gamma_bin = []
    for val in sums:
        if val >= max_len / 2:
            gamma_bin.append(1)
        else:
            gamma_bin.append(0)
    return gamma_bin


def epsilon(values, max_len):
    sums = [0 for _ in range(len(values[0]))]
    for i in range(len(sums)):
        for v in values:
            sums[i] += int(v[i])
    epsilon_bin = []
    for val in sums:
        if val < max_len / 2:
            epsilon_bin.append(1)
        else:
            epsilon_bin.append(0)
    return epsilon_bin


def oxygen(values, mask):
    i = 0
    while True:
        bit = mask[i]
        new_values = []
        for value in values:
            if value[i] == bit:
                new_values.append(value)

        if len(new_values) > 1:
            values = new_values
            i += 1
            mask = gamma(values, len(values))
            continue
        else:
            return int(''.join([str(el) for el in new_values[0]]),2)


def co2(values, mask):
    i = 0
    while True:
        bit = mask[i]
        new_values = []
        for value in values:
            if value[i] == bit:
                new_values.append(value)

        if len(new_values) > 1:
            values = new_values
            i += 1
            mask = epsilon(values, len(values))
            continue
        else:
            return int(''.join([str(el) for el in new_values[0]]),2)



if __name__ == '__main__':
    # values = test_values
    gamma_bin = gamma(values, len(values))
    epsilon_bin = epsilon(values, len(values))
    g = int(''.join([str(el) for el in gamma_bin]), 2)
    e = int(''.join([str(el) for el in epsilon_bin]), 2)
    power = g * e
    life_support = oxygen(values, gamma_bin) * co2(values, epsilon_bin)
    print(power, life_support)
