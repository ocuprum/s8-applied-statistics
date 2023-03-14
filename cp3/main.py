import show
import numpy as np 
import hypothesis_testing as ht 

gamma = 0.05
N = [500, 5000, 50000]
M = [1000, 10000, 100000]

print('1 - Критерій пустих блоків')
print('2 - Критерій Спірмена')
print('3 - Критерій Кендалла')
print('4 - Критерій випадковості\n')

task = int(input('Введіть номер завдання: '))

if task == 1:
    xlam, ylam = 1, 1.2
    show.show_homogeneity(N, M, gamma, xlam, ylam)

elif task == 2:
    show.show_independence('spearman', N, gamma)
    #show.show_independence()

elif task == 3:
    pass

elif task == 4: 
    pass


