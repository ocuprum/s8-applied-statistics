import scipy.stats as stats
import hypothesis_testing as ht


def show_homogeneity(N, M, gamma):
    print('-' * 30)
    xlam, ylam = 1, 1.2
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


def show_independence(criteria, N, gamma):
    pass



def show_randomness():
    pass