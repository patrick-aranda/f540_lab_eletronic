# Objetivo: gráfico.
# Base: arquivo de dados csv.
# Requisitos: preciso dizer de qual arquivo ler os dados e qual tipo de gráfico desejado.


# Imports.
from pathlib import Path
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt


# Functions.
def prep_data_fourier():
    print("hello")
    #hgffjj

def prep_data_T_dB():
    columns = [[],[],[],[],[],[]]
    aux = []
    with open(filename, "r") as file:
        csvreader = csv.reader(file)
        global header
        header = next(csvreader) # next()method returns me the next record from my variable. Since is the first time used, it returns the first record (first line) and skip to next one.
        for row in csvreader: # "row" poderia ser qlq coisa, é apenas o índice da linha.
            aux = []
            aux.extend(row) # Estendo minha linha, deixando cada termo da linha em uma coluna. Como antes dei um next, csvreader começa da 2ª linha.
            for i in range(0,6): # Percorro minha lista aux.
                columns[i].append(float(aux[i])) # Adiciono o i-ézimo termo da minha lista aux à minha i-ézima coluna.
    global frequency_Hz, phase_Ch21_degree, Trans_dB, Trans_dB_error, phase_list, Trans, Vpp1_V, Vpp2_V
    frequency_Hz = columns[0]
    Vpp1_V = columns[1] # Dados desnecessários.
    Vpp2_V = columns[2] # Dados desnecessários.
    phase_Ch21_degree = columns[3]
    Trans = columns[4] # Dados desnecessários.
    Trans_dB = columns[5]
    Trans_dB_error = [] # Incerteza associada à transmitância em dB.
    for i in range(len(Trans_dB)):
        Trans_dB_error.append(0.02*(((1/Vpp2_V[i])**2)+((1/Vpp1_V[i])**2))**(1/2))
    phase_error = 0.01 # Incerteza associada à fase.
    phase_list = []
    for l in range(len(phase_Ch21_degree)):
        phase_list.append(phase_error)

def media_T_dB(): # Desnecessária neste programa.
    media = 0
    for j in range(len(Trans_dB)):
        media = media + Trans_dB[j]
    media = media/len(Trans_dB)
    return media

def desvio_padrao_T_dB(): # Desnecessária neste programa.
    aux = 0
    media = media_T_dB()
    for k in range(len(Trans_dB)):
        aux = aux + (Trans_dB[k] - media)**2
    desvio_padrao = (aux/(len(Trans_dB)-1))**(1/2)
    return desvio_padrao

def media_error(): # Desnecessária neste programa.
    desvio_padrao = desvio_padrao_T_dB()
    media_error = desvio_padrao/(len(Trans_dB))**(1/2)
    return media_error


# Code.
filepath = filedialog.askopenfilename() # Isto te permite selecionar um arquivo.
filename = Path(filepath).name

if filename in ("ch1_fourier_dados.csv", "ch2_fourier_dados.csv"):
    graphic_type = input("What's the desired graphic: ch1, ch2 or comparative?")
    prep_data_fourier()
    if graphic_type == "ch1":
        print("hello")
        #jsvsfjs
    elif graphic_type == "ch2":
        print("hello")
    else:
        print("hello")
else:
    graphic_type = input("What's the desired graphic: T_dB, phase or both?")
    prep_data_T_dB()
    if graphic_type == "T_dB":
        plt.xscale('log')
        plt.errorbar(frequency_Hz, Trans_dB, yerr=Trans_dB_error, fmt="o", markerfacecolor = "red", markeredgecolor = "black", capsize = 5)
        plt.xlabel(header[0])
        plt.ylabel(header[5])
        plt.xlim(left=5)
        plt.grid()
        plt.show()
    elif graphic_type == "phase":
        plt.xscale("log")
        plt.errorbar(frequency_Hz, phase_Ch21_degree, yerr=phase_list, fmt="o", markerfacecolor = "red", markeredgecolor = "black", capsize = 5)
        plt.xlabel(header[0])
        plt.ylabel(header[3])
        plt.xlim(left=5)
        plt.grid()
        plt.show()
    else:
        plt.xscale("log")
        trans_plot = plt.errorbar(frequency_Hz, Trans_dB, yerr=Trans_dB_error, fmt="o", markerfacecolor="blue", markeredgecolor="black", capsize=5)
        phase_plot = plt.errorbar(frequency_Hz, phase_Ch21_degree, yerr=phase_list, fmt="o", markerfacecolor = "red", markeredgecolor = "black", capsize = 5)
        plt.xlabel(header[0])
        plt.xlim(left=5)
        plt.grid()
        plt.legend([trans_plot,phase_plot],[header[5],header[3]])
        plt.show()
