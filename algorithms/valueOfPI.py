import random

def estimate_pi(num_simulations, interval):
    results = []
    for simulation in range(num_simulations):
        points_circle = 0
        points_square = 0
        for i in range(interval**2):
            rand_x = random.uniform(-1, 1)
            rand_y = random.uniform(-1, 1)
            origin_dist = rand_x**2 + rand_y**2

            if origin_dist <= 1:
                points_circle += 1
            points_square += 1

        pi_estimate = 4 * points_circle / points_square
        results.append(pi_estimate)
    return results

num_simulations = 10
interval = 1000
print (estimate_pi(num_simulations, interval))
