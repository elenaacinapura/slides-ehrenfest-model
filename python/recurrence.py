from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os
from matplotlib import rcParams
import matplotlib.font_manager as font_manager

############################################
# Set custom fonts
############################################
font_dirs = ['/home/elena/.fonts', ]
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)
rcParams['font.family'] = 'Fira Sans'
rcParams['font.weight'] = 'light'
plt.rc("axes", labelweight="light")
rcParams['font.size'] = 24

theo = []
sample = []

text = [r'$N = 10$', r'$N = 15$', r'$N = 20$', r'$N = 30$']
x = [4, 6, 8, 12]
y = [7e2, 2e4, 5e5, 4e8]

for j in range(4):
    data = pd.read_csv('recurrence_time_th_{}.csv'.format(j), delimiter='\t')
    i = data['i']
    N = len(i)
    b = [i for i in range(N)]
    theo.append(data['val'])
    data = pd.read_csv('recurrence_time_sampled_{}.csv'.format(j), delimiter='\t')
    sample.append(data['val'])

    plt.figure()
    plt.plot(b, theo[j], '.', label='Prediction', color='royalblue', marker='X', markersize=15)
    plt.plot(b, sample[j], '.', label='Simulation', color='red', marker='.', markersize=15)
    plt.xlabel('State')
    plt.ylabel('Time steps')
    plt.yscale('log')
    plt.text(x[j], y[j], text[j], size=20)
    plt.tight_layout()
    # plt.show()
    plt.savefig('../pictures/recurrence_{}.pdf'.format(j), format='pdf', transparent=True)

