
# ***atentar-se para responsabilidade única de cada classe***
class CreateTask:
    def __init__(self, titulo: str, descript: str):
        self.titulo = titulo
        self.descript = descript
        self.situation = False

    def criarTask(self):
        task = {
            "titulo": self.titulo,
            "descrição": self.descript,
            "situação": self.situation

        }
        self.computarTask(task)
    #
    # *** Mover a resdponsabilidade de computar task para outra classe ***
    #
    def computarTask(task):
        taskList = []
        taskList.append(task)

    

    def concluirTask(self):
        self.situation = True
    

        

