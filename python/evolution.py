from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
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
rcParams['font.size'] = 26

########################################
# Read data
########################################
# Limiting distribution
data = pd.read_csv('limiting_dist.csv', delimiter='\t')
i = data['i']
limiting_dist = data['val']

N = len(i)
b = [i for i in range(N)]

# Sampling distribution
visit_freq = []
for j in range(4):
    data = pd.read_csv('visit_freq_{}.csv'.format(j), delimiter='\t')
    visit_freq.append(data['val'])

    plt.figure()
    plt.hist(i[:N], bins=b, weights=limiting_dist, label='Limiting distribution', color='b', alpha=0.5, ec='k')
    plt.hist(i[:N], bins=b, weights=visit_freq[j], label='Sample visit frequency',alpha=0.5, ls='dashed', density=1, color='r', ec='k')
    plt.xlabel('State')
    plt.ylabel('Probability')
    # plt.legend(bbox_to_anchor=(0.83, -0.18))
    plt.tight_layout()
    # plt.show()
    plt.savefig('../pictures/evolution_{}.pdf'.format(j), format='pdf')

