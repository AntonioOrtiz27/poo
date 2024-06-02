import json
from pathlib import Path
from lista import Lista
from calefactor import *


class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        calefactores = d['calefactores']
        lista = Lista()
        
        for calefactor in calefactores:
            class_name = calefactor.pop('__class__')
            class_ = eval(class_name)
            atributos = calefactor['__atributos__']
            unCalefactor = class_(**atributos)
            lista.agregar(unCalefactor)
            
        return lista
        
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()            
            
    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
        
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)