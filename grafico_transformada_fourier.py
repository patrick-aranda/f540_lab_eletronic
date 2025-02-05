# Dados em arquivo csv.
import csv


columns = [[],[],[]]
with open("ch1_fourier_dados.csv", "r") as file:
    csvreader = csv.reader(file) # Lê o arquivo, linha por linha, e retorna uma lista.
    header1 = next(csvreader) # next()method returns me the next record from my variable. Since is the first time used, it returns the first record (first line) and skip to next one.
    next(csvreader)
    for row in csvreader: # "row" poderia ser qlq coisa, é apenas o índice da linha.
        columns[0].append(float(row[0]))
        columns[1].append(float(row[1]))
       
with open("ch2_fourier_dados.csv", "r") as file:
    csvreader = csv.reader(file)
    next(csvreader)
    next(csvreader)
    for row in csvreader:
        columns[2].append(float(row[1]))
frequency_Hz = columns[0]
amplitude_1 = columns[1]
amplitude_2 = columns[2]


import matplotlib.pyplot as plt


plt.xscale("log")



from math import log10

frequency_log_Hz = []
for i in frequency_Hz:
    frequency_log_Hz.append(log10(i))
#Queria deixar a escala do eixo x em décadas (10**log(f)) de Hz.
x_axis = [f"10^{x:.3f}" for x in frequency_log_Hz]
#Não consegui mudar o eixo x como queria. Se coloco para plotar x_axis o eixo fica todo poluido.
header1[0] = "frequency_log_Hz"

from pylab import plot, show, xlabel, legend, xlim
plot(frequency_log_Hz,amplitude_1,"go") #Primeiro termo da string indica cor (g=green) e segundo diz para ser pontos pequenos.
plot(frequency_log_Hz,amplitude_2,"bo") #b indica blue.
xlabel(header1[0])
xlim(1.9,4.5) #Restringi o gráfico para região de interesse.
legend(["Amplitude Ch1", "Amplitude Ch2"])
show()
