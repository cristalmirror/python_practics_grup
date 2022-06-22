
#se encuentra bajo GPL v2.0
#este programa contiene la insterfaz qu el usurio usara para
#manipular loos datos

from datetime import date
from tad_list_client import*
from tad_client import*

l_c=creat_list_client()#se crea el una variable de tipo lista de clietes

#introduce los datos al tad lista de cliete que se creo
def option_1():
    
    print("\***menu opcion 1***\n")
    n_c=creat_client()
    na=input("\nintrodusca el nombre del cliente ")
    sna=input("\nintrodusca el apellido del cliente ")
    s_t=input("\nintrodusca el tipo de servicio ")
    s_p=input("\nintrodusca el precio del servcio ")
    n_c=input("\nintrodusca el numero de cliente ")
    print("\n")

   n_c=load_client(n_c,na,sna,s_t,s_p,n_c)
   load_in_list(l_c,n_c)

#modifica los datos  de lo clientes mientras se le de la opcio de modificar
def option_2():

    opc3=1

    while opc3==1:
        print("\***menu opcion 2***\n")
        opc4=input("\nintrodusca el dato que desea modificar\n
                    modificar nombre              (1)
                    modificar apellido            (2)
                    modificar fecha de de alta    (3)
                    modificar tipo de servcio     (4)
                    modificar precio del servicio (5)
                    modificar numero de clinet    (6)
                    >>>")
        if opc4 ==1:
            print("\ncambio de nombre")
            #se ingresa los parametros de busqueda
            aux1=input("\ninstrodusca nombre actual>>>")
            aux2=input("\ninstrodusca el apellido actual>>>")
            aux3=input("\nintrodusca el nuero de cliente")
            
            #se busca el cliente que conisida con los datos de busqueda
            data=browser_client(l_c,aux1,aux2,aux3)

            #se modifica el dato relevante
            aux1=input("\ninstrodusca un nuevo nombre")
            clie_mod=modify_name(data,aux1)

            #elimina el cliente sin modifica de la lista de clintes
            l_c=delate_client(l_c,data)

            #agrega al cliente con la modificacion
            load_client(l_c,clie_mod)
            
            
        elif opc4==2:
            print("\ncambio de apellido")
             #se ingresa los parametros de busqueda
            aux1=input("\ninstrodusca nombre actual>>>")
            aux2=input("\ninstrodusca el apellido actual>>>")
            aux3=input("\nintrodusca el nuero de cliente")
            
            #se busca el cliente que conisida con los datos de busqueda
            data=browser_client(l_c,aux1,aux2,aux3)

            #se modifica el dato relevante
            aux1=input("\ninstrodusca un nuevo nombre")
            clie_mod=modify_surname(data,aux1)

            #elimina el cliente sin modifica de la lista de clintes
            l_c=delate_client(l_c,data)

            #agrega al cliente con la modificacion
            load_client(l_c,clie_mod)
           
        elif opc4==3:
             print("\ncambio de fecha de alta")
             #se ingresa los parametros de busqueda
            aux1=input("\ninstrodusca nombre actual>>>")
            aux2=input("\ninstrodusca el apellido actual>>>")
            aux3=input("\nintrodusca el nuero de cliente")
            
            #se busca el cliente que conisida con los datos de busqueda
            data=browser_client(l_c,aux1,aux2,aux3)

            #se modifica el dato relevante
            aux1=input("\ninstrodusca un nuevo dia -->")
            aux2=input("\ninstrodusca un nuevo mes -->")
            aux3=input("\ninstrodusca un nuevo dia -->")
            
            clie_mod=modify_date_up(data,aux1,aux2,aux3)

            #elimina el cliente sin modifica de la lista de clintes
            l_c=delate_client(l_c,data)

            #agrega al cliente con la modificacion
            load_client(l_c,clie_mod)
           
        elif opc4==4:
             #se ingresa los parametros de busqueda
            aux1=input("\ninstrodusca nombre actual>>>")
            aux2=input("\ninstrodusca el apellido actual>>>")
            aux3=input("\nintrodusca el nuero de cliente")
            
            #se busca el cliente que conisida con los datos de busqueda
            data=browser_client(l_c,aux1,aux2,aux3)

            #se modifica el dato relevante
            aux1=input("\ninstrodusca un nuevo nombre")
            clie_mod=modify_serv_type(data,aux1)

            #elimina el cliente sin modifica de la lista de clintes
            l_c=delate_client(l_c,data)

            #agrega al cliente con la modificacion
            load_client(l_c,clie_mod)
           
        elif opc4==5:
             #se ingresa los parametros de busqueda
            aux1=input("\ninstrodusca nombre actual>>>")
            aux2=input("\ninstrodusca el apellido actual>>>")
            aux3=input("\nintrodusca el nuero de cliente")
            
            #se busca el cliente que conisida con los datos de busqueda
            data=browser_client(l_c,aux1,aux2,aux3)

            #se modifica el dato relevante
            aux1=input("\ninstrodusca un nuevo nombre")
            clie_mod=modify_serv_price(data,aux1)

            #elimina el cliente sin modifica de la lista de clintes
            l_c=delate_client(l_c,data)

            #agrega al cliente con la modificacion
            load_client(l_c,clie_mod)
               
        elif opc4==6:
            #se ingresa los parametros de busqueda
            aux1=input("\ninstrodusca nombre actual>>>")
            aux2=input("\ninstrodusca el apellido actual>>>")
            aux3=input("\nintrodusca el nuero de cliente")
            
            #se busca el cliente que conisida con los datos de busqueda
            data=browser_client(l_c,aux1,aux2,aux3)

            #se modifica el dato relevante
            aux1=input("\ninstrodusca un nuevo dia -->")
            aux2=input("\ninstrodusca un nuevo mes -->")
            aux3=input("\ninstrodusca un nuevo dia -->")
            clie_mod=modify_num_clie(data,aux1)

            #elimina el cliente sin modifica de la lista de clintes
            l_c=delate_client(l_c,data)

            #agrega al cliente con la modificacion
            load_client(l_c,clie_mod)
           
        
        
    
#elimna un cliente de la lista de  clientes
def option_3():
    #se ingresa los parametros de busqueda
    aux1=input("\ninstrodusca nombre actual>>>")
    aux2=input("\ninstrodusca el apellido actual>>>")
    aux3=input("\nintrodusca el nuero de cliente")
            
    #se busca el cliente que conisida con los datos de busqueda
    data=browser_client(l_c,aux1,aux2,aux3)

    #elimina el cliente que se selecciono
    delate_client(l_c,data)
    
#imprime los datos de la lista de clientes
def option_4():
    #recorre la lista de clientes  y la imprime
    i=0
    for i in l_c:
        print("\n------------------------\n")
        print("\nNombre: ",view_name(i))
        print("\nApellido: ",view_surname(i))
        print("\nAlta: ",view_date_up(i))
        print("\nTipo de Servicio: ",view_serv_type(i))
        print("\nPrecio del Servicio: ",view_serv_price(i))
        print("\nCodigo del Cliente: ",view_num_clie(i))
        print("\n")
        
    
#elimia los clientes con un servicio dado 
def option_5():

    ts=input("\nintrodusca el servicio para elimiar clientes eliminar>>>")

    l_c=remove_client(l_c,ts)

        
    
#realiza el descuento a los clientes con servcio de mas de tres años
def option_6():
    
    data_time_now=input("introdusca el dia de hoy en el siguie te formato:\n dd-mm-aa\n ejemplo 02-11-2025\n>>>")    

    l_c=discount_price(l_c,data_time_now)
    
#retorna la lista de los clientes que tienen promocion
def option_7():
    auxi=client_with_promotion(l_c)

    i=0
    for i in auxi:
        print("\n------------------------\n")
        print("\nNombre: ",view_name(i))
        print("\nApellido: ",view_surname(i))
        print("\nAlta: ",view_date_up(i))
        print("\nTipo de Servicio: ",view_serv_type(i))
        print("\nPrecio del Servicio: ",view_serv_price(i))
        print("\nCodigo del Cliente: ",view_num_clie(I))
        print("\n")
    
    
def option_8():
    
    print("\n----Bienverido por favor introdusca la operacion que desea realizar-----\n\n")
    print("agregar un cliente                              (1)\n")     
    print("modificar un cliente                            (2)\n")
    print("eliminar un cliente                             (3)\n")
    print("acceder al listado de clientes                  (4)\n")
    print("eliminar cliente con servico x                  (5)\n")
    print("realizar descuento a user de mas de 3anios      (6)\n")
    print("realizar listado de los usuarios con promocion  (7)\n")
    print("imprimir el menu de opciones                    (8)\n")



# se crea el menu de opciones
print("\n----Bienverido por favor introdusca la operacion que desea realizar-----\n\n")


print("agregar un cliente                              (1)\n")     
print("modificar un cliente                            (2)\n")
print("eliminar un cliente                             (3)\n")
print("acceder al listado de clientes                  (4)\n")
print("eliminar cliente con servico x                  (5)\n")
print("realizar descuento a user de mas de 3anios      (6)\n")
print("realizar listado de los usuarios con promocion  (7)\n")
print("imprimir el menu de opciones                    (8)\n")
opc=1
opc2=0

#carga el dato de la opcion seleccionada
opc2=input(">>>")

#evalua las opciones del sistema 
while opc == 1:
    if opc2==0:

        print("no se tomo ningura opcion\n")

    elif opc2==1:

        option_1()

    elif opc2 == 2:

        option_2()
        
    elif opc2 == 3:

        option_3()
        
    elif opc2 == 4:

        option_4()
        
    elif opc2 == 5:

        option_5()
        
    elif opc2 == 6:

        option_6()
        
    elif opc2 == 7:
        option_7()

    elif opc2 == 8:
        option_8()
        
    opc=input("desea realizar otra operacion \nSI(1)\nNO(0)\n")

