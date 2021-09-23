import pandas as pd
from matplotlib import pyplot as plt


def calc_population(population):
    return population / 10 ** 6


sample = pd.read_csv("countries.csv")
afghan = sample[sample.country == "Afghanistan"]
us = sample[sample.country == "United States"]
china = sample[sample.country == "China"]
plt.plot(afghan.year, calc_population(afghan.population))
plt.plot(us.year, calc_population(us.population))
plt.plot(china.year, calc_population(china.population))
plt.xlabel("year")
plt.ylabel("population, mln")
plt.legend(["Afghanistan", "US", "China"])
plt.show()
