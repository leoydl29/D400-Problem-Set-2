def factor_pairs(n: int) -> list[tuple[int, int]]:
    """
    Returns all unique integer factor pairs (a, b) such that a * b = n.
    Only positive divisors are considered and mirrored duplicates are excluded,
    e.g. (a, b) is included but (b, a) is not.

    Parameters
    ----------
    n : int
        The number to factorise.

    Returns
    -------
    list of tuple[int, int]
        A list of tuples containing the factor pairs.
    """
    return [(i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0]
