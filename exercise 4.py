from typing import List

def chunking_by(lst: List[int], size: int) -> List[List[int]]:
    if not lst:
        return []
    result = []
    chunk = []
    for elem in lst:
        chunk.append(elem)
        if len(chunk) == size:
            result.append(chunk)
            chunk = []
    if chunk:
        result.append(chunk)
    return result
print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) # [[5, 4, 7], [3, 4, 5], [4]]
print(chunking_by([3, 4, 5], 1)) # [[3], [4], [5]]
print(chunking_by([], 2)) # []