import json, os

class player:
    def __init__(self,name,port,glob,team,pais,tipo,edad,peso,altura,foto):
        self.name=name
        self.glob=glob
        self.port=port
        self.team=team
        self.pais=pais
        self.tipo=tipo
        self.edad=edad
        self.peso=peso
        self.altura=altura
        self.foto=foto
        self.goles=0
    def gol(self):
        self.goles+=1
    def printall(self):
        print(self.name)
        print(self.glob)
        print(self.pais)
        print(self.tipo)
        print(self.edad)
        print(self.peso)
        print(self.altura)
        print(self.goles)



lista_madrid=[]
lista_juve=[]
lista_arsenal=[]
lista_psg=[]
lista_barsa=[]
lista_bayern=[]


players_file = open(os.path.join("data", "players.json"), encoding='utf-8')


with players_file as data_file:    
    data = json.load(data_file)

for p in data["madrid"]:
    obj = player(p["name"], p["glob"], p["port"], p["team"], p["pais"], p["tipo"], p["edad"], p["peso"], p["altura"], p["foto"])
    lista_madrid.append(obj)

for p in data["juve"]:
    obj = player(p["name"], p["glob"], p["port"], p["team"], p["pais"], p["tipo"], p["edad"], p["peso"], p["altura"], p["foto"])
    lista_juve.append(obj)

for p in data["arsenal"]:
    obj = player(p["name"], p["glob"], p["port"], p["team"], p["pais"], p["tipo"], p["edad"], p["peso"], p["altura"], p["foto"])
    lista_arsenal.append(obj)

for p in data["psg"]:
    obj = player(p["name"], p["glob"], p["port"], p["team"], p["pais"], p["tipo"], p["edad"], p["peso"], p["altura"], p["foto"])
    lista_psg.append(obj)

for p in data["barsa"]:
    obj = player(p["name"], p["glob"], p["port"], p["team"], p["pais"], p["tipo"], p["edad"], p["peso"], p["altura"], p["foto"])
    lista_barsa.append(obj)

for p in data["bayern"]:
    obj = player(p["name"], p["glob"], p["port"], p["team"], p["pais"], p["tipo"], p["edad"], p["peso"], p["altura"], p["foto"])
    lista_bayern.append(obj)