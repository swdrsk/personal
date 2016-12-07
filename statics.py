import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# data generate
x = np.random.normal(0,10,size=100)
y = np.random.normal(5,10,size=100)

# visualize
bins = np.linspace(-40,50,18)
plt.hist(x,bins,alpha=0.5)
plt.hist(y,bins,alpha=0.5)

# hypothesis test
result = stats.mannwhitneyu(x,y)
print(result.pvalue)

plt.show()