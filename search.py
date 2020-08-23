# Use this code to find which numbers repeat an interesting number of times in Pascal's triangle.

import time
from collections import defaultdict

def search(row_limit: int, minimum_counts: int = 5) -> [(int, int)]:
    # A dictionary representing how many times a number appears in the cells we've generated. Every number appears once in the outer diagonals,
    # so we can begin the counts at 2
    counts = defaultdict(lambda: 2)

    # Below I am dictating the rows and columns I will compute cell values for.

    # (I have excluded the outer two diagonals (on either side) of Pascal's triangle, because we know that the numbers in those diagonals (across the whole triangle) are an infinite number of 1s and two appearances of all other positive integers apart from 2 (for which there is only one appearance).)

    # Faster method for calculating subsequent nCr for performance reasons
    # While this part was by no means the bottleneck, it's still nice to have
    for n in range(4, row_limit):
        nCr = n
        for r in range(2, n - 1):
            nCr *= n - r + 1
            nCr //= r
            counts[nCr] += 1

    # Below I am checking how many times each distinct number appears in the cells we've generated. If a number appears more than four times, print it.

    matches = list()

    for entry, frequency in counts.items():
        if frequency < minimum_counts:
            continue

        matches.append((entry, frequency))

    return matches


if __name__ == '__main__':
    start_time = time.time()

    matches = search(3001, 5)

    for entry, frequency in matches:
        print(f"The number {entry:,} appears at least {frequency} times across the whole triangle")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'Ran in {elapsed_time} seconds')

