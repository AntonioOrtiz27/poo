from claseMaterial import *
import csv

class gestor_material:
  __listamats = list
  
  def __init__(self):
    self.__listamats = []
    
  def cargarMaterialesDesdeCSV(self):
    with open("Material.csv",) as a: 
        reader = csv.reader(a,delimiter=';') 
        next(reader)
        for fila in reader: 
          material = mate_refrec(int(fila[0]), fila[1], int(fila[2]), float(fila[3]), fila[4])
          self.__listamats.append(material) 
        print("Material cargados correctamente.")
        
  def getGestorMat(self,idd):
    i = 0
    
    while i < len(self.__listamats):
      if(int(self.__listamats[i].idd) == int(idd)):
        return self.__listamats[i]
      else:
        i+=1
    return
    
  
  def mostrar_material(self):
    for mate in self.__listamats:
      print(mate)
      
  def obtenerMaterial(self,id):
    for objetito in self.__listamats:
      if id == objetito.idd:
        print(f"sus caracteristicas son:{objetito.caracteristicas}")
        return objetito.costo_adicional
      
  def obtenerMat(self,idd):
    for materiales in self.__listamats:
      if idd == materiales.idd:
        return materiales.material
  
  def obtenerAdd(self,id,costo):
    for costito in self.__listamats:
      if id==costito.idd:
        return costo+costito.costo_adicional