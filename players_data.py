
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

m1=player("Keylor Navas Gamboa",91,55,"Real Madrid","Costa Rica","Goalkeeper",28,85,185,"m1.jpg")
m2=player("Kiko Casilla Cortés",83,55,"Real Madrid","Spain","Goalkeeper",29,84,191,"m2.jpg")
m3=player("Cristiano Ronaldo",55,98,"Real Madrid","Portugal","Shooter",31,80,185,"m3.jpg")
m4=player("Karim Benzema",55,95,"Real Madrid","France","Shooter",28,79,187,"m4.jpg")
m5=player("Sergio Ramos García",55,93,"Real Madrid","Spain","Shooter",30,75,183,"m5.jpg")
m6=player("Gareth Bale",55,92,"Real Madrid","Gales","Shooter",26,74,183,"m6.jpg")
m7=player("Marcelo Vieira da Silva",55,89,"Real Madrid","Brazil","Shooter",28,75,174,"m7.jpg")

j1=player("Gianluigi Buffon",93,55,"Juventus","Italia","Goalkeeper",38,83,191,"j1.jpg")
j2=player("Rubinho Fernando",72,55,"Juventus","Brazil","Goalkeeper",33,82,186,"j2.jpg")
j3=player("Alex Sandro Lobo Silva",55,88,"Juventus","Brazil","Shooter",25,78,180,"j3.jpg")
j4=player("Paul Pogba",55,91,"Juventus","France","Shooter",23,80,188,"j4.jpg")
j5=player("Paulo Dybala",55,91,"Juventus","Argentina","Shooter",22,69,177,"j5.jpg")
j6=player("Mario Mandžukić",55,84,"Juventus","Croatia","Shooter",30,84,187,"j6.jpg")
j7=player("Juan Cuadrado",55,83,"Juventus","Colombia","Shooter",28,66,176,"j7.jpg")

a1=player("Petr Čech",85,55,"Arsenal","Czech Republic","Goalkeeper",34,90,196,"a1.jpg")
a2=player("David Ospina",88,55,"Arsenal","Chile","Goalkeeper",27,79,183,"a2.jpg")
a3=player("Mesut Özil",55,94,"Arsenal","Germany","Shooter",27,76,183,"a3.jpg")
a4=player("Alexis Sánchez",55,88,"Arsenal","Chile","Shooter",27,62,169,"a4.jpg")
a5=player("Olivier Giroud",55,83,"Arsenal","France","Shooter",29,88,192,"a5.jpg")
a6=player("Aaron Ramsey",55,83,"Arsenal","Gales","Shooter",25,70,177,"a6.jpg")
a7=player("Joel Campbell",55,83,"Arsenal","Costa Rica","Shooter",24,72,178,"a7.jpg")

p1=player("Kevin Trapp",84,55,"Paris Saint-Germain","Germany","Goalkeeper",22,88,189,"p1.jpg")
p2=player("Salvatore Sirigu",83,55,"Paris Saint-Germain","Italy","Goalkeeper",29,80,192,"p2.jpg")
p3=player("Zlatan Ibrahimović",55,98,"Paris Saint-Germain","Sweden","Shooter",34,95,195,"p3.jpg")
p4=player("Ángel Di María",55,89,"Paris Saint-Germain","Argentina","Shooter",28,75,180,"p4.jpg")
p5=player("Edinson Cavani",55,86,"Paris Saint-Germain","Uruguay","Shooter",29,71,184,"p5.jpg")
p6=player("Maxwell Scherer",55,87,"Paris Saint-Germain","Brazil","Shooter",34,73,176,"p6.jpg")
p7=player("David Luiz Moreira",55,89,"Paris Saint-Germain","Brazil","Shooter",29,84,189,"p7.jp")

b1=player("Claudio Bravo",83,55,"FC Barcelona","Chile","Goalkeeper",33,80,184,"b1.jp")
b2=player("Marc-André ter Stegen",82,55,"FC Barcelona","Germany","Goalkeeper",24,85,187,"b2.jp")
b3=player("Lionel Messi",55,98,"FC Barcelona","Argentina","Shooter",28,72,170,"b3.jp")
b4=player("Neymar da Silva",55,97,"FC Barcelona","Brazil","Shooter",24,68,174,"b4.jp")
b5=player("Luis Suárez",55,97,"FC Barcelona","Uruguay","Shooter",29,85,182,"b5.jp")
b6=player("Andrés Iniesta",55,95,"FC Barcelona","Spain","Shooter",32,68,171,"b6.jp")
b7=player("Daniel Alves da Silva",55,92,"FC Barcelona","Brazil","Shooter",33,72,172,"b7.jp")

g1=player("Manuel Neuer",92,55,"FC Bayern Munchen","Germany","Goalkeeper",30,92,193,"g1.jp")
g2=player("Sven Ulreich",77,55,"FC Bayern Munchen","Germany","Goalkeeper",27,84,192,"g2.jp")
g3=player("Robert Lewandowski",55,98,"FC Bayern Munchen","Poland","Shooter",27,79,185,"g3.jp")
g4=player("Thomas Müller",55,94,"FC Bayern Munchen","Germany","Shooter",26,75,186,"g4.jp")
g5=player("Arjen Robben",55,91,"FC Bayern Munchen","Holland","Shooter",32,80,180,"g5.jp")
g6=player("Philipp Lahm",55,90,"FC Bayern Munchen","Germany","Shooter",32,66,170,"g6.jp")
g7=player("Mario Götze",55,91,"FC Bayern Munchen","Germany","Shooter",24,72,176,"g7.jp")

lista_madrid=[m1,m2,m3,m4,m5,m6,m7]
lista_juve=[j1,j2,j3,j4,j5,j6,j7]
lista_arsenal=[a1,a2,a3,a4,a5,a6,a7]
lista_psg=[p1,p2,p3,p4,p5,p6,p7]
lista_barsa=[b1,b2,b3,b4,b5,b6,b7]
lista_bayern=[g1,g2,g3,g4,g5,g6,g7]
