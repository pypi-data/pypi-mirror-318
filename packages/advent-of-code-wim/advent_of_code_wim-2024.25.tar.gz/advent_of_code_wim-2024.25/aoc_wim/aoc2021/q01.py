"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""
from aocd import data

ns = [int(n) for n in data.split()]
print("answer_a:", sum(n2 > n1 for n1, n2 in zip(ns, ns[1:])))
print("answer_b:", sum(n2 > n1 for n1, n2 in zip(ns, ns[3:])))
