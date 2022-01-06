"""
"La primitiva" - statistics of numbers

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
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

# create subfolder for storing data
if "result of analysis of primitiva" not in os.listdir():
    os.mkdir("result of analysis of primitiva")

# read lottery data
file_name = "historical data la primitiva 11_09_1999 -  30_12_2021.xlsx"
sheet = "numeros ganadores"
df_primitiva_all_data = pd.read_excel(io=file_name, sheet_name=sheet)
df_primitiva = df_primitiva_all_data

# get analysis of all bollas : number of ocurrencies over all history of the game
n_of_bola = [1,2,3,4,5,6]
all_bolas = list()
for bola_int in n_of_bola:
    bola_column = np.array([element for element in df_primitiva["Bola"+str(bola_int)]])
    unique_bola, counts = np.unique(bola_column, return_counts=True)
    all_bolas.append(np.array(list(zip(unique_bola, counts))))

# plot scatter chart where distribution of all balls showed in the same chart
fig = plt.figure(figsize=(15,7), dpi=100)
axes = fig.add_axes([0.1,0.1,0.8,0.8])
name_bola = 1
for bola in all_bolas:
    axes.scatter(bola[:,0], bola[:,1], label='bola'+str(name_bola))
    name_bola +=1
axes.legend(loc=5)
plt.xlabel('number')
plt.ylabel(f'total draws over last {df_primitiva.shape[0]} games')
plt.grid(visible= True, which= 'both', axis= 'both')
plt.xticks(list(range(1,50)))
plt.title(f"distribution of winning numbers over last {df_primitiva.shape[0]} games")
plt.savefig(f"result of analysis of primitiva\distribution of wining numbers over last {df_primitiva.shape[0]} games in same scatter plot chart.png")

# plot bar chart where distribution of every ball of 6 is showed separetely in each subplot 
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(nrows=6, ncols=1, figsize=(10,20), dpi=150)
fig.suptitle(f"distribution of winning numbers over last {df_primitiva.shape[0]} games for 6 balls seaparately", fontsize=14)
fig.subplots_adjust(top=0.95)
for column in range(6):
    ax[column].bar(all_bolas[column][:,0], all_bolas[column][:,1], width=1, edgecolor="white", linewidth=0.7)
    len_ticks = 50
    ax[column].set(xlim=(0, len_ticks), xticks=np.arange(1, len_ticks))
    ax[column].set_title(f"Bola Nº {column+1}")
plt.savefig(f"result of analysis of primitiva\distribution of winning numbers over last {df_primitiva.shape[0]} games for 6 balls seaparately in bar chart.png")

# sort wining numbers of every ball in descending order of occurrences and take n top numbers
for_sorting_bolas = all_bolas.copy()
top_occurrences_numbers = set()
n_of_balls_with_max_occurrence_take_to_analysis = 3
for i in range(0,6):
    sorted_elements =  sorted(for_sorting_bolas[i], key= lambda column: column[1], reverse=True)
    print(sorted_elements)
    numbers = np.array([[i[0], i[1]] for i in sorted_elements])
    # n_of_balls_with_max_occurrence_take_to_analysis -> here nº of numbers with max occurrences
    top_occurrences_numbers.update(set(numbers[:n_of_balls_with_max_occurrence_take_to_analysis][:, 0]))

all_combinations = [i for i in combinations(top_occurrences_numbers, 6)]

#last gained combinations
last_n_games = 108
last5_ndarray = df_primitiva[["Bola1", "Bola2", "Bola3", "Bola4", "Bola5", "Bola6"]][-last_n_games:].to_numpy()
asserted_numbers_from_combination = list()
for i in range(len(last5_ndarray)):
    asserted_numbers_from_combination.append(len(set.intersection(top_occurrences_numbers, set(last5_ndarray[i, :]))))

# description of analysis
with open("result of analysis of primitiva\description over analysis of wining numbers and the game.txt", "w") as file_description:
    file_description.write(f'It is analysis of max winning numbers from tickets over {str(df_primitiva.shape[0])} games\n')
    file_description.write(f'Next set is set of numbers with max occurrence of {n_of_balls_with_max_occurrence_take_to_analysis} levels of every ball of the ticket:\n{top_occurrences_numbers}\n') 
    file_description.write(f'And with this set it forms\n{len(all_combinations)}\nof posible combinations of tickets.\n') 
    file_description.write(f'After making analysis of last {last_n_games} games, comparing set of balls with maximum occurrence and gaining tickets,\n')
    file_description.write('I got list of numbers where every number are number of balls from set with max occurrence that coincide\n')
    file_description.write(f'with balls from gaining tiquet\n')
    file_description.write(f"{asserted_numbers_from_combination}\n")
    file_description.write(f'\nAnd mean is {np.mean(asserted_numbers_from_combination)}\n')
    file_description.write(f'Analysis was done getting to consideration {n_of_balls_with_max_occurrence_take_to_analysis} max occurrence of every one of 6 positions of the ball from ticket indepedently.')

# saving combinations of tickets with major probability to excel
all_combinations_pandas_df = pd.DataFrame(all_combinations)
name_of_excel_file = "result of analysis of primitiva/all possible "+ str(len(all_combinations)) +" tickets combinations of set of top "+ str(n_of_balls_with_max_occurrence_take_to_analysis) +" max drawed numbers of every of 6 balls " + str(top_occurrences_numbers) + " over period of "+ str(df_primitiva.shape[0]) +" games.xlsx"
all_combinations_pandas_df.to_excel(excel_writer= name_of_excel_file)

# get analysis of all numbers drawn over all 6 balls : number of ocurrencies over all history of the game
n_of_bola = [1,2,3,4,5,6]
all_bolas = list()

for bola_int in n_of_bola:
    bola_column = [element for element in df_primitiva["Bola"+str(bola_int)]]
    unique_bola, counts = np.unique(bola_column, return_counts=True)
    all_bolas.append(dict(list(zip(unique_bola, counts))))

sum_of_all_numbers_over_6_balls = {i:0 for i in range(1,50)}

for column in all_bolas:
    keys_list = column.keys()
    for number in range(1,50):
        if number in keys_list:
            sum_of_all_numbers_over_6_balls[number] += column[number]

fig = plt.figure(figsize=(15,3), dpi=100)
axes = fig.add_axes([0.1,0.1,0.8,0.8])
plt.scatter(sum_of_all_numbers_over_6_balls.keys(), sum_of_all_numbers_over_6_balls.values())
plt.grid(visible= True, which= 'both', axis= 'both')
plt.xticks(list(range(1,50)))
plt.title(f"distribution of all numbers over 6 balls over period of "+ str(df_primitiva.shape[0]) +" games")
plt.savefig(f"result of analysis of primitiva\distribution of all numbers over 6 balls over period of "+ str(df_primitiva.shape[0]) +" games.png")