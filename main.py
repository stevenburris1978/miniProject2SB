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

#code to create charts folder if there is not one already
try:
    Path("charts").mkdir()
except FileExistsError:
    pass