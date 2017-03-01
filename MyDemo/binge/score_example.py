#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: score_example.py
@time: 2017-02-14 16:09
@description:
"""


def PercentileRank(scores, your_score):
    """Computes the percentile rank relative to a sample of scores."""
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


def Percentile(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank. """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score


def Percentile2(scores, percentile_rank):
    """Computes the value that corresponds to a given percentile rank.

    Slightly more efficient.
    """
    index = int(percentile_rank / 100 * (len(scores) - 1))
    return scores[index]


scores = [55, 66, 77, 88, 99]
your_score = 88

percentile_rank = PercentileRank(scores, your_score)
print(percentile_rank)

print('score, percentile rank')
for score in scores:
    print(PercentileRank(scores, score))

print('prank, score, score')
for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
    print(percentile_rank, Percentile(scores, percentile_rank), Percentile2(scores, percentile_rank)),
    # print(Percentile(scores, percentile_rank))
    # print(Percentile2(scores, percentile_rank))
