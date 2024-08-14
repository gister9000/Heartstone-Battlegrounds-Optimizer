from simulate import simulate_battle

simulations_count = 1000


def optimize(candidates, opposition):
    points = list()
    # draw yields 0 points
    # win yields 1 point
    # lose yielads -1 point

    for candidate_i in range(len(candidates)):
        points.append(0)
        for simulation_i in range(simulations_count):
            result = simulate_battle(candidates[candidate_i], opposition)
            if result == 1:
                points[candidate_i] += 1
            elif result == 2:
                points[candidate_i] -= 1
        print(f"Candidate {candidate_i}: {points}")
    return points
