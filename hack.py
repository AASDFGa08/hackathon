
from sys import maxsize 
from itertools import permutations
import json
import numpy as np
V = 21

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight) 
		
	return min_path 


input = open('level0.json')
data = json.load(input)
print(data)
distances = [neighborhood['distances'] for neighborhood in data['neighbourhoods'].values()]
two_d_array = np.array(distances)
print(two_d_array)
s=0
print(travellingSalesmanProblem(two_d_array, s))

