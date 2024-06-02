main
    lista = Lista()
    encoder = ObjectEncoder()
    dic = encoder.leerJSONArchivo("calefactores.json")
    lista = encoder.decodificarDiccionario(dic)
    
    encoder.guardarJSONArchivo(lista.to_dict(), "calefactores2.json")
    
    
lista
    def to_dict(self):
        d = dict(
            __class__=self.__class__.__name__,
            calefactores=[calefactor.to_dict() for calefactor in self]
            )
        return d
    
    
clase padre
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
    
    
    
clase hijo
    def to_dict(self):
        data = super().to_dict()
        data["__atributos__"]["potencia"] = self.potencia
        return data