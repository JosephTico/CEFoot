
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

lista_madrid=[m1,m2,m3,m4,m5,m6,m7]
lista_juve=[j1,j2,j3,j4,j5,j6,j7]
lista_arsenal=[a1,a2,a3,a4,a5,a6,a7]
lista_psg=[p1,p2,p3,p4,p5,p6,p7]
lista_barsa=[b1,b2,b3,b4,b5,b6,b7]
lista_bayern=[g1,g2,g3,g4,g5,g6,g7]
