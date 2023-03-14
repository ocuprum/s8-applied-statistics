import numpy as np
import scipy.stats as stats

is_empty_block = lambda Y, l, r: int(Y[(l < Y) & (Y <= r)].size == 0)

def empty_blocks(X, Y, gamma):
    '''Критерій однорідності - критерій пустих блоків'''

    X.sort()
    n, m = X.size, Y.size

    eb_count = is_empty_block(Y, l=-np.inf, r=X[0])
    for i in range(n-1):
        eb_count += is_empty_block(Y, X[i], X[i+1])
    eb_count += is_empty_block(Y, l=X[-1], r=np.inf)

    z_gamma = stats.norm.ppf(1-gamma)
    ro = m // n

    criteria = n / (1 + ro) + (n ** 0.5) * z_gamma * ro / ((1 + ro) ** 1.5)
    hypothesis = 0 if eb_count <= criteria else 1

    return hypothesis

def spearman_criteria(X, Y, gamma):
    '''Гіпотеза незалежності - критерій Спірмена'''
    
    sorted_X = np.sort(X)
    n = X.size

    nums = np.array(range(1, n+1))
    stat_arr = np.array([Y[np.where(X == x)[0]] for x in sorted_X])
    stat_arr = stat_arr.reshape(stat_arr.shape[0])

    spearman_stat = 1 - (6 / (n * (n ** 2 -1))) * np.sum((nums-stat_arr) ** 2)

    z_gamma = stats.norm.ppf(1-gamma)
    criteria = z_gamma / (n ** 0.5)

    hypothesis = 0 if abs(spearman_stat) < criteria else 1

    return hypothesis


def kendall_criteria():
    '''Гіпотеза незалежності - критерій Кендалла'''
    pass



def inversions_criteria():
    '''Гіпотеза випадковості'''
    pass