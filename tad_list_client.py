from datetime import date,timedelta
from tad_client import*

#crea una lista de los clientes 
def creat_list_client():
    list_client=[]
    return list_client

#añade los clientes a la lista
def load_in_list(list_client,cli):
    list_client.append(cli)

#elimina los clientes que tengan servicio especial
def remove_client(list_client,ty_se):

    count=0
    while count != len(list_client):#se introduce la lista y el tipo de servicio
                                          #para recorrer toda lista de los clientes    
        if ty_se == list_client[count] :#si el tipo de cliente coincide se elimina de la lista

            list_client.remove(cli)
            
        count+=1
        
    return list_client #se retorna la lista modificada

#elimina un cliente en particular 
def delate_client(list_client,cli):
    
    list_client.remove(cli)
    return list_client


#realiza el descuento a los clientes
def discount_price(list_client,year):

    cont=0
    
    while cont != len(list_client):# repite bucle hasta completar el temaño de la lista

        if(date.today().month().year()-timedelta(month=36)) >= list_client[cont].client[2]:#si el timepo que se cargo es mayor que el actual -3 años entonces realiza el descuento

            #realiza el descuento en la lista del elemento
            list_client[count].client[4]=(list_client[count].client[4]/100)*15
    
    cont+=1 

    return list_client #se debuelve la lista con los descuetos realizados

#lista de los clientes con promocion
def list_promotion_clients(list_client):
    
    cont=0
    #forma un nuevo listado de clientes
    list_client_2=[]

    #recorre la lista 
    while cont !=len(list_client):
        #si la fecha actual menos tres meses coincide con la fecha de  alta
        if (date.today().month().year()-timedelta(month=3)) >= list_client[cont].client[2]:

            aux_cli=list_client[cont]
            list_client_2.append(aux_cli)#se crea una nueva lista con los clietes que cumplen la condicion

        cont+=1
        
    return list_client_2 #devuelve la lista completa
