#ABIGAIL CHÁVEZ
class VocSerial():
    def __init__(self, rarchivo): #CONSTRUCTOR
        self.rarchivo = rarchivo

    #VOCAL A
    def vocalesA(self):
        doc= open(self.rarchivo, "r", encoding= 'utf-8') #ABRE ARCHIVO DE RUTA QUE SE PASA POR PARÁMETRO, CODIFICACION DE LOS ARCHIVOS UTF-8
        cont = 0
        while doc:
            try:
                letra = doc.read(1) #LEE CARACTER A CARACTER EL CONTENIDO DEL FICHERO
                if letra.upper()=="A":
                    cont=cont+1
                elif not letra:
                    break

            except UnicodeEncodeError:
                continue
        doc.close()
        return cont


    #VOCAL E
    def vocalesE(self):
        doc= open(self.rarchivo, "r", encoding= 'utf-8') #ABRE ARCHIVO DE RUTA QUE SE PASA POR PARÁMETRO, CODIFICACION DE LOS ARCHIVOS UTF-8
        cont = 0
        while doc:
            try:
                letra = doc.read(1) #LEE CARACTER A CARACTER EL CONTENIDO DEL FICHERO
                if letra.upper()=="E":
                    cont=cont+1
                elif not letra:
                    break

            except UnicodeEncodeError:
                continue
        doc.close()
        return cont

    #VOCAL I
    def vocalesI(self):
        doc= open(self.rarchivo, "r", encoding= 'utf-8') #ABRE ARCHIVO DE RUTA QUE SE PASA POR PARÁMETRO, CODIFICACION DE LOS ARCHIVOS UTF-8
        cont = 0
        while doc:
            try:
                letra = doc.read(1) #LEE CARACTER A CARACTER EL CONTENIDO DEL FICHERO
                if letra.upper()=="I":
                    cont=cont+1
                elif not letra:
                    break

            except UnicodeEncodeError:
                continue
        doc.close()
        return cont

    #VOCAL O
    def vocalesO(self):
        doc= open(self.rarchivo, "r", encoding= 'utf-8') #ABRE ARCHIVO DE RUTA QUE SE PASA POR PARÁMETRO, CODIFICACION DE LOS ARCHIVOS UTF-8
        cont = 0
        while doc:
            try:
                letra = doc.read(1) #LEE CARACTER A CARACTER EL CONTENIDO DEL FICHERO
                if letra.upper()=="O":
                    cont=cont+1
                elif not letra:
                    break

            except UnicodeEncodeError:
                continue
        doc.close()
        return cont

    #VOCAL U
    def vocalesU(self):
        doc= open(self.rarchivo, "r", encoding= 'utf-8') #ABRE ARCHIVO DE RUTA QUE SE PASA POR PARÁMETRO, CODIFICACION DE LOS ARCHIVOS UTF-8
        cont = 0
        while doc:
            try:
                letra = doc.read(1) #LEE CARACTER A CARACTER EL CONTENIDO DEL FICHERO
                if letra.upper()=="U":
                    cont=cont+1
                elif not letra:
                    break

            except UnicodeEncodeError:
                continue
        doc.close()
        return cont