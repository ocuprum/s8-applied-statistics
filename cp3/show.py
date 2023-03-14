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



def show_independence(criteria, N, gamma):
    print('-' * 25)
    
    if criteria == 'spearman':
        criteria = ht.spearman_criteria
        print('КРИТЕРІЙ СПІРМЕНА\n')
    elif criteria == 'kendall':
        criteria = ht.kendall_criteria
        print('КРИТЕРІЙ КЕНДАЛЛА\n')


    for n in N:
        print(' * Розмір вибірки: {}'.format(n))

        X = stats.uniform(0, 1).rvs(size=n)

        eta = stats.uniform(-1, 1).rvs(size=n)
        print('1) Y - сума в.в.')
        Y = X * eta
        print('Результат -> гіпотеза {}\n'.format(criteria(X, Y, gamma)))

        print('2) Y - добуток в.в.')
        Y = X + eta
        print('Результат -> гіпотеза {}\n\n'.format(criteria(X, Y, gamma )))    



def show_randomness():
    pass