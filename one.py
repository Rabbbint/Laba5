def longest_common_prefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]

    # Найти самое короткое слово в массиве
    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]

    return shortest

#O(n * m)