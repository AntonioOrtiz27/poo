class Calefactor:
    def __init__(self, marca, modelo, pais, precio, forma_de_pago, cuotas, promocion):
        self.marca = marca
        self.modelo = modelo
        self.pais = pais
        self.precio = float(precio)
        self.forma_de_pago = forma_de_pago
        self.cuotas = int(cuotas)
        self.promocion = promocion
        
    def __str__(self):
        return f"{self.modelo} {self.precio}"
    
    def to_dict(self):
        d = {
            "__class__": self.__class__.__name__,
            "__atributos__": {
                "marca": self.marca,
                "modelo": self.modelo,
                "pais": self.pais,
                "precio": self.precio,
                "forma_de_pago": self.forma_de_pago,
                "cuotas": self.cuotas,
                "promocion": self.promocion
                }
            }
        return d
    
    def calcular_importe(self):
        importe = self.precio
        if self.promocion == "Si":
            importe -= self.precio*0.15
        return importe
        
        
        
class CalefactorElectrico(Calefactor):
    def __init__(self, marca, modelo, pais, precio, forma_de_pago, cuotas, promocion, potencia):
        super().__init__(marca, modelo, pais, precio, forma_de_pago, cuotas, promocion)
        self.potencia = potencia
    
    def __str__(self):
        return super().__str__() + f"{self.potencia}"
    
    def to_dict(self):
        data = super().to_dict()
        data["__atributos__"]["potencia"] = self.potencia
        return data
    
    def calcular_importe(self):
        importe = super().calcular_importe()
        
        if self.potencia > 1000:
            importe += self.precio*0.01
        if self.cuotas > 1:
            importe += self.precio*0.3
        return importe
        
class CalefactorGas(Calefactor):
    def __init__(self, marca, modelo, pais, precio, forma_de_pago, cuotas, promocion, matricula, calorias):
        super().__init__(marca, modelo, pais, precio, forma_de_pago, cuotas, promocion)
        self.matricula = matricula
        self.calorias = calorias    
        
    def to_dict(self):
        data = super().to_dict()
        data["__atributos__"]["matricula"] = self.matricula
        data["__atributos__"]["calorias"] = self.calorias
        return data
        
    def __str__(self):
        return super().__str__() + f"{self.calorias}"
    
        
    def calcular_importe(self):
        importe = super().calcular_importe()
        if self.calorias > 3000:
            importe +=  self.precio*0.01
        if self.cuotas > 1:
            importe += self.precio*0.4
        return importe