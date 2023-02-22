import conf_interval as ci
import numpy as np

n, gamma = 1000, 0.01
sample = ci.gen_sample(n)

print('Mean:{}\nVariance:{}\n'.format(np.mean(sample), np.var(sample)))
print(ci.mean_conf_interval_unknown_var(sample, gamma))
print(ci.var_conf_interval(sample, gamma))
print(ci.mean_conf_interval_unknown_dist(sample, gamma))