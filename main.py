# INF601VA - Advanced Programming in Python
# Steven Burris
# 09-20-2023
# *Mini Project 2SB*
# put api url here

import pprint
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pathlib import Path

try:
    Path("charts").mkdir()
except FileExistsError:
    pass