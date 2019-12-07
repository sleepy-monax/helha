# %%


def power_set(values, index=-1, current=[], result=[]):
    n = len(values)

    if (n == index):
        return result

    if len(current) != 0:
        result.append(current[:])

    for i in range(index + 1, n):
        current.append(values[i])
        power_set(values, i, current)
        current.remove(values[i])

    return result


power_set(['a', 'b', 'c'])
