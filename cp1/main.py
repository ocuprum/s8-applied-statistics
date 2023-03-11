import show
import probability_calc as pc

task = int(input('Введіть номер завдання: '))

while task in [1, 2]:
    if task == 1:
        gamma = 0.01
        N = [10000000]
        show.show_ci(gamma, N)

    elif task == 2:
        gamma = 0.01
        z_gamma = 2.575
        epsilon = 0.01
        
        M = [1, 10, 100]
        n1 = 1500
        show.show_pc(pc.monte_carlo, M, n1, epsilon, 'Монте-Карло', z_gamma, gamma)

        M = [1, 10, 100, 1000]
        n1 = 50
        show.show_pc(pc.second_method, M, n1, epsilon, '2', z_gamma, gamma)

        M = [10, 100]
        n1 = 50
        show.show_pc(pc.m_bigger_than_one_method, M, n1, epsilon, 'для m > 1', z_gamma, gamma)

    task = int(input('Введіть номер завдання: '))