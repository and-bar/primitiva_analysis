import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt

# print all elements of the array
np.set_printoptions(threshold=sys.maxsize)

file_name = "historical data la primitiva 11_09_1999 -  30_12_2021.xlsx"
sheet = "numeros ganadores"
df_primitiva = pd.read_excel(io=file_name, sheet_name=sheet)

bola1 = np.array([element for element in df_primitiva["Bola1"]])
unique_bola1, counts = np.unique(bola1, return_counts=True)
numbers_bola1 = np.array(list(zip(unique_bola1, counts)))
numbers_bola1.shape


plt.figure(figsize=(15,7))
plt.grid(visible= True, which= 'both', axis= 'both')
plt.xticks(numbers_bola1[:,0])
# plt.plot(numbers_bola1[:,0],numbers_bola1[:,1], linewidth=5, markersize=12)
plt.scatter(numbers_bola1[:,0],numbers_bola1[:,1])
plt.xlabel('bola')
plt.ylabel('veces sacada en todo periodo')
plt.title('Bola n1')
plt.show()
