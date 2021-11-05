#ABIGAIL CHAVEZ
from multiprocessing import Process
class VocParalelo(Process):

    def __init__(self, rarchivo, vocal): #CONSTRUCTOR
        Process.__init__(self) #PROCESO
        self.rarchivo = rarchivo
        self.vocal = vocal

    def run(self): #FUNCION PARA INICIAR PROCESO
        print("NUMERO DE VOCALES " +self.vocal+ " ES: " +str(self.contV()))

    def contV(self):
        cont = 0
        doc = open(self.rarchivo, 'r', encoding="utf-8")
        while doc:
            try:
                letra = doc.read(1)
                if letra.upper() == self.vocal:
                    cont = cont+1
                elif not letra:
                    break
            except UnicodeEncodeError:
                continue
        doc.close()
        return cont

