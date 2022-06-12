from datetime import date,timedelta
#este tad crea un cliente carga sus datos
#y nos permite recperar su informacion

#crea la lista para guardar los datos de los cientes
def creat_client():

    client=["","","","","",0]
    return client

#carga los datos de los clientes en  la lista
def load_client(client,name,surnames,serv_type,serv_price,num_clie):

    client[0]=name
    client[1]=surname
    client[2]=today()
    client[3]=serv_type
    client[4]=serv_price
    client[5]=num_clie
    return client

def view_name(client):#devuelve el nombrel del cliente

    return client[0]

def view_surname(client):#devuelve el apellido del cliente

    return client[1]

def view_date_up(client):#devuelve el tipo de servicio del cliente

    return client[2]


def view_serv_type(client):#devuelve el tipo de servicio del cliente

    return client[3]

def view_serv_price(client):#devuelve el precio del servicio

    return client[4]

def view_num_clie(client):#devuelve el numero de cliente

    return client[5]




#permite modificar el nombre del cliete
def modify_name(client,name):

    client[0]=name
    return client

#modifica el apellido
def modify_surname(client,surname): 

    client[1]=name
    return client

#permite modificar la fecha de alta del cliente
def modify_date_up(client,day,month,year):

    client[2]=timedelta(day,month,year)
    return client


#permite modificar el servicio del cleinte
def modify_serv_type(client,serv_type):

    client[3]=serv_type
    return client


#modifica el precio del servicio
def modify_serv_price(client,serv_price):

    client[4]=serv_price
    return client


#modifica el numero del cliente
def modify_num_clie(client,num_clie):

    client[5]=num_clie
    return client
