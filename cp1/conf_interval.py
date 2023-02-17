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

def conf_interval_unknown_var(sample, n, gamma):
    mean = sample_mean(n, sample)
    var_sq = sample_var(n, sample, mean) ** 0.5
    print(mean, sample_var(n, sample, mean))

    z_gamma = stats.t.ppf(q=(1-gamma / 2), df=n-1)
    val = z_gamma * (var_sq ** 0.5) / ((n - 1) ** 0.5)
    
    return mean - val, mean + val

def conf_interval_unknown_dist():
    pass

def conf_interval_unknown_mean():
    pass