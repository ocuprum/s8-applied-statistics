import numpy as np
import scipy.stats as stats
import scipy.special as special

rng = np.random.default_rng()
gen_sample = lambda n, lam: rng.exponential(scale=lam, size=n)
delta = lambda n, freqs, probs: np.sum((freqs ** 2) / (probs * n)) - n
empirical_cdf = lambda sample, t: sample[sample <= t].size / sample.size

def get_freq(sample, l, r=None):
    if r is None:
        return sample[l <= sample].size
    else:
        return sample[(l <= sample) & (sample < r)].size

def get_intervals(sample, r, lam=None):
    sample.sort()

    if lam is None:
        return np.array([i / r for i in range(r)])

    intervals = np.array([0])
    intervals = np.append(intervals, np.array([
        - np.log(1-i/r) / lam for i in range(1, r)
    ]))

    return intervals
    
def get_D(sample, dist, lam=None):
    size = sample.size
    sample.sort()
    maxs = np.zeros(size)
    for i in range(size):
        if dist == 'exp':
            cdf_val = stats.expon.cdf(x=sample[i], scale=lam)
        elif dist == 'uni':
            cdf_val = stats.uniform.cdf(x=sample[i])

        v1 = cdf_val - i / size
        v2 = (i + 1) / size - cdf_val
        maxs[i] = max(v1, v2)
    
    return np.max(maxs)
    


def kolmogorov_test(sample, gamma, dist, lam=None):
    z_gamma = special.kolmogi(gamma)
    D = get_D(sample, dist, lam)
    hypothesis = 0 if (sample.size ** 0.5) * D < z_gamma else 1

    return hypothesis


def chi2_test(sample, gamma, dist, lam=None):
    r = 3 * sample.size // 100
    z_gamma = stats.chi2.ppf(q=1-gamma, df=r-1)
    sample.sort()
    intervals = get_intervals(sample, r, lam)

    freqs = np.append(
        np.array(
        [get_freq(sample, intervals[i], intervals[i+1])
         for i in range(len(intervals)-1)]
        ),
        get_freq(sample, intervals[-1])
    )
       
    if dist == 'exp':
        Fs = stats.expon.cdf(intervals, scale=lam)
    
    elif dist == 'uni':
        Fs = stats.uniform.cdf(intervals)
    
    Fs = np.append(Fs, 1)
    probs = Fs[1:] - Fs[:-1]
    d = delta(sample.size, freqs, probs)

    hypothesis = 0 if d < z_gamma else 1
    
    return hypothesis


def empty_boxes_test(sample, gamma, dist=None, lam=None):
    ro = 2
    r = sample.size // ro
    z_gamma = stats.norm.ppf(1-gamma)
    exp = np.exp(-ro)

    intervals = [i / r for i in range(r+1)]
    freqs = np.array(
        [get_freq(sample, intervals[i], intervals[i+1])
         for i in range(len(intervals)-1)]
    )
  
    mu = freqs[freqs == 0].size
    crit = r * exp + z_gamma * np.sqrt(r * exp * (1 - (1 + ro) * exp))

    hypothesis = 0 if mu <= crit else 1

    return hypothesis


def smirnov_test(x_smpl, gamma, lam):
    z_gamma = special.kolmogi(gamma)

    n = x_smpl.size
    m = n // 2

    y_smpl = gen_sample(m, lam)

    x_smpl.sort()
    y_smpl.sort()

    D_pos = max([(k + 1) / m - empirical_cdf(x_smpl, t=y_smpl[k])
                 for k in range(m)])
    D_neg = max([empirical_cdf(x_smpl, t=y_smpl[k]) - k / m 
                 for k in range(m)])
    D = max(D_pos, D_neg)

    hypothesis = 0 if D <= z_gamma * np.sqrt(1/n + 1/m) else 1

    return hypothesis