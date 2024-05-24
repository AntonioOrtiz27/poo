from GestorEdificio import *

def menu():
    op=int(input("""Ingrese una opcion
                    [1] : Nombre y apellido de los propietarios de
                         cada uno de los departamentos del edificio.
                    [2] : Superficie total de un edificio.
                    [3] : Superficie total cubierta de su departamento y porcentaje
                          que representa del total de la superficie cubierta del edificio.
                    [4] : cantidad de departamentos que tienen 3 dormitorios y más de un baño. 
                    ---->"""))
    return op

def testComposicion():
    GE=gestorEdificio()
    GE.csvEdificio()
    
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            nom=str(input("ingrese nombre de edificio:"))
            GE.edificioNom(nom)
        elif opcion==2:
            edi=str(input("ingrese nombre de edificio para saber su superficie total cubierta:"))
            GE.superficieTotal(edi)
        elif opcion==3:
            nom_P = input("Ingrese nombre y apellido del propietario a mostrar superficie\n")
            porcentaje = GE.suppropie(nom_P,GE)
            if porcentaje is not None:
                print(f"Porcentaje que ocupan el/los departamentos de {nom_P} es: {porcentaje}%\n")
        elif opcion==4:
            numpiso=int(input("Ingrese numero de piso\n"))
            GE.CantidadDepas(numpiso)
            
        opcion=menu()
    
if __name__=="__main__":
        testComposicion()