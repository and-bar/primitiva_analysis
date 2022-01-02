import numpy as np
# import sys
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

# print all elements of the array
# np.set_printoptions(threshold=sys.maxsize)

file_name = "historical data la primitiva 11_09_1999 -  30_12_2021.xlsx"
sheet = "numeros ganadores"
df_primitiva = pd.read_excel(io=file_name, sheet_name=sheet)

# get analysis of all bollas : number of ocurrencies over all period
n_of_bola = [1,2,3,4,5,6]
all_bolas = list()
for bola_int in n_of_bola:
    bola_column = np.array([element for element in df_primitiva["Bola"+str(bola_int)]])
    unique_bola, counts = np.unique(bola_column, return_counts=True)
    all_bolas.append(np.array(list(zip(unique_bola, counts))))

# plot result
fig = plt.figure(figsize=(15,7), dpi=150)
axes = fig.add_axes([0.1,0.1,0.8,0.8])

name_bola = 1
for bola in all_bolas:
    axes.scatter(bola[:,0], bola[:,1], label='bola'+str(name_bola))
    name_bola +=1

axes.legend(loc=5)
plt.xlabel('bola')
plt.ylabel('veces sacada en todo periodo')
plt.grid(visible= True, which= 'both', axis= 'both')
plt.xticks(list(range(1,50)))
# plt.savefig("all bolas analysis.png")
plt.show()

for_sorting_bolas = all_bolas.copy()

# sort numbers of columns in descending order of occurrences and take top numbers
top_occurrences_numbers = set()
for i in range(0,6):
    sorted_elements =  sorted(for_sorting_bolas[i], key= lambda column: column[1], reverse=True)
    numbers = np.array([[i[0], i[1]] for i in sorted_elements])
    # numbers[:3] here deep of the numbers of max occurrences
    top_occurrences_numbers.update(set(numbers[:2][:, 0]))

top_occurrences_numbers

all_combinations = [i for i in combinations(top_occurrences_numbers, 6)]
len(all_combinations)


#last gained combinations
last5_ndarray = df_primitiva[["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]][-100:].to_numpy()

asserted_numbers_from_combination = list()
for i in range(len(last5_ndarray)):
    asserted_numbers_from_combination.append(len(set.intersection(top_occurrences_numbers, set(last5_ndarray[i, :]))))

asserted_numbers_from_combination