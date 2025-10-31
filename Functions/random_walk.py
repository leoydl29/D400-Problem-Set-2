import random
import matplotlib.pyplot as plt

def walk(start=0,end=10,step_size=1):
    """
    Simulate a random walk that stops once it reaches `end` units away from the origin

    Parameters
    __________
        start (int): Starting position of the walker.
        end (int): Absolute distance from the origin at which the walk stops.

    Returns
    __________
        tracer (list[int]): The sequence of positions during the walk.
        steps (int): Total number of steps taken.
    """

    x = start
    steps = 0
    tracer = [x]

    while abs(x) < end*step_size:
        x += random.choice([-step_size, step_size])
        tracer.append(x)
        steps += 1

    print(f"Terminated in {steps} steps")

    return tracer, steps


def visualise_walk(tracer):
    """
    Visualize the random walk

    Parameters:
        tracer (list[int]): Sequence of positions from the walk.
        show_origin (bool): If True, draws a line at y=0 for reference.
    """

    plt.plot(tracer)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.xlabel("Step")
    plt.ylabel("Position")
    plt.title("Simulated Random Walk")
    plt.show()


    
        