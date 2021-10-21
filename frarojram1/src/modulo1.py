# -*- coding: utf-8 -*-
'''
Created on 18 oct 2021

@author: francis
'''
import csv
from collections import namedtuple
from datetime import datetime

RegistrosAirbnb = namedtuple('RegistrosAirbnb', 'visitas, room_type, neighborhood, satisfaction, accommodates, bedrooms, price, LATITUDE, LONGITUDE, NAME, CLEAN, STAIRS, NUMBER_OF_FLATS, LAST_RENT')

def leer_csv(fichero):
    
    registros = []
    
    with open(fichero) as f:
        
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        lista=[]
        
        for registros in lector:
        
            visitas = registros[0]
            room_type = registros[1]
            neighborhood = registros[2]
            satisfaction = float(registros[3])
            accommodates = int(registros[4])
            bedrooms = float(registros[5])
            price = float(registros[6])
            LATITUDE = registros[7]
            LONGITUDE = registros[8]
            NAME = registros[9]
            CLEAN = registros[10]
            STAIRS = registros[11]
            NUMBER_OF_FLATS = int(registros[12])
            LAST_RENT = datetime.strptime(registros[13],"%m/%d/%Y").date()
        
            tupla = RegistrosAirbnb(visitas, room_type, neighborhood, satisfaction, accommodates, 
                                    bedrooms, price, LATITUDE, LONGITUDE, NAME, CLEAN, 
                                    STAIRS, NUMBER_OF_FLATS, LAST_RENT)
            lista.append(tupla)
        
    return lista


def filtrar_por_visitas(registro, Visitas):
    res = [tupla for tupla in registro if tupla.visitas == Visitas]
    return res

















