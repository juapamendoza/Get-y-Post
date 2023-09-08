from fastapi import FastAPI

#pydantic va a obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

# crear el objeto a partir de la clase
PassengersAPI = FastAPI()

class Passenger(BaseModel):
    id: int
    name: str
    survived: bool
    sex: str
    age: int
    ticket: str
    fare: float
    cabin: str

passenger_list=[Passenger(id=1, name="Braund, Mr. Owen Harris", survived=0, sex="male", age=22, ticket="A/5 21171", fare=7.25, cabin="None"),
                Passenger(id=2, name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)", survived=1, sex="female", age=38, ticket="PC 17599", fare=71.2833, cabin="C85"),
                Passenger(id=3, name="Heikkinen, Miss. Laina", survived=1, sex="female", age=26, ticket="STON/O2. 3101282", fare=7.925, cabin="None"),
                Passenger(id=4, name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", survived=1, sex="female", age=35, ticket="113803", fare=53.1, cabin="C123"),
                Passenger(id=5, name="Allen, Mr. William Henry", survived=0, sex="male", age=35, ticket="373450", fare=8.05, cabin="None"),
                Passenger(id=6, name="Moran, Mr. James", survived=0, sex="male", age=0, ticket="330877", fare=8.45583, cabin="None"),
                Passenger(id=7, name="McCarthy, Mr. Timothy J", survived=0, sex="male", age=54, ticket="17463", fare=51.8625, cabin="E46"),
                Passenger(id=8, name="Palsson, Master. Gosta Leonard", survived=0, sex="male", age=2, ticket="349909", fare=21.075, cabin="None"),
                Passenger(id=9, name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", survived=1, sex="female", age=27, ticket="347742", fare=11.1333, cabin="None"),
                Passenger(id=10, name="Nasser, Mrs. Nicholas (Adele Achem)", survived=1, sex="female", age=14, ticket="237736", fare=30.0708, cabin="None"),
                Passenger(id=11, name="Sandstrom, Miss. Marguerite Rut", survived=1, sex="female", age=4, ticket="PP 9549", fare=16.7, cabin="G6"),
                Passenger(id=12, name="Bonnell, Miss. Elizabeth", survived=1, sex="female", age=58, ticket="113783", fare=26.55, cabin="C103"),
                Passenger(id=13, name="Saundercock, Mr. William Henry", survived=0, sex="male", age=20, ticket="A/5. 2151", fare=8.05, cabin="None"),
                Passenger(id=14, name="	Andersson, Mr. Anders Johan", survived=0, sex="male", age=39, ticket="347082", fare=31.275, cabin="None"),
                Passenger(id=15, name="Vestrom, Miss. Hulda Amanda Adolfina", survived=0, sex="female", age=0, ticket="350406", fare=7.8542, cabin="None")]

@PassengersAPI.get("/passengerclass/")
async def passengerclass():
    return (passenger_list)

@PassengersAPI.post("/passengerclass/")
async def passengerclass(passenger:Passenger):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_passenger in enumerate(passenger_list):
        if saved_passenger.id == passenger.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el pasajero ya existe"}
    else:
        passenger_list.append(passenger)
        return passenger

#uvicorn [title_archivo]:[title_objeto] --reload    
"""
{
    "id": 16,
    "name": "Hewlett, Mrs. (Mary D Kingcome)",
    "survived": true,
    "sex": "female",
    "age": 55,
    "ticket": "248706",
    "fare": 16,
    "cabin": "None"
}
{
    "id": 17,
    "name": "Rice, Master. Eugene",
    "survived": false,
    "sex": "male",
    "age": 2,
    "ticket": "382652",
    "fare": 29.125,
    "cabin": "None"
}
{
    "id": 18,
    "name": "Williams, Mr. Charles Eugene",
    "survived": true,
    "sex": "male",
    "age": 0,
    "ticket": "244373",
    "fare": 13,
    "cabin": "None"
}
{
    "id": 19,
    "name": "Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",
    "survived": false,
    "sex": "female",
    "age": 31,
    "ticket": "345763",
    "fare": 18,
    "cabin": "None"
}
{
    "id": 20,
    "name": "Masselmani, Mrs. Fatima",
    "survived": true,
    "sex": "female",
    "age": 0,
    "ticket": "2649",
    "fare": 7.225,
    "cabin": "None"
}

###########

{
    "id": 19,
    "name": "PRUEBA",
    "survived": true,
    "sex": "female",
    "age": 0,
    "ticket": "2649",
    "fare": 7.225,
    "cabin": "PRUEBA"
}

{
    "id": 4,
    "name": "PRUEBA",
    "survived": true,
    "sex": "female",
    "age": 0,
    "ticket": "2649",
    "fare": 7.225,
    "cabin": "PRUEBA"
}

###########

{
    "id": 21,
    "name": "Fynney, Mr. Joseph J",
    "survived": false,
    "sex": "male",
    "age": 35,
    "ticket": "239865",
    "fare": 26,
    "cabin": "None"
}
{
    "id": 22,
    "name": "Beesley, Mr. Lawrence",
    "survived": true,
    "sex": "male",
    "age": 34,
    "ticket": "248698",
    "fare": 13,
    "cabin": "D56"
}
{
    "id": 23,
    "name": "McGowan, Miss. Anna "Annie"",
    "survived": true,
    "sex": "female",
    "age": 15,
    "ticket": "330923",
    "fare": 8.0292,
    "cabin": "None"
}
{
    "id": 24,
    "name": "Sloper, Mr. William Thompson",
    "survived": true,
    "sex": "male",
    "age": 28,
    "ticket": "113788",
    "fare": 35.5,
    "cabin": "A6"
}
{
    "id": 25,
    "name": "Palsson, Miss. Torborg Danira",
    "survived": false,
    "sex": "female",
    "age": 8,
    "ticket": "349909",
    "fare": 21.075,
    "cabin": "None"
}
"""