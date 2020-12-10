from datetime import datetime
from typing import Dict
from pydantic import BaseModel

## 1st Block: Parameters definition

class ClientInDB(BaseModel):        ## Class of IN definition to DB.
    Id_Client: int                  ## Basemodel: Herency Mehod in Python.  
    NRegister: int       
    Name: str
    Last_name: str
    date_in: datetime =datetime.now()
    

## 2nd Block: Definition of fictitious DB
database_users=Dict[int,ClientInDB]
database_users={
    "1234":ClientInDB(**{"Id_Client":"1234",        ## **:Mapping Python Object.
    "NRegister":"1",
    "Name":"Pierina",
    "Last_name":"Fierro"
    })
}

def get_user(Id_Client: int):                       ## Function to obtain client information
    if Id_Client in database_users.keys():
        return database_users[Id_Client]            
    else:
        return None

def update_user(client_in_db : ClientInDB):         ## Function to update client information
    database_users[client_in_db.Id_Client] = client_in_db
    return client_in_db         

database_register=[]
generator={"id":0}                  ## auto increment

def save_client(client_register:ClientInDB):        ## Function to update client information
    generator["id"]=generator["id"]+1               ## Save in generator dictionary the ID of register number.
    client_register.NRegister=generator["id"]
    database_register.append(client_register)
    return client_register 