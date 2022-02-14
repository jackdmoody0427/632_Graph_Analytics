#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:10:12 2022

@author: jackmoody
"""
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import networkx as nx


G =  nx.read_graphml("/Users/jackmoody/Desktop/Spring 2022 JHU/graphs/data/students/students.graphml")

#Start with finding the histogram of degrees “students.graphml” and plot it
# def of degree = the number of edges attached to each vertex
hist = nx.degree_histogram(G)
#print(hist)
xs = range(len(hist))
plt.scatter(xs, hist)
plt.xlabel('degree')
plt.ylabel('counts')
plt.title('histogram degree vs counts')

'''
TRIAL WORK
# Calculate the average degree (bar k)
avg_deg = nx.average_degree_connectivity(G)
print("average degree trial 1:\n",avg_deg)
#another way of trying to get average degree
print("average degree trial 2 from nx.info:\n",nx.info(G))
'''

#Calculate average degree (bar k)
N,K = G.order(),G.size()
avg_deg = float(K)/N
print("Nodes: ", N)
print("Edges: ", K)
print("Average degree: ", avg_deg)

#Plot the probability of a vertex having a degree greater than or equal to k 
#as a function of k:
    
#What is the probability that a node in this graph has larger than 
#average degree ?
l = []
degrees = [val for (node, val) in G.degree()]
for i in degrees:
    if i > avg_deg:
        l.append(i)
print(l)
prob_bigger = np.array(l)/N
print(prob_bigger)

'''
degree_freq = nx.degree_histogram(G)
degrees = range(len(degree_freq))
plt.figure(figsize=(12, 8)) 
plt.loglog(degrees[m:], degree_freq[m:],'go-') 
plt.xlabel('Degree')
plt.ylabel('Frequency')
'''