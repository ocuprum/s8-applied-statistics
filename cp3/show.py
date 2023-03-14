import numpy as np
import time
import scipy.stats as stats
import hypothesis_testing as ht


def show_homogeneity(N, M, gamma, xlam, ylam):
    print('-' * 25)
    print('КРИТЕРІЙ ПУСТИХ БЛОКІВ\n')
    if len(N) != len(M):
        return False
    
    for i in range(len(N)):
        print(' * Розмір вибірки X: {}'.format(N[i]))
        print('   Параметр = {}'.format(xlam))
        print(' * Розмір вибірки Y: {}'.format(M[i]))
        print('   Параметр = {}'.format(ylam))
        X = stats.expon(xlam).rvs(size=N[i])
        Y = stats.expon(ylam).rvs(size=M[i])
        print('Результат -> гіпотеза {}\n'.format(ht.empty_blocks(X, Y, gamma)))
    print()



def show_independence(crit, N, gamma):
    print('-' * 25)
    
    if crit == 'spearman':
        crit = ht.spearman_crit
        print('КРИТЕРІЙ СПІРМЕНА\n')
    elif crit == 'kendall':
        crit = ht.kendall_crit
        print('КРИТЕРІЙ КЕНДАЛЛА\n')


    for n in N:
        print(' * Розмір вибірки: {}'.format(n))

        X = stats.uniform(0, 1).rvs(size=n)

        eta = stats.uniform(-1, 1).rvs(size=n)
        print('1) Y - сума в.в.')
        Y = X * eta
        print('Результат -> гіпотеза {}\n'.format(crit(X, Y, gamma)))

        print('2) Y - добуток в.в.')
        Y = X + eta
        print('Результат -> гіпотеза {}\n\n'.format(crit(X, Y, gamma)))    



def show_randomness(N, gamma):
    print('-' * 25)
    print('КРИТЕРІЙ ВИПАДКОВОСТІ\n')

    for n in N:
        print(' * Розмір вибірки: {}'.format(n))

        uni_sample = stats.uniform(-1, 1).rvs(size=n)
        X = np.array([np.sum(uni_sample[:i-1]) / i for i in range(1, n+1)])
        #X = np.array([np.sum(stats.uniform(-1, 1).rvs(size=i)) / i for i in range(1, n+1)])
        print('Результат -> гіпотеза {}\n'.format(ht.inversions_crit(X, gamma)))  