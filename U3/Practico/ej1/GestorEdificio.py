import csv
from claseEdifcio import *
from claseDepa import *

class gestorEdificio:
    __edificios: list
    
    def __init__(self):
        self.__edificios=[]
        
    def agregarEdificio(self,edificio):
        self.__edificios.append(edificio)
        

    def csvEdificio(self):
        with open('EdificioNorte.csv') as a:
            reader = csv.reader(a,delimiter=';')
            xedificio= None
            for fila in reader:
                if len(fila) == 6:
                    xedificio=Edificio(*fila)
                    self.__edificios.append(xedificio)
                elif len(fila) == 7:
                    departamento=Departamento(*fila)
                    xedificio.agregar_Dep(departamento) 
                    
            print("EDIFICIOS CARGADOS\n")
            
                         
    def mostrarArchivo(self):
        for edificio in self.__edificios:
            print(edificio)
            for depa in edificio.getDepa():
                print(depa)
                
    def edificioNom(self, nom):
        i = 0
        band = False
        while i < len(self.__edificios) and band==False:
            if self.__edificios[i].getNombre == nom:
                band = True
                for depa in self.__edificios[i].Departamento:
                    print(depa.getnya())
            else:
                i += 1   
            if band!=True:
                print(f"No se encontró un edificio con el nombre '{nom}'")
                
    def superficieTotal(self,edi):
        superficie = 0
        i=0
        band=False
        while i < len(self.__edificios) and band==False:
            if self.__edificios[i].getNombre == edi and band==False:
                band = True
                for depa in self.__edificios[i].Departamento:
                    superficie += float(depa.Superficie)
            else:
                i += 1
                
        if band is not True:            
            print("No se encontro el edificio.")
        else:
            print(f"La superficie total es {superficie}")
        return superficie
    
    def superficieTotal2(self, edi):
        superficie = 0
        for edificio in self.__edificios:
            if edificio.getNombre == edi:
                for depa in edificio.Departamento:
                    superficie += float(depa.Superficie)
        return superficie
    
    def buscarnomE(self,idd):
        i = 0
        band = False
        while i < len(self.__edificios) and band:
            if self.__edificios[i].idd == idd:
                band = False
            else:
                i+=1
        
        if not band:
            return self.__edificios[i].getNombre

    def suppropie(self,nom_P,GE):
        i = 0
        sup = 0
        band = True
        while i < len(self.__edificios) and band:
            idd = self.__edificios[i].idd
            for depa in self.__edificios[i].Departamento:
                if depa.getnya().lower() == nom_P.lower():
                    band = False
                    sup += float(depa.Superficie)
            i+=1
            
        if sup!=0:
            print(f"id del edificio: {idd}")
            NumEdi = GE.buscarnomE(idd)
            totalSup=GE.superficieTotal2(NumEdi)
            if NumEdi != 0:               
                porcentaje = 100 * (sup / totalSup)
                return porcentaje
            else:
                print("El área total del edificio es cero.")
            return None
        else:
            print("No se encontró una persona con ese nombre.\n")
        return None
    
    def CantidadDepas(self, numpiso):
        cont = 0
        for edi in self.__edificios:
            print(f"Para el {edi.getNombre  }")
            for depa in edi.Departamento:
                if depa.getNumpiso == numpiso:  
                    if depa.getCantdor == 3 and depa.getCantB > 1:
                        cont +=1
            print(f"La cantidad de departamentos que tienen 3 dormitorios y más de un baño en el piso {numpiso} es: {cont}\n")
  
