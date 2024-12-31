"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""
from collections import Counter
from pathlib import Path

from aocd import data

cwd = root = Path("/")
dirs = Counter()

for line in data.splitlines():
    match line.split():
        case ["$", "cd", "/"]: cwd = root
        case ["$", "cd", ".."]: cwd = cwd.parent
        case ["$", "cd", name]: cwd /= name
        case [s, name] if s.isdigit():
            for p in [cwd, *cwd.parents]:
                dirs[p] += int(s)

rmbytes = dirs[root] - 70_000_000 + 30_000_000
a = sum(v for v in dirs.values() if v <= 100_000)
b = min(v for v in dirs.values() if v >= rmbytes)

print("answer_a:", a)
print("answer_b:", b)
