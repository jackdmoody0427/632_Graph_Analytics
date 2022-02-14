#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 17:45:48 2022

@author: jackmoody
"""

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_edgelist("/Users/jackmoody/Desktop/web-Google.txt")

print(nx.info(G))

F = nx.draw(G)
plt.show(F)