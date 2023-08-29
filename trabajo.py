class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med,lista_med):
        for i in lista_med:
            if i == med:
                return True
            else:
                self.__nombre=med
                return False 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}
    
    def verificarExiste(self,historia):
        for m in self.__lista_felinos or self.__lista_caninos:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        for i in self.__lista_felinos or self.__lista_caninos:
            if i.verHistoria == mascota.verHistoria():
                return True
            elif i.verHistoria != mascota.verHistoria:
                if mascota.verTipo == 'felino':
                    self.__lista_felinos[mascota.verHistoria()] = mascota
                elif mascota.verTipo == "canino":
                    self.__lista_caninos[mascota.verHistoria()] = mascota
        return False
    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_felinos or self.__lista_caninos:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_felinos or self.__lista_caninos:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_felinos or self.__lista_caninos:
            if historia == masc.verHistoria() and masc in self.__lista_felinos:
                self.__lista_felinos.pop(historia)  #opcion con el pop
                return True  #eliminado con exito
            elif historia == masc.verHistoria() and masc in self.__lista_caninos:
                self.__lista_caninos.pop(historia)  #opcion con el pop
                return True  #eliminado con exito
        return False 
    
def main():
    servicio_hospitalario = sistemaV()
    mas= Mascota()
    medicamento = Medicamento()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                mas.asignarHistoria(historia)
                nombre=input("Ingrese el nombre de la mascota: ")
                mas.asignarNombre(nombre)
                while True:
                    tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                
                    if tipo == "felino":
                        mas.asignarTipo(tipo)
                        break
                    elif tipo == 'canino':
                        mas.asignarTipo(tipo)
                        break
                    else:
                        print('tipo de mascota no valido')
                        continue

                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med = []

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    medicamento.asignarNombre(nombre_medicamentos,lista_med)
                    if medicamento.asignarNombre(nombre_medicamentos,lista_med) == True:
                        print('el medicamento ya esta asignado')
                        continue
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas.asignarPeso(peso)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")
