import numpy as np
import scipy.stats as stats

rng = np.random.default_rng()
gen_sample = lambda n: [rng.normal(0, 1) for _ in range(n)]
sample_mean = lambda n, sample: sum(sample) / n

def sample_var(n, sample, mean=False):
    if mean is False:
        mean = sample_mean(n, sample)
    sample = np.array(sample) - mean
    result = sum([el ** 2 for el in sample])

    return result / n

def mean_conf_interval_unknown_var(sample, n, gamma):
    mean = sample_mean(n, sample)
    var_sq = sample_var(n, sample, mean) ** 0.5

    z_gamma = stats.t.ppf(q=(1-gamma / 2), df=n-1)
    val = z_gamma * (var_sq ** 0.5) / ((n - 1) ** 0.5)
    
    return mean - val, mean + val

def conf_interval_unknown_dist():
    pass

def var_conf_interval(sample, n, gamma):
    var = sample_var(n, sample)
    print(var ** 0.5)
    val = n * var

    z1 = stats.chi2.ppf(q=1-gamma / 2, df=n-1)
    z2 = stats.chi2.ppf(q=gamma / 2, df=n-1)
    if z1 >= z2: z1, z2 = z2, z1

    return val / z2, val / z1