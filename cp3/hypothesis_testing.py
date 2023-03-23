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

    crit = n / (1 + ro) + (n ** 0.5) * z_gamma * ro / ((1 + ro) ** 1.5)
    print('Count: {}'.format(eb_count))
    print('Crit: {}'.format(crit))
    hypothesis = 0 if eb_count <= crit else 1

    return hypothesis


def spearman_crit(X, Y, gamma):
    '''Гіпотеза незалежності - критерій Спірмена'''
    
    sorted_X = np.sort(X)
    n = X.size

    nums = np.array(range(1, n+1))
    stat_arr = np.array([Y[np.where(X == x)[0]] for x in sorted_X])
    stat_arr = stat_arr.reshape(stat_arr.shape[0])

    spearman_stat = 1 - (6 / (n * (n ** 2 -1))) * np.sum((nums-stat_arr) ** 2)

    z_gamma = stats.norm.ppf(1-gamma)
    crit = z_gamma / (n ** 0.5)

    print('Cov: \n{}'.format(np.cov(X, Y)))
    print('Spear Stat: {}'.format(spearman_stat))
    print('Crit: {}'.format(crit))

    hypothesis = 0 if abs(spearman_stat) < crit else 1

    return hypothesis


def kendall_crit(X, Y, gamma):
    '''Гіпотеза незалежності - критерій Кендалла'''

    sorted_X = np.sort(X)
    n = X.size

    stat_arr = np.array([Y[np.where(X == x)[0]] for x in sorted_X])
    stat_arr = stat_arr.reshape(stat_arr.shape[0])

    count = 0
    for i in range(n):
        test_arr = stat_arr[i+1:]
        count += test_arr[stat_arr[i] < test_arr].size
    kendall_stat = 4 * count / (n * (n-1)) - 1

    z_gamma = stats.norm.ppf(1-gamma)
    crit = 2 * z_gamma / (3 * (n ** 0.5))

    print('Kend Stat: {}'.format(kendall_stat))
    print('Crit: {}'.format(crit))

    hypothesis = 0 if abs(kendall_stat) < crit else 1

    return hypothesis


def inversions_crit(X, gamma):
    '''Гіпотеза випадковості'''

    n = X.size

    invers_stat = 0
    for i in range(n):
        test_arr = X[i+1:]
        invers_stat += test_arr[X[i] > test_arr].size

    z_gamma = stats.norm.ppf(1-gamma)
    norm_stat = 6 / (n * (n ** 0.5)) * abs(invers_stat - n * (n-1) / 4)

    hypothesis = 0 if norm_stat <= z_gamma else 1

    return hypothesis