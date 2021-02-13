import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities

    :param hist: list
    :return: list
    """

    return hist/np.sum(hist)


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width

    :param histo: list 
    :param width: float
    :return: float
    """
    m = np.sum(histo)
    w = width
    proba_histo = norm_histogram(histo)
    sum_proba_square = np.sum(proba_histo**2)
    J = 2/((m-1)*w) - (m+1)/((m-1)*w) * sum_proba_square

    return J
    


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    computed_Js = []
    for num_bin in range(min_bins, max_bins+1):
        histo = plt.hist(data, num_bin, (minimum, maximum))[0]
        width = (maximum-minimum)/num_bin
        J = compute_j(histo, width)
        computed_Js.append(J)

    return np.array(computed_Js)


def find_min(l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    arg_min = np.argmin(l)
    return l[arg_min], arg_min


if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
