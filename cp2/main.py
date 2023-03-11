import show 
import scipy.stats as stats
import hypothesis_testing as ht

task = int(input('Введіть номер завдання: '))

N = [1000, 10000, 100000]
lam1, lam2 = 1, 1.3
gamma = 0.05

while task in [1, 2, 3, 4]:
    if task == 1:
        show.show_pht(ht.kolmogorov_test, N, lam1, lam2, gamma)
        show.show_pht(ht.kolmogorov_test, N, lam1, lam1, gamma)

    elif task == 2:
        show.show_pht(ht.chi2_test, N, lam1, lam2, gamma)
        show.show_pht(ht.chi2_test, N, lam1, lam1, gamma)

    elif task == 3:
        show.show_pht(ht.empty_boxes_test, N, lam1, lam2, gamma)
        show.show_pht(ht.empty_boxes_test, N, lam1, lam1, gamma)

    elif task == 4:
        show.show_hht(N, lam1, lam2, lam1, gamma)
        show.show_hht(N, lam1, lam1, lam1, gamma)

    task = int(input('Введіть номер завдання: '))