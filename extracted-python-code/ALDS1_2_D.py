import sys
from typing import Iterator


# Standard output speedup
def output(result: list[str]) -> None:
    sys.stdout.write('\n'.join(result) + '\n')


# effective gaps [Reference: Tokuda (1992)]
def tokuda_gaps(n: int) -> list[int]:
    gaps = []
    k = 1
    while True:
        gap = (9**k - 4**k) // (5 * 4**(k-1))
        if gap > n:
            break
        gaps.append(gap)
        k += 1
    gaps.reverse()
    return gaps

def gapped_insertion_sort(arr: list[int], gap: int) -> int:
    cnt = 0
    n = len(arr)
    for i in range(gap, n):
        val = arr[i]
        j = i - gap
        while j >= 0 and arr[j] > val:
            arr[j + gap] = arr[j]
            j -= gap
            cnt += 1
        arr[j + gap] = val
    return cnt


def shell_sort(arr: list[int]) -> tuple[int, int, list[int]]:
    cnt = 0
    n = len(arr)
    gaps = tokuda_gaps(n)
    m = len(gaps)
    for i in range(m):
        cnt += gapped_insertion_sort(arr, gaps[i])
    return cnt, m, gaps


def solve(lines: Iterator[str] = None) -> None:
    result = []  # Output buffer

    # --- Logic starts here ---
    n = int(next(lines))
    arr = [int(next(lines)) for _ in range(n)]
    cnt, m, gaps = shell_sort(arr)

    result.append(f'{m}')
    result.append(' '.join(map(str, gaps)))
    result.append(f'{cnt}')
    result.append('\n'.join(map(str, arr)))

    # --- Logic ends here ---

    output(result)


def main():
    data = sys.stdin.buffer.read().decode()
    lines = [ln for line in data.splitlines() if (ln := line.strip())]  # drop blank lines in case of trailing newlines
    solve(iter(lines))


if __name__ == '__main__':
    main()

