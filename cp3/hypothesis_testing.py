import numpy as np
import scipy.stats as stats

def is_empty_block(Y, l=None, r=None):
    if l is None:
        return int(Y[Y <= r].size == 0)
    elif r is None:
        return int(Y[l < Y].size == 0)
    else:
        return int(Y[(l < Y) & (Y <= r)].size == 0)

def empty_blocks(X, Y, gamma):
    '''Критерій однорідності - критерій пустих блоків'''

    X.sort()
    n, m = X.size, Y.size

    eb_count = is_empty_block(Y, r=X[0])
    for i in range(n-1):
        eb_count += is_empty_block(Y, X[i], X[i+1])
    eb_count += is_empty_block(Y, l=X[-1])

    z_gamma = stats.norm.ppf(1-gamma)
    ro = m // n

    criteria = n / (1 + ro) + (n ** 0.5) * z_gamma * ro / ((1 + ro) ** 1.5)
    hypothesis = 0 if eb_count <= criteria else 1

    return hypothesis

def spearman_criteria():
    '''Гіпотеза незалежності - критерій Спірмена'''
    pass


def kendall_criteria():
    '''Гіпотеза незалежності - критерій Кендалла'''
    pass



def inversions_criteria():
    '''Гіпотеза випадковості'''
    pass