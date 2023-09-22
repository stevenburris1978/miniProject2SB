# INF601VA - Advanced Programming in Python
# Steven Burris
# 09-20-2023
# *Mini Project 2SB*
# put api url here

import pprint
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

# get pandas data frame of Software developer Salaries in US Cities
data = pd.read_csv('SofwareDeveloperIncomeExpensesperUSACity.csv', index_col='Metro')

print (data['Mean Software Developer Salary (adjusted)'])

# get salaries
goodSalaries = np.array(data['Mean Software Developer Salary (adjusted)'])
print(goodSalaries)

# get salaries over $100,000
bestSalaries = [i for i in goodSalaries if i > 100000]
print(bestSalaries)

# List salaries
salary = list(range(1, len(bestSalaries) + 1))

# This plots the graph
plt.plot(salary, bestSalaries, 'red')
plt.plot(salary, bestSalaries, 'o')

# Get our min and max for Y
salaries = bestSalaries
salaries.sort()
lowPrice = salaries[0]
highPrice = salaries[-1]

# Set X, Y axis min and max
# form [xmin, xmax, ymin, ymax]
plt.axis([0, 45, lowPrice-1000, highPrice+1000])

plt.title('Best Software Developer Salaries')
plt.xlabel('Number of Cities With Salaries over 100,000')
plt.ylabel('Salaries over 100,000')

# code to create charts folder if there is not one already
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

# auto save png pics to folder with stock name
savefile = "charts/" + "chart1.png"
plt.savefig(savefile)
plt.show()





