"""
"La primitiva" - estadistics of numbers

https://es.wikipedia.org/wiki/Loter%C3%ADa_Primitiva_de_Espa%C3%B1a#:~:text=La%20Loter%C3%ADa%20Primitiva%20es%20un,bombo%20con%2049%20n%C3%BAmeros%20(modalidad
Rules: 
    
    realización de una apuesta basada en 6 números de entre los 49 posibles, 
    a los que se añade un séptimo número de reintegro del 0 al 9 elegido 
    aleatoriamente por el terminal electrónico al validar la apuesta.
    El precio de la participación es fijo para un sorteo determinado de 1 €.
    En el sorteo se extraen los 6 números que formarán la combinación ganadora,
    y adicionalmente se extrae un séptimo número denominado "complementario"
    Después, de un bombo aparte se extrae otra bola correspondiente al reintegro.
    
    Existen varias categorías de acertantes dependiendo de los números que se 
    aciertan.

    Categoría Especial: Acertar los seis números de la combinación ganadora y el reintegro
    1ª Categoría: Acertar los seis números de la combinación ganadora
    2ª Categoría: Acertar cinco números de la combinación y el número complementario
    3ª Categoría: Acertar cinco números de la combinación
    4ª Categoría: Acertar cuatro números de la combinación
    5ª Categoría: Acertar tres números de la combinación
    Reintegro: Acertar el número del reintegro
    
    En caso de que en una misma categoría aparecieran varios acertantes,
    se repartirían el premio a partes iguales.
    
    En cuanto al número complementario, el apostante no puede marcar ningún 
    número complementario, sino que ese número se contará dentro de los seis 
    que elija como su combinación, y solo en el caso de que los otros cinco 
    correspondan a la combinación principal; es decir, el complementario solo 
    se utiliza en la 2ª Categoría de premios.
    
    Cada apuesta se hace seleccionando 6 números de una tabla de 49 números 
    (del 1 al 49). Además el terminal que valida la apuesta asigna 
    automáticamente un número, del 0 al 9, independiente de los anteriores, 
    el reintegro.
    
    En el sorteo se extraen en total ocho números, de dos bombos. 
    En primer lugar se extraen 6 de entre los 49 números que determina los 
    premios de primera, tercera, cuarta y quinta categoría, así como una parte 
    de la categoría especial.
    Para determinar los premios de segunda categoría se extrae, de entre los 
    43 restantes, un séptimo número, el complementario
    
    Además, de un bombo diferente, con 10 números (del 0 al 9), se extrae 
    un octavo número para determinar el premio por reintegro, así como la otra 
    parte de la categoría especial.
        
        
"""

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

# get analysis of all bollas : number of ocurrencies over all history of the game
n_of_bola = [1,2,3,4,5,6]
all_bolas = list()
for bola_int in n_of_bola:
    bola_column = np.array([element for element in df_primitiva["Bola"+str(bola_int)]])
    unique_bola, counts = np.unique(bola_column, return_counts=True)
    all_bolas.append(np.array(list(zip(unique_bola, counts))))

# plot result
fig = plt.figure(figsize=(20,10), dpi=150)
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
plt.savefig("all bolas over all history.png")
# plt.show()

for_sorting_bolas = all_bolas.copy()

# sort numbers of columns in descending order of occurrences and take top numbers
top_occurrences_numbers = set()
n_of_balls_with_max_occurrence_take_to_analysis = 3
for i in range(0,6):
    sorted_elements =  sorted(for_sorting_bolas[i], key= lambda column: column[1], reverse=True)
    numbers = np.array([[i[0], i[1]] for i in sorted_elements])
    # numbers[:3] here deep of the numbers of max occurrences
    top_occurrences_numbers.update(set(numbers[:n_of_balls_with_max_occurrence_take_to_analysis][:, 0]))

print(f'It is analysis of max gained numbers from tickets over all history of the game')
print(f'Next set is set of numbers with max occurrence of {n_of_balls_with_max_occurrence_take_to_analysis} levels of every ball of the ticket:\n{top_occurrences_numbers}') 
all_combinations = [i for i in combinations(top_occurrences_numbers, 6)]
print(f'And with this set it forms\n{len(all_combinations)}\nof posible combinations of tickets.') 


#last gained combinations
last_n_games = 108
last5_ndarray = df_primitiva[["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]][-last_n_games:].to_numpy()

asserted_numbers_from_combination = list()
for i in range(len(last5_ndarray)):
    asserted_numbers_from_combination.append(len(set.intersection(top_occurrences_numbers, set(last5_ndarray[i, :]))))

print(f'After making analysis of last {last_n_games} games, comparing set of balls with maximum occurrence and gaining tickets,')
print('I got list of numbers where every number are number of balls from set with max occurrence that coincide ')
print(f'with balls from gaining tiquet')
print(asserted_numbers_from_combination)
print(f'\nAnd mean is {np.mean(asserted_numbers_from_combination)}\n')
print(f'Analysis was done getting to consideration {n_of_balls_with_max_occurrence_take_to_analysis} max occurrence of every one of 6 positions of the ball from ticket indepedently.')


import numpy as np
np.mean([6,6,6])