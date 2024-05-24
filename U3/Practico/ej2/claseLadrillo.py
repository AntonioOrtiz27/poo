class Ladrillo:
  __alto: int
  __largo: int
  __ancho: int
  __cant: int
  __idd: int
  __kg_Mat_prim_uti: float
  __costo: float
  __material_refrectario: list
  
  def __init__(self,alto:int, largo:int, ancho:int,cant:int,idd:int,kg_Mat_prim_uti:float,costo:int):
        self.__alto = alto
        self.__largo = largo
        self.__ancho = ancho
        self.__cant = cant
        self.__idd = idd
        self.__kg_Mat_prim_uti = kg_Mat_prim_uti
        self.__costo = int(costo)
        self.__material_refrectario = [] #agregacion
        
  def __str__(self):
    try:
        material_0 = str(self.__material_refrectario[0])
    except IndexError:
        material_0 = ''
    try:
        material_1 = str(self.__material_refrectario[1])
    except IndexError:
        material_1 = ''
    try:
        material_2 = str(self.__material_refrectario[2])
    except IndexError:
        material_2 = ''
    try:
        material_3 = str(self.__material_refrectario[3])
    except IndexError:
        material_3 = ''
    try:
        material_4 = str(self.__material_refrectario[4])
    except IndexError:
        material_4 = ''

    materiales = material_0 + material_1 + material_2 + material_3 + material_4
    return (f"Ladrillos\n ID: {self.__idd}, Alto: {self.__alto} cm, Largo: {self.__largo} cm, "
            f"Ancho: {self.__ancho} cm, Cantidad: {self.__cant}, "
            f"Kg:{self.__kg_Mat_prim_uti}, Costo: {self.__costo}, "
            f"Material: [{materiales}]")
            
            
  @property
  def idd(self):
        return int(self.__idd)
  @property
  def material_refrectario(self):
        return self.__material_refrectario

  @property
  def costo(self):
        return int(self.__costo)

  @property
  def cant(self):
        return int(self.__cant)