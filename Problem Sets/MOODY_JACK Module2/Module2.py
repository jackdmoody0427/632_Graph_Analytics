#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 14:32:03 2022

@author: jackmoody
"""


import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import networkx as nx

# Build a simple matrix:
    
G =  nx.read_graphml("/Users/jackmoody/Desktop/Spring 2022 JHU/graphs/data/students/students.graphml")
#print(A)


###  Laplacian matrix :
    
L = nx.laplacian_matrix(G.to_undirected())

Ld=L.todense()

###  Visualize and save the laplacian matrix:
    
plt.imshow(Ld)
plt.colorbar()
#plt.savefig("/Users/jackmoody/Desktop/l.png", format="png")
plt.show()

###  Calculate eigenvalues of adjacency matrix :
    
eigenvalues, eigenvectors = linalg.eig(Ld)
print(len(eigenvalues))

with open("/Users/jackmoody/Desktop/results.txt",'w') as f:
    for i in range(len(eigenvalues)):
        f.write("\nEigenvalue: "+ str(eigenvalues[i]))

