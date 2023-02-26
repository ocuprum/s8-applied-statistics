import numpy as np
import scipy.stats as stats
from conf_interval import sample_mean

rng = np.random.default_rng()
gen_exp_sample = lambda m: rng.exponential(scale=1, size=m)

def sample_var(estimations, est_mean=False):
    n = estimations.size
    if est_mean is False:
        est_mean = sample_mean(estimations)
     
    smpl_var = (np.sum(estimations ** 2) - n * (est_mean ** 2)) / (n-1)
    return smpl_var

# METHODS
def monte_carlo(m, n):
    eta = 1 / rng.uniform(low=0, high=1, size=n) - 1
    exp_smpl_sums = [np.sum(gen_exp_sample(m)) for _ in range(n)]
    ests = eta > exp_smpl_sums

    return ests.astype('int')
    
def second_method(m, n):
    smpl_sums = np.ones(n)
    add_exp_smpl = np.vectorize(lambda num: num + np.sum(gen_exp_sample(m)))
    smpl_sums = add_exp_smpl(smpl_sums)

    return 1 / smpl_sums 

def m_bigger_than_one_method(m, n):
    if m == 1: return False
    exp_sums = np.array([np.sum(gen_exp_sample(m-1)) for _ in range(n)])

    return (exp_sums / (1 + exp_sums)) / (m-1)

# DEFINE SAMPLE SIZE
def sample_size(method, m, n, epsilon, z_gamma=False, gamma=False):
    if method is m_bigger_than_one_method and m == 1: return False

    if z_gamma is False:
        z_gamma = stats.norm.ppf(q=1-gamma/2)

    ests = method(m, n)
    smpl_mean = sample_mean(ests)
    smpl_var = sample_var(ests, smpl_mean)
    
    val = lambda a, b: (pow(z_gamma, 2) * b) / (pow(epsilon, 2) * pow(a, 2))
    new_val = val(smpl_mean, smpl_var)

    if n > new_val: 
        return n

    return int(new_val) + 1