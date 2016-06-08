
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

p1=player("Keylor Navas Gamboa",91,55,"Madrid","Costa Rica","portero",28,85,185,"NO DISPONIBLE")
p1=player("Kiko Casilla Cortés",83,55,"Madrid","Spain","portero",29,84,191,"NO DISPONIBLE")
p1=player("Cristiano Ronaldo",55,98,"Madrid","Portugal","jugador",31,80,185,"NO DISPONIBLE")
p1=player("Karim Benzema",55,95,"Madrid","France","jugador",28,79,187,"NO DISPONIBLE")
p1=player("Sergio Ramos García",55,93,"Madrid","Spain","jugador",30,75,183,"NO DISPONIBLE")
p1=player("Gareth Bale",55,92,"Madrid","Gales","jugador",26,74,183,"NO DISPONIBLE")
p1=player("Marcelo Vieira da Silva",55,89,"Madrid","Brazil","jugador",28,75,174,"NO DISPONIBLE")

p1=player("Gianluigi Buffon",93,55,"Juventus","Italia","portero",38,83,191,"NO DISPONIBLE")
p1=player("Rubinho Fernando",72,55,"Juventus","Brazil","portero",33,82,186,"NO DISPONIBLE")
p1=player("Alex Sandro Lobo Silva",55,88,"Juventus","Brazil","jugador",25,78,180,"NO DISPONIBLE")
p1=player("Paul Pogba",55,91,"Juventus","France","jugador",23,80,188,"NO DISPONIBLE")
p1=player("Paulo Dybala",55,91,"Juventus","Argentina","jugador",22,69,177,"NO DISPONIBLE")
p1=player("Mario Mandžukić",55,84,"Juventus","Croatia","jugador",30,84,187,"NO DISPONIBLE")
p1=player("Juan Cuadrado",55,83,"Juventus","Colombia","jugador",28,66,176,"NO DISPONIBLE")

p1=player("Petr Čech",85,55,"Arsenal","Czech Republic","portero",34,90,196,"NO DISPONIBLE")
p1=player("David Ospina",88,55,"Arsenal","chile","portero",27,79,183,"NO DISPONIBLE")
p1=player("Mesut Özil",55,94,"Arsenal","Germany","jugador",27,76,183,"NO DISPONIBLE")
p1=player("Alexis Sánchez",55,88,"Arsenal","Chile","jugador",27,62,169,"NO DISPONIBLE")
p1=player("Olivier Giroud",55,83,"Arsenal","France","jugador",29,88,192,"NO DISPONIBLE")
p1=player("Aaron Ramsey",55,83,"Arsenal","Gales","jugador",25,70,177,"NO DISPONIBLE")
p1=player("Joel Campbell",55,83,"Arsenal","Costa Rica","jugador",24,72,178,"NO DISPONIBLE")
p1=player("Theo Walcott",55,81,"Arsenal","England","jugador",27,68,176,"NO DISPONIBLE")

p1=player("Kevin Trapp",84,55,"psg","Germany","portero",22,88,189,"NO DISPONIBLE")
p1=player("Salvatore Sirigu",83,55,"psg","Italy","portero",29,80,192,"NO DISPONIBLE")
p1=player("Zlatan Ibrahimović",55,98,"psg","Sweden","jugador",34,95,195,"NO DISPONIBLE")
p1=player("Ángel Di María",55,89,"psg","Argentina","jugador",28,75,180,"NO DISPONIBLE")
p1=player("Edinson Cavani",55,86,"psg","Uruguay","jugador",29,71,184,"NO DISPONIBLE")
p1=player("Maxwell Scherer",55,87,"psg","Brazil","jugador",34,73,176,"NO DISPONIBLE")
p1=player("David Luiz Moreira",55,89,"psg","Brazil","jugador",29,84,189,"NO DISPONIBLE")

p1=player("Claudio Bravo",83,55,"barcelona","Chile","portero",33,80,184,"NO DISPONIBLE")
p1=player("Marc-André ter Stegen",82,55,"barcelona","Germany","portero",24,85,187,"NO DISPONIBLE")
p1=player("Lionel Messi",55,98,"barcelona","Argentina","jugador",28,72,170,"NO DISPONIBLE")
p1=player("Neymar da Silva",55,97,"barcelona","Brazil","jugador",24,68,174,"NO DISPONIBLE")
p1=player("Luis Suárez",55,97,"barcelona","Uruguay","jugador",29,85,182,"NO DISPONIBLE")
p1=player("Andrés Iniesta",55,95,"barcelona","Spain","jugador",32,68,171,"NO DISPONIBLE")
p1=player("Daniel Alves da Silva",55,92,"barcelona","Brazil","jugador",33,72,172,"NO DISPONIBLE")

p1=player("Manuel Neuer",92,55,"bayern","Germany","portero",30,92,193,"NO DISPONIBLE")
p1=player("Sven Ulreich",77,55,"bayern","Germany","portero",27,84,192,"NO DISPONIBLE")
p1=player("Robert Lewandowski",55,98,"bayern","Poland","jugador",27,79,185,"NO DISPONIBLE")
p1=player("Thomas Müller",55,94,"bayern","Germany","jugador",26,75,186,"NO DISPONIBLE")
p1=player("Arjen Robben",55,91,"bayern","Holland","jugador",32,80,180,"NO DISPONIBLE")
p1=player("Philipp Lahm",55,90,"bayern","Germany","jugador",32,66,170,"NO DISPONIBLE")
p1=player("Mario Götze",55,91,"bayern","Germany","jugador",24,72,176,"NO DISPONIBLE")