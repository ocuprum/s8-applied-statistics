import numpy as np
import scipy.stats as stats

rng = np.random.default_rng()
gen_sample = lambda n: [rng.normal(0, 1) for _ in range(n)]
sample_mean = lambda sample: sum(sample) / len(sample)

def sample_var(sample, mean=False):
    n = len(sample)
    if mean is False:
        mean = sample_mean(sample)
    sample = np.array(sample) - mean
    result = np.sum(sample ** 2)

    return result / n


def mean_conf_interval_unknown_var(sample, gamma):
    n = len(sample)

    smpl_mean = sample_mean(sample)
    var_sq = sample_var(sample, smpl_mean) ** 0.5

    z_gamma = stats.t.ppf(q=1-gamma / 2, df=n-1)
    val = z_gamma * (var_sq ** 0.5) / ((n - 1) ** 0.5)
    
    return smpl_mean - val, smpl_mean + val

def mean_conf_interval_unknown_dist(sample, gamma):
    n = len(sample)

    smpl_mean = sample_mean(sample)
    smpl_var = sample_var(sample, smpl_mean)

    z_gamma = stats.norm.ppf(q=1-gamma / 2)
    val = z_gamma * (smpl_var ** 0.5) / (n ** 0.5)

    return smpl_mean - val, smpl_mean + val

def var_conf_interval(sample, gamma):
    n = len(sample)
    smpl_var = sample_var(sample)
    val = n * smpl_var

    z1 = stats.chi2.ppf(q=1-gamma / 2, df=n-1)
    z2 = stats.chi2.ppf(q=gamma / 2, df=n-1)
    if z1 >= z2: z1, z2 = z2, z1

    return val / z2, val / z1