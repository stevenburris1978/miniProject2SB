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

data = pd.read_csv('SofwareDeveloperIncomeExpensesperUSACity.csv', index_col='Metro')

print (data['Mean Software Developer Salary (adjusted)'])

goodSalaries = np.array(data['Mean Software Developer Salary (adjusted)'])
print(goodSalaries)

bestSalaries = [i for i in goodSalaries if i > 100000]
print(bestSalaries)

days = list(range(1, len(bestSalaries) + 1))

plt.plot(days, bestSalaries, 'red')
plt.plot(days, bestSalaries, 'o')

salaries = bestSalaries
salaries.sort()
lowPrice = salaries[0]
highPrice = salaries[-1]

plt.axis([1, 50, lowPrice - 1, highPrice + 1])

plt.title('Best Software Salaries')
plt.xlabel('Cities')
plt.ylabel('Salary')

# code to create charts folder if there is not one already
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

# auto save png pics to folder with stock name
savefile = "charts/" + "chart1.png"
plt.savefig(savefile)
plt.show()



