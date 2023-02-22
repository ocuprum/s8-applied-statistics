import conf_interval as ci

n, gamma = 1000, 0.01
sample = ci.gen_sample(n)
#print(ci.mean_conf_interval_unknown_var(sample, n, gamma))
print(ci.var_conf_interval(sample, n, gamma))