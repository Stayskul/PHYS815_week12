# PHYS815_week12
contains homework for week 12


This homework contains code from the following:

My own repositories

https://stackabuse.com/kernel-density-estimation-in-python-using-scikit-learn/


To run this code:

1. place random.py in a folder and specify its location in the kernel.py program

2. Generate some data, thrown according to a lognormal distribution: python3 Datagen.py -mux ? -sigx ? -Nmeas 1000 > Data.txt

2. Simply run Kernel.py
    python3 Kernal.py -Input Data.txt
    
    This will display the optimized model (from kernel denstiy estimation), with the actual data histogram
    It will also tell you the optimal value of the "Bandwidth" parameter
