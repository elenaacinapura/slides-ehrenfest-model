# %%
from matplotlib import pyplot as plt
from scipy.stats import binom
import numpy as np
from matplotlib import rcParams
import matplotlib.font_manager as font_manager

font_dirs = ['/home/elena/.fonts', ]
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)

rcParams['font.family'] = 'Fira Sans'
rcParams['font.weight'] = 'light'
plt.rc("axes", labelweight="light")
rcParams['font.size'] = 18
N = 10
p = 0.5

x = [i for i in range(N+1)]
binss = [i-0.5 for i in range(N+2)]

plt.figure('visit_frequency')
plt.hist(x, bins=binss, weights=binom.pmf(x, N, p), color='firebrick', alpha=0.8, ls='solid', ec='k')
plt.xticks([0, 2, 4, 6, 8, 10])
plt.xlabel('State')
plt.ylabel('Probability', labelpad=10)
plt.tight_layout()
# plt.show()
plt.savefig('../pictures/binomial.pdf', format='pdf', transparent=True)

plt.figure('mean_rec_time')
plt.hist(x, bins=binss, weights=1.0/binom.pmf(x, N, p), color='firebrick', alpha=0.8, ls='solid', ec='k')
plt.xticks([0, 2, 4, 6, 8, 10])
plt.xlabel('State')
plt.ylabel('Time', labelpad=10)
plt.tight_layout()
# plt.show()
plt.savefig('../pictures/mean_recurrence.pdf', format='pdf', transparent=True)
# %%
