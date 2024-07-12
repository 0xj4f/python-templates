"""
# Batch Process Example for lists

range(start, limit, step)

                +---+---+---+---+---+---+
                | P | y | t | h | o | n |
                +---+---+---+---+---+---+
Slice position: 0   1   2   3   4   5   6
Index position:   0   1   2   3   4   5

>>> p = ['P','y','t','h','o','n']
# Why the two sets of numbers:
# indexing gives items, not lists
>>> p[0]
 'P'
>>> p[5]
 'n'

# Slicing gives lists
>>> p[0:1]
 ['P']
>>> p[0:2]
 ['P','y']

---
array slicing
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed


A slice object can represent a slicing operation, i.e.:
a[start:stop:step]
is equivalent to:
a[slice(start, stop, step)]

"""

limit = 50
wordlist = list("a" * 1000)

for i in range(0, len(wordlist), limit):
    print("[+] batch:", i)

    # for accessing list arrays
    batch = wordlist[i : i + limit]
    for j, password in enumerate(batch):
        print(i + j)

    # or
    # for j in range(i, i + limit):
    #     print(j)
