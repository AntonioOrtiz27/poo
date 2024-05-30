from claseServicio import Servicio
from claseServicioTransporte import ServicioT
from claseServicioEmbalaje import ServicioE
from lista import Lista

def test():
    opcion = int(input("""Ingrese opcion: 
        1_Insertar por cola
        2_Mostrar datos por cola
        3_Mostrar lista ordenada por costo
        4_Mostrar cantidad de servis cuyo embalaje supera los 50kg.
        5_Servicio que mas contrataciones tuvo.
        0_Para finalizar
        ----->""")) 
    return opcion 
    
if __name__ == '__main__':
    lista = Lista()
      
    #insertar por posición Manuel,al final pos-1 o a la cabeza pos.
    op=test()
    while op != 0:
        if op == 1:
            dato=str(input("ingrese el servicio a insertar en la lista de servicios(Transporte o Embalaje):"))
            if dato == "transporte":
                nomEmpresa=input("ingrese Nombre de Empresa:")
                nomContratante=input("ingrese Nombre de contratante:")
                direccion=input("ingrese direccion:")
                fecha=input("ingrese fecha:")
                comision=float(input("ingrese comision:"))
                precio=float(input("ingrese precio:"))
                peso=float(input("ingrese peso:"))
                destino=input("ingrese destino:")
                hora=float(input("ingrese hora:"))
                transportesito= ServicioT(nomEmpresa,nomContratante,direccion,fecha,comision,precio,peso,destino,hora)
                lista.agregar(transportesito)
            elif dato == "embalaje":
                nomEmpresa=input("ingrese Nombre de Empresa:")
                nomContratante=input("ingrese Nombre de contratante:")
                direccion=input("ingrese direccion:")
                fecha=input("ingrese fecha:")
                comision=float(input("ingrese comision:"))
                precio=float(input("ingrese precio:"))
                peso=float(input("ingrese peso:"))
                cantidad=int(input("ingrese cantidad de unidades:"))
                embalaje =ServicioE(nomEmpresa,nomContratante,direccion,fecha,comision,precio,peso,cantidad)
                lista.agregar(embalaje)
            else:
                print("Tipo de inmueble no reconocido.")
        elif op==2:
            print("Inmuebles insertados.")
            lista.mostrar()
        elif op==3:
            lista.mostrarlistaTransporte()
        elif op==4:
            lista.mostrarlistaEmbalaje()
        elif op==5:
            fecha=str(input("ingrese fecha:"))
            lista.mostrarfechas(fecha)
        op=test()
        
'''
1
transporte
TransporteX
Juan Pérez
Calle 123, Ciudad
2024-05-01
5
100
1000
Buenos Aires
5
1
embalaje
EmbalajeY
María López
Avenida 456, Ciudad
2024-05-01
10
10
60
5
'''
