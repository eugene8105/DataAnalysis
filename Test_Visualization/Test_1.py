import pandas as pd
from matplotlib import pyplot as plt

'''
    Basic visualization with matplotlib library.
'''
'''x = [1, 2, 3]
y = [4, 5, 6]
z = [2, 3, 6]

plt.plot(x, y)
plt.plot(x, z)
plt.title("Test visual")
plt.xlabel("X visual")
plt.ylabel("Y visual")
plt.legend(["This is Y", "This is Z"])
plt.show()
'''

dt = pd.read_csv('countries.csv')

us = dt[dt.country == 'United States']
china = dt[dt.country == 'China']
# first value is X and second is Y
plt.plot(us.year, us.population / 10**6) # divided by millions
plt.plot(china.year, china.population / 10**6) # divided by millions
plt.title("Comparison a population")
plt.xlabel("Year")
plt.ylabel("Population in millions")
plt.legend(["US", "China"])

plt.show()

