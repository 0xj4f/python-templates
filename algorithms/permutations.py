#!/usr/bin/env python
# -*- coding: utf-8 -*-


combinations = 0

def permutation(item):
    if len(item) == 0: return 0
    if len(item) == 1: return [item]

    l = []
    for i in range(len(item)):
        m = item[i]
        remaining_item = item[:i] + item[i+1:]

        for p in permutation(remaining_item):
            l.append([m] + p)

    return l



data = list('*+()')

for p in permutation(data):
    combinations += 1
    print("".join(p))

print("total Combinations: {}".format(combinations))


