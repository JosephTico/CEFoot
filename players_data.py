
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

m1=player("Keylor Navas Gamboa",91,55,"Real Madrid","Costa Rica","portero",28,85,185,"NO DISPONIBLE")
m2=player("Kiko Casilla Cortés",83,55,"Real Madrid","Spain","portero",29,84,191,"NO DISPONIBLE")
m3=player("Cristiano Ronaldo",55,98,"Real Madrid","Portugal","jugador",31,80,185,"NO DISPONIBLE")
m4=player("Karim Benzema",55,95,"Real Madrid","France","jugador",28,79,187,"NO DISPONIBLE")
m5=player("Sergio Ramos García",55,93,"Real Madrid","Spain","jugador",30,75,183,"NO DISPONIBLE")
m6=player("Gareth Bale",55,92,"Real Madrid","Gales","jugador",26,74,183,"NO DISPONIBLE")
m7=player("Marcelo Vieira da Silva",55,89,"Real Madrid","Brazil","jugador",28,75,174,"NO DISPONIBLE")

j1=player("Gianluigi Buffon",93,55,"Juventus","Italia","portero",38,83,191,"NO DISPONIBLE")
j2=player("Rubinho Fernando",72,55,"Juventus","Brazil","portero",33,82,186,"NO DISPONIBLE")
j3=player("Alex Sandro Lobo Silva",55,88,"Juventus","Brazil","jugador",25,78,180,"NO DISPONIBLE")
j4=player("Paul Pogba",55,91,"Juventus","France","jugador",23,80,188,"NO DISPONIBLE")
j5=player("Paulo Dybala",55,91,"Juventus","Argentina","jugador",22,69,177,"NO DISPONIBLE")
j6=player("Mario Mandžukić",55,84,"Juventus","Croatia","jugador",30,84,187,"NO DISPONIBLE")
j7=player("Juan Cuadrado",55,83,"Juventus","Colombia","jugador",28,66,176,"NO DISPONIBLE")

a1=player("Petr Čech",85,55,"Arsenal","Czech Republic","portero",34,90,196,"NO DISPONIBLE")
a2=player("David Ospina",88,55,"Arsenal","chile","portero",27,79,183,"NO DISPONIBLE")
a3=player("Mesut Özil",55,94,"Arsenal","Germany","jugador",27,76,183,"NO DISPONIBLE")
a4=player("Alexis Sánchez",55,88,"Arsenal","Chile","jugador",27,62,169,"NO DISPONIBLE")
a5=player("Olivier Giroud",55,83,"Arsenal","France","jugador",29,88,192,"NO DISPONIBLE")
a6=player("Aaron Ramsey",55,83,"Arsenal","Gales","jugador",25,70,177,"NO DISPONIBLE")
a7=player("Joel Campbell",55,83,"Arsenal","Costa Rica","jugador",24,72,178,"NO DISPONIBLE")

p1=player("Kevin Trapp",84,55,"Paris Saint-Germain","Germany","portero",22,88,189,"NO DISPONIBLE")
p2=player("Salvatore Sirigu",83,55,"Paris Saint-Germain","Italy","portero",29,80,192,"NO DISPONIBLE")
p3=player("Zlatan Ibrahimović",55,98,"Paris Saint-Germain","Sweden","jugador",34,95,195,"NO DISPONIBLE")
p4=player("Ángel Di María",55,89,"Paris Saint-Germain","Argentina","jugador",28,75,180,"NO DISPONIBLE")
p5=player("Edinson Cavani",55,86,"Paris Saint-Germain","Uruguay","jugador",29,71,184,"NO DISPONIBLE")
p6=player("Maxwell Scherer",55,87,"Paris Saint-Germain","Brazil","jugador",34,73,176,"NO DISPONIBLE")
p7=player("David Luiz Moreira",55,89,"Paris Saint-Germain","Brazil","jugador",29,84,189,"NO DISPONIBLE")

b1=player("Claudio Bravo",83,55,"FC Barcelona","Chile","portero",33,80,184,"NO DISPONIBLE")
b2=player("Marc-André ter Stegen",82,55,"FC Barcelona","Germany","portero",24,85,187,"NO DISPONIBLE")
b3=player("Lionel Messi",55,98,"FC Barcelona","Argentina","jugador",28,72,170,"NO DISPONIBLE")
b4=player("Neymar da Silva",55,97,"FC Barcelona","Brazil","jugador",24,68,174,"NO DISPONIBLE")
b5=player("Luis Suárez",55,97,"FC Barcelona","Uruguay","jugador",29,85,182,"NO DISPONIBLE")
b6=player("Andrés Iniesta",55,95,"FC Barcelona","Spain","jugador",32,68,171,"NO DISPONIBLE")
b7=player("Daniel Alves da Silva",55,92,"FC Barcelona","Brazil","jugador",33,72,172,"NO DISPONIBLE")

g1=player("Manuel Neuer",92,55,"FC Bayern Munchen","Germany","portero",30,92,193,"NO DISPONIBLE")
g2=player("Sven Ulreich",77,55,"FC Bayern Munchen","Germany","portero",27,84,192,"NO DISPONIBLE")
g3=player("Robert Lewandowski",55,98,"FC Bayern Munchen","Poland","jugador",27,79,185,"NO DISPONIBLE")
g4=player("Thomas Müller",55,94,"FC Bayern Munchen","Germany","jugador",26,75,186,"NO DISPONIBLE")
g5=player("Arjen Robben",55,91,"FC Bayern Munchen","Holland","jugador",32,80,180,"NO DISPONIBLE")
g6=player("Philipp Lahm",55,90,"FC Bayern Munchen","Germany","jugador",32,66,170,"NO DISPONIBLE")
g7=player("Mario Götze",55,91,"FC Bayern Munchen","Germany","jugador",24,72,176,"NO DISPONIBLE")

lista_madrid=[m1,m2,m3,m4,m5,m6,m7]
lista_juve=[j1,j2,j3,j4,j5,j6,j7]
lista_arsenal=[a1,a2,a3,a4,a5,a6,a7]
lista_psg=[p1,p2,p3,p4,p5,p6,p7]
lista_barsa=[b1,b2,b3,b4,b5,b6,b7]
lista_bayern=[g1,g2,g3,g4,g5,g6,g7]
