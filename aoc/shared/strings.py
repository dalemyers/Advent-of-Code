def findall(haystack: str, needle: str) -> list[int]:
    indices = []
    index = 0
    while True:
        substring = haystack[index:]
        found_index = substring.find(needle)
        if found_index == -1:
            break
        indices.append(index + found_index)
        index += found_index + len(needle)
    return indices
