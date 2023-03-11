import conf_interval as ci
import probability_calc as pc

def show_ci(gamma: float, N: list):
    for n in N:
        print('\nКількість реалізацій: {}'.format(n))

        sample = ci.gen_sample(n)
        smpl_mean, smpl_var = ci.sample_mean(sample), ci.sample_var(sample)
        print('Вибіркове середнє: {}\nВибіркова дисперсія: {}\n'.format(smpl_mean, smpl_var))
        
        print('Довірчий інтервал:')
        ci1 = ci.mean_conf_interval_unknown_var(sample, gamma)
        print('* для мат.сподівання/ дисперсія невідома/ нормальний розподіл: {}'.format(ci1))
        print('     довжина інтервалу: {}'.format(ci1[1] - ci1[0]))
        ci2 = ci.mean_conf_interval_unknown_dist(sample, gamma)
        print('* для мат.сподівання/ розподіл невідомий: {}'.format(ci2))
        print('     довжина інтервалу: {}'.format(ci2[1] - ci2[0]))
        ci3 = ci.var_conf_interval(sample, gamma)
        print('* для дисперсії/ нормальний розподіл: {}'.format(ci3))
        print('     довжина інтервалу: {}'.format(ci3[1] - ci3[0]))
        print('-' * 110)

def show_pc(method, M, n0, epsilon, method_name, z_gamma: False, gamma: False):
    print('\n---МЕТОД: {}---'.format(method_name))
    for m in M:
        print('\n   M = {}'.format(m))
        n = pc.sample_size(method, m, n0, epsilon, z_gamma, gamma)
        ests = method(m, n)
        smpl_prob = pc.sample_mean(ests)
        smpl_var = pc.sample_var(ests)
        conf_int_mean = ci.mean_conf_interval_unknown_dist(ests, gamma)
        conf_int_var = ci.var_conf_interval(ests, gamma)
        print('* оцінка ймовірності: {}'.format(smpl_prob))
        print('* вибіркова дисперсія: {}'.format(smpl_var))
        print('* довірчий інтервал для мат.сподівання: {}'.format(conf_int_mean))
        print('* довірчий інтервал для дисперсії: {}'.format(conf_int_var))
        print('* кількість виконаних реалізацій: {}'.format(n))
    print('-' * 80)