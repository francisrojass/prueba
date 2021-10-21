'''
Created on 19 oct 2021

@author: francis
'''
from modulo1 import *

def main():
    
    datos = leer_csv("../data/TI2_airbnb.csv")
    
    print("Número de datos leídos ===  ", len(datos))
    
    
    print("Tres primeros registros ===  ", datos[:3])
    
    
    print("Tres últimos registros ===  ", datos[125:])
    
    filtro_por_visista = filtrar_por_visitas(datos, "moderado")
    print("Pisos visitados moderadamente == ", filtro_por_visista)
    
if __name__ == '__main__':
    main()