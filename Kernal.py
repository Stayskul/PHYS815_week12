import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

#takes a .txt file, reads it, and makes a list
if __name__ == "__main__":
    
    haveH1 = False
    

    if '-input' in sys.argv:
        p = sys.argv.index('-input')
        InputFile = sys.argv[p+1]
        haveH1 = True


    if haveH1:
        with open(InputFile, "r") as f:
            myArray = f.read().split()

        for i in range(0, len(myArray)):
            myArray[i] = float(myArray[i])
    
    def myArr():

        x=[]
        data=myArray
        x=np.concatenate((x,data))

        return x
    x_train=myArr()[:, np.newaxis]
    x_test = np.linspace(0, 400, 2000)[:, np.newaxis]

    bandwidth = np.arange(0.1, 8, .1)
    kde = KernelDensity(kernel='gaussian')
    grid = GridSearchCV(kde, {'bandwidth': bandwidth})
    grid.fit(x_train)

    kde = grid.best_estimator_
    log_dens = kde.score_samples(x_test)
    
    
    plt.fill(x_test, np.exp(log_dens), c='blue', alpha=0.5)

    plt.hist(myArray, 50, facecolor='green', alpha=0.55, density=True)
    plt.show()
    print("optimal bandwidth: " + "{:.2f}".format(kde.bandwidth))
