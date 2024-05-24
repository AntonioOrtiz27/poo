from GestorMaterial import *
from claseLadrillo import *
from claseMaterial import *

class gestor_ladrillos:
  __lista = list
  
  def __init__(self):
    self.__lista = []
    
  def cargarLadrillosDesdeCSV(self,GM):
    with open("ladrillo.csv") as archi:
      reader = csv.reader(archi,delimiter=';')
      next(reader)
      for fila in reader:
            ladri = Ladrillo(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            materiales = fila[7].split(',')
            for material in materiales:
                mate = GM.getGestorMat(material)
                if isinstance(mate,mate_refrec):
                  ladri.material_refrectario.append(mate)
                else:
                  print(f"No tiene material Refractario el Ladrillo {ladri.idd  }")
            self.__lista.append(ladri) 
      print("Ladrillos creados correctamente\n")
    archi.close()
  
  def mostrar_Ladrillito(self):
    for ladrillo in self.__lista:
      print(ladrillo)
      
  def caracterisitcas(self,GM,id):
    i:int=0
    band:bool=False
    while i < len(self.__lista) and band==False:
      objetito=self.__lista[i]
      if id == objetito.idd:
        print(f"Su costo es: ${objetito.costo}")
        add=GM.obtenerMaterial(id)
        adicional=add+objetito.costo
        print(f"Costo adicional por el Material Refractario: ${adicional}")
        band=True
      else:
        i+=1
      
  def formato(self,GM):
    print("N°Id     Material      Costo asociado")
    for objetito in self.__lista:
      mat=GM.obtenerMat(objetito.idd)
      add=GM.obtenerAdd(objetito.idd,objetito.costo)
      print(f"{objetito.idd}    {mat:<5}      {add}")
        