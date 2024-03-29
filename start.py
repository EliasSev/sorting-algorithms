from sorting_algorithms import Sorting, Distributions
from graphics import Graphics

def start(n, algorithm, distribution, inverse=False, width=800, height=500, fps=60,
          color_range=None, lower=0, upper=800, restart=True):
    algorithm = str(algorithm).lower()
    distribution = str(distribution).lower()

    distributions = Distributions(n, lower=lower, upper=upper, inverse=inverse)
    dist_map = {"linear": distributions.linear,
                "quadratic": distributions.quadratic,
                "step": distributions.step,
                "logarithmic": distributions.logarithmic,
                "random": distributions.Random,
                "exponential": distributions.exponential}

    if distribution not in dist_map:
        raise ValueError(f"invalid distribution: {distribution}")
    A = dist_map[distribution]()

    sorting = Sorting(A)
    sort_map = {"quick sort": sorting.quick_sort,
                "insertion sort": sorting.insertion_sort,
                "selection sort": sorting.selection_sort,
                "bubble sort": sorting.bubble_sort,
                "merge sort": sorting.merge_sort,
                "bogo sort": sorting.bogo_sort,
                "heap sort": sorting.heap_sort,
                "shell sort": sorting.shell_sort}
    
    if algorithm not in sort_map:
        raise ValueError(f"invalid algorithm: {algorithm}")
    H = sort_map[algorithm]()
    graphics = Graphics(H, width, height, fps, color_range, restart, algorithm)
    graphics.start()
    


if __name__ == "__main__":
    num = 400     # number of numbers to sort
    fps = 300      # max frames per second
    width = 800   # window width
    height = 500  # window height
    color_range = (0, 1)            # 0: dark blue, 0.4: light blue, 0.5: light green, 0.65: yellow, 0.8: orange, 1: red
    algorithm = "shell sort"        # quick, insertion, selection, bubble, merge, bogo, heap, shell
    distribution = "exponential"    # linear, quadratic, step, logarithmic, random, exponential
    inverse = False  # reverse the numbers
    lower = 0        # lowest number
    upper = height   # largest number (upper <= height)
    restart = False  # pause when done sorting
    
    start(n=num,
        algorithm=algorithm,
        distribution=distribution,
        inverse=inverse,
        width=width,
        height=height,
        fps=fps,
        color_range=color_range,
        lower=lower,
        upper=upper,
        restart=restart)
    