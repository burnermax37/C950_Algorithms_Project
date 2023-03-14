# Load distances
DISTANCES = []
# DISTANCES is created as a global object so that it can be accessed by main function and object methods
# of the truck class.


def load_distance_data(filename):
    """Load data from distances CSV into distances triangle matrix"""
    # Inner and outer loop both have number of iterations proportional to N, giving time complexity of O(N^2)
    # Final result is nested list structure with about (N^2)/2 elements, giving space complexity O(N^2)

    # Open file
    with open(filename) as distancesFile:
        # Extract lines of file
        lines = distancesFile.readlines()

        # For each line in file
        for i in range(len(lines)):

            # Add a list to nested DISTANCES list
            DISTANCES.append([])

            # Extract distance values from line
            line = [float(val) for val in lines[i].strip().split(",")]

            # For each line so far, plus one
            for j in range(i + 1):
                # Append distance value to DISTANCES nested list structure
                DISTANCES[i].append(line[j])
                j += 1


def distance(location_index_alpha, location_index_beta):
    """Use distance triangle matrix to calculate distance between two locations"""
    # Size of input does not vary (two integers) so space and time complexity are constant.
    try:
        return DISTANCES[location_index_alpha][location_index_beta]
    except IndexError:
        # If initial access triggers an IndexError, try access after swapping row index and column index
        return DISTANCES[location_index_beta][location_index_alpha]
