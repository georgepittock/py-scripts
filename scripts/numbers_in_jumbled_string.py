"""
Takes a jumbled string of numbers 0-9 in word form and output it as the numbers.

i.e.
input: 'wtneoeehtro'
output: 123

Order does not matter of output


This was from an interview I had at a company (not going to say who). The function submitted is what I submitted. I
didn't save a copy of what I submitted but here is my closest guess, bar a few possible small possible mistakes I
didn't spot in the time it's like for like.
Although it is good and I was happy with it it's not perfect and I knew with some more time I could write better. So
it is below.


If you want to see how much better:
>>> import timeit
>>> import random
>>>
>>> all_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ] * 10
>>> for i in range(100):
...     use_nums = random.sample(all_nums, i)
...     test_nums = list("".join(use_nums))
...     random.shuffle(test_nums)
...     nums = "".join(test_nums)
...     a = timeit.timeit(
...         f"submitted('{nums}')", number=10000, setup="from __main__ import submitted"
...     )
...     b = timeit.timeit(f"new('{nums}')", number=10000, setup="from __main__ import new")
...     s1, s2 = submitted(nums), new(nums)
...     assert s1 == s2, f"s1 != s2 {s1}, {s2} ({nums}"
...     print(f"N: {i}    Old: {a}    New: {b}")

My old version is better for `use_nums` with length < 5. Other than that it becomes slower, look at the difference as length gets over 50!
"""
import random
import timeit
from collections import Counter


def submitted(string):
    out = ""
    num_count = [0 for _ in range(10)]
    for el in string:
        if el == "z":
            num_count[0] += 1
        if el == "w":
            num_count[2] += 1
        if el == "u":
            num_count[4] += 1
        if el == "x":
            num_count[6] += 1
        if el == "g":
            num_count[8] += 1
        if el == "o":
            num_count[1] += 1
        if el == "t":
            num_count[3] += 1
        if el == "f":
            num_count[5] += 1
        if el == "s":
            num_count[7] += 1
        if el == "i":
            num_count[9] += 1

    num_count[1] = num_count[1] - (num_count[2] + num_count[0] + num_count[4])
    num_count[3] = num_count[3] - (num_count[2] + num_count[8])
    num_count[5] = num_count[5] - (num_count[4])
    num_count[7] = num_count[7] - (num_count[6])
    num_count[9] = num_count[9] - (num_count[6] + num_count[5] + num_count[8])

    for index, elem in enumerate(num_count):
        for _ in range(elem):
            out += str(index)
    return out


def new(string):
    c = Counter(string)
    zeros = c["z"]
    twos = c["w"]
    fours = c["u"]
    sixes = c["x"]
    eights = c["g"]
    ones = c["o"] - (twos + zeros + fours)
    threes = c["t"] - (twos + eights)
    fives = c["f"] - fours
    sevens = c["s"] - sixes
    nines = c["i"] - (fives + sixes + eights)
    vals = dict(
        [
            (0, zeros),
            (1, ones),
            (2, twos),
            (3, threes),
            (4, fours),
            (5, fives),
            (6, sixes),
            (7, sevens),
            (8, eights),
            (9, nines),
        ]
    )
    out = "".join([str(k) * v for k, v in vals.items() if v != 0])
    return out
