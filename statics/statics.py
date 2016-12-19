import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import time

def mannwhitneyu():
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

def median():
    x = np.random.normal(10,100,size=200001)
    start = time.time()
    ave = np.average(x)
    end = time.time() - start
    print('average:%f, time:%f'%(ave, end))

    start = time.time()
    x.sort()
    med = x[100000]
    end = time.time() - start
    print('median:%f, time:%f'%(med, end))


if __name__=="__main__":
    median()
