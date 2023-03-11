import numpy as np
import scipy.stats as stats
import hypothesis_testing as ht

def show_pht(test, N: list, real_lam: float, test_lam: float, gamma: float):
    print('-' * 25)
    print('  Дійсний параметр: {}'.format(real_lam))
    print('  H0 - Тестовий параметр: {}'.format(test_lam))
    print()
    for n in N:
        print('* Розмір вибірки: {}'.format(n))

        exp_sample = ht.gen_sample(n, real_lam)
        uniform_sample = np.exp(-test_lam * exp_sample)

        if test is ht.empty_boxes_test:
            exp_sample = np.exp(-test_lam * exp_sample)
        print(' EXPONENTIAL: Результат -> гіпотеза {}'.format(test(sample=exp_sample, gamma=gamma,
                                                                     dist='exp', lam=test_lam)))

        print(' UNIFORM: Результат -> гіпотеза {}\n'.format(test(sample=uniform_sample, gamma=gamma,
                                                                 dist='uni')))


def show_hht(N: list, x_real_lam: float, y_real_lam: float, test_lam: float, gamma: float):
    print('-' * 25)
    print(' Дійсні параметри: X -> {}, Y -> {}'.format(x_real_lam, y_real_lam))
    print('  H0 - Тестовий параметр: {}'.format(test_lam))
    print()
    for n in N:
        print('* Розмір вибірки: {}'.format(n))

        x_sample = ht.gen_sample(n, x_real_lam)
        print('Результат -> гіпотеза {}\n'.format(ht.smirnov_test(x_smpl=x_sample, gamma=gamma,
                                                                lam=y_real_lam)))