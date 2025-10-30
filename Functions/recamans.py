from typing import List

def recaman_sequence(n: int) -> List[int]:
    """
    Generate the first n terms of the Recamán sequence.

    a0 = 0
    a_k = a_{k-1} - k if (a_{k-1} - k) >= 0 and not already seen
          else a_{k-1} + k

    Args:
        n: Number of terms to generate (n >= 0).

    Returns:
        A list of n integers forming the Recamán sequence.
    """
    if n <= 0:
        return []

    res = [0]
    seen = {0}

    for i in range(1, n):
        candidate = res[-1] - i
        if candidate < 0 or candidate in seen:
            candidate = res[-1] + i
        res.append(candidate)
        seen.add(candidate)

    return res

if __name__ == "__main__":
    n = 20
    seq = recaman_sequence(n)
    print(" ".join(map(str, seq)))