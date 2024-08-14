import copy
from simulate import simulate_battle
import sys
import os


def disable_prints():
    sys.stdout = open(os.devnull, 'w')


def enable_prints():
    sys.stdout = sys.__stdout__


simulations_count = 1000


def optimize(candidates, opposition):
    points = list()
    # draw yields 0 points
    # win yields 1 point
    # lose yielads -1 point
    for candidate_i in range(len(candidates)):
        points.append(0)

        disable_prints()
        for _ in range(simulations_count):
            candidate_copy = copy.deepcopy(candidates[candidate_i])
            opposition_copy = copy.deepcopy(opposition)
            result = simulate_battle(candidate_copy, opposition_copy)
            if result == 1:
                points[candidate_i] += 1
            elif result == 2:
                points[candidate_i] -= 1
        enable_prints()
        print(f"Candidate {candidate_i}/{len(candidates)}: {points[candidate_i]}")
    return points
