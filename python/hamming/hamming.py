def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Not equal length")

    strand_a.upper(), strand_b.upper()
    return sum(1 for (i, j) in zip(strand_a, strand_b) if i != j)
