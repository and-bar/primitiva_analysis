import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt

# print all elements of the array
# np.set_printoptions(threshold=sys.maxsize)

file_name = "historical data la primitiva 11_09_1999 -  30_12_2021.xlsx"
sheet = "numeros ganadores"
df_primitiva = pd.read_excel(io=file_name, sheet_name=sheet)

# # analysis of bola1
# bola1 = np.array([element for element in df_primitiva["Bola1"]])
# unique_bola1, counts = np.unique(bola1, return_counts=True)
# numbers_bola1 = np.array(list(zip(unique_bola1, counts)))
# numbers_bola1.shape


# plt.figure(figsize=(15,7))
# plt.grid(visible= True, which= 'both', axis= 'both')
# plt.xticks(numbers_bola1[:,0])
# plt.scatter(numbers_bola1[:,0],numbers_bola1[:,1])
# plt.xlabel('bola')
# plt.ylabel('veces sacada en todo periodo')
# plt.title('Bola n1')
# # plt.savefig("bola1 analysis.png")
# plt.show()

# get analysis of all bollas : number of ocurrencies over all period
n_of_bola = [1,2,3,4,5,6]
all_bolas = list()
for bola_int in n_of_bola:
    bola_column = np.array([element for element in df_primitiva["Bola"+str(bola_int)]])
    unique_bola, counts = np.unique(bola_column, return_counts=True)
    all_bolas.append(np.array(list(zip(unique_bola, counts))))

# plt.figure(figsize=(15,7))
# plt.grid(visible= True, which= 'both', axis= 'both')

# for bola in all_bolas:
#     plt.scatter(bola[:,0], bola[:,1])

# plt.xticks(numbers_bola1[:,0])
# plt.xlabel('bola')
# plt.ylabel('veces sacada en todo periodo')
# plt.title('Bola n1')
# # plt.savefig("bola1 analysis.png")
# plt.show()


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
plt.savefig("all bolas analysis.png")
plt.show()

