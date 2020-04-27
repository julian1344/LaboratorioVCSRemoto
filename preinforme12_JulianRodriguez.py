# -*- coding: utf-8 -*-

"""

Created on Sat Apr 25 09:08:26 2020

@author: julian

"""

#%%

import numpy as np

promedioLista = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87, 
                 119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53, 
                 117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 
                 110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 
                 110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57, 
                 122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15, 
                 124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67, 
                 107.73, 105.76, 107.85] # Datos para trabajar los siguientes procedimientos.

numeroMaximo = (max([float(num) for num in promedioLista]))
numeroMinimo = (min([float(num) for num in promedioLista]))
print(float(numeroMaximo - numeroMinimo)) # Halle de los argumentos max y min los numeros pedidos, para luego encontrar la diferencia.

media = np.mean(promedioLista)
mediana = np.median(promedioLista) # Se utilizo numpy para obtener los valores indicados.
print(media, mediana) # promedioMedia = [num, sum/2([for num in promedioLista])].

promedioSupera = [ int(num) for num in promedioLista if media < int(num[0])]
print(promedioSupera)
        
suma = 0
desviacionProblema = [valor for valor in promedioLista if suma + (valor - media)**2]
print(desviacionProblema)

desviacionTemperatura = []

variable = 0.00986923
temp= (i*510)/(17.16*0.08206)
promedioTemperatura = [(temp) for temp in promedioLista if i*variable]









