"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """



import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
import time
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos
def initialize(tipo: str):
    Data={
        "videos":None,
        "categorias":None
    }
    Data["videos"]=lt.newList(tipo)
    Data["categorias"]=lt.newList(tipo)

    return Data
# Funciones para agregar informacion al catalogo
def add_video(Data, video):
    lt.addLast(Data["videos"],video)

def add_categoria(Data, categoria):
    lt.addLast(Data["categorias"],categoria)

def compare_likes(vid1:dict,vid2:dict)->bool:
    return float(vid1["likes"])>float(vid2["likes"])

def filtrar_count_cat(videos:list,categories:list,categoria:str,pais:str)->list:
    vids_cat=lt.newList()
    cat_id=None
    j=0
    search=True
    while j<lt.size(categories) and search:
        categ=lt.getElement(categories,j)
        if categ["name"]==categoria:
            search=False
            print(categ)
            cat_id=categ["id"]
        j+=1
    for i in range(lt.size(videos)):
        video_i=lt.getElement(videos,i)
        if video_i["category_id"]==cat_id and video_i["country"]==pais:
            lt.addLast(vids_cat,video_i)
    return vids_cat

def sort_vids(videos:list)->list:  
    start_time = time.process_time()
    sorted_list = shell.sort(videos, compare_likes)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByLikes(video1, video2): 
    """ Devuelve verdadero (True) si los likes de video1 son menores que los del video2 
    Args: video1: informacion del primer video que incluye su valor 'likes' 
    video2: informacion del segundo video que incluye su valor 'likes' """
    return (float(video1['likes']) < float(video2['likes']))

# Funciones de ordenamiento
def sortVideos(Data, size, algorithm):
    sub_list = lt.subList(Data['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if algorithm=="shell":
        sorted_list = shell.sort(sub_list, cmpVideosByLikes)
    elif algorithm=="selection":
        sorted_list = sel.sort(sub_list, cmpVideosByLikes)
    elif algorithm=="insertion":
        sorted_list = ins.sort(sub_list, cmpVideosByLikes)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

