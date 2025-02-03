import csv
columns = [[],[],[],[],[],[]] #Número de colunas (pouco eficiente o código)
aux = []
with open("3-amplificador_de_tensão.csv", "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader) #next()method returns me the next record from my variable. Since is the first time used, it returns the first record (first line) and skip to next one.
    for row in csvreader: #"row" poderia ser qlq coisa, é apenas o índice da linha.
        aux = []
        aux.extend(row) #extendo minha linha, deixando cada termo da linha em uma coluna. Como antes dei um next, csvreader começa da 2ª linha.
        for i in range(0,6): #percorro minha lista aux.
            columns[i].append(float(aux[i])) #adiciono o i-ézimo termo da minha lista aux à minha i-ézima coluna.

frequency_Hz = columns[0]
Vpp1_V = columns[1]
Vpp2_V = columns[2]
phase_Ch21_degree = columns[3]
Trans = columns[4]
Trans_dB = columns[5]


Trans_dB_error = []
for i in range(len(Trans_dB)):
    Trans_dB_error.append(0.02*(((1/Vpp2_V[i])**2)+((1/Vpp1_V[i])**2))**(1/2))

#media = 0 # Da transmitância
#for j in range(len(Trans_dB)):
#    media = media + Trans_dB[j]
#media = media/len(Trans_dB) # Calculei a média das transmitâncias

#aux = 0
#for k in range(len(Trans_dB)):
#    aux = aux + (Trans_dB[k] - media)**2
#desvio_padrao = (aux/(len(Trans_dB)-1))**(1/2)
#media_error = desvio_padrao/(len(Trans_dB))**(1/2)

phase_error = 0.01
phase_list = []
for l in range(len(phase_Ch21_degree)):
    phase_list.append(phase_error)

import numpy as np
import matplotlib.pyplot as plt

plt.xscale('log')
plt.errorbar(frequency_Hz, Trans_dB, yerr=Trans_dB_error, fmt="o", markerfacecolor = "red", markeredgecolor = "black", capsize = 5)
plt.xlabel(header[0])
plt.ylabel(header[5])
plt.xlim(left=5)
plt.grid()
plt.show()

#print("Média =", media, "+/-", media_error)
