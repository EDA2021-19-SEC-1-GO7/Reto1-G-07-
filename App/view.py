"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing import cast
import config as cf
import sys
import controller as ctrl
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Mostrar los videos con más likes que son tendencia.")
    print("3- Video que más ha sido trending en un pais especifico.")
    print("4- Video que más ha sido trending en una categoria especifica.")
    print("5- n videos con más comentarios, en un pais y con tag especifico.")

def printType():
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")

def printSortingAlgorithm():
    print("1- Selection Sort")
    print("2- Insertion Sort")
    print("3- Shell Sort")

Data = None

def initialize(tipo)->dict:
    return ctrl.initialize(tipo)

def Load_Data(storage:dict)->None:
    ctrl.Load_Data(storage)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        printType()
        Inputs = input("Seleccione el tipo de representación de la lista\n")
        if int(Inputs[0]) == 1:
            Datos=initialize('ARRAY_LIST')    
        elif int(Inputs[0]) == 2:
            Datos=initialize('LINKED_LIST')   
        print("Cargando información de los archivos ....")
        Load_Data(Datos)
        print("Numero de videos cargados: "+str(lt.size(Datos["videos"])))
        first=lt.firstElement(Datos["videos"])
        print("Datos del primer video cargado:\n"+
            "Titulo: "+str(first["title"])+"\n"+
            "Canal: "+str(first["channel_title"])+"\n"+
            "Fecha de trending: "+str(first["trending_date"])+"\n"+
            "Pais: "+str(first["country"])+"\n"+
            "Vistas: "+str(first["views"])+"\n"+
            "Likes: "+str(first["likes"])+"\n"+
            "Dislikes: "+str(first["dislikes"])
        )
        print("Categorias: \n"+"id "+" nombre")
        for i in range(lt.size(Datos["categorias"])):
            cats=Datos["categorias"]
            elemento=lt.getElement(cats,i+1)
            id=elemento["id"]
            name=elemento["name"]
            print(id+" "+name)
        
    elif int(inputs[0]) == 2:
        country = input("Indique el país: ")
        category_name = input("Indique el nombre de la categoría: ")
        n = int(input("Indique tamaño de la muestra: "))

        while n>lt.size(Datos["videos"]):
            print("La muestra excede la cantidad de videos cargados en la memoria")
            n = input("Indique tamaño de la muestra: ")

        printSortingAlgorithm()
        Inputs = input("Seleccione el tipo de algoritmo de ordenamiento iterativo\n")
        if int(Inputs[0]) == 1:
            pass  
        elif int(Inputs[0]) == 2:
            pass


    else:
        sys.exit(0)
sys.exit(0)
