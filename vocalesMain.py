from vocalesSerial import VocSerial
from vocalesParalelo import VocParalelo
import time

if __name__ == "__main__":
    ruta = input("Introduce la ruta del archivo: ")
    tiempoISerial = time.perf_counter() #INICIA CRONÓMETRO

    #PROGRAMA 1 : CONTAR VOCALES SERIAL (1 PROCESO)
    #CONTRUYE OBJETO DE TIPO VOCSERIAL PASANDO LA RUTA (EJECUTA EL PROGRAMA VOCSERIAL)
    prueba1 = VocSerial(ruta)
    #LLAMA A LAS FUNCIONES DEL OBJETO PRUEBA1 (CUENTA LAS DIFERENTES VOCALES)
    print("NUMERO DE VOCALES A: " +str(prueba1.vocalesA()))
    print("NUMERO DE VOCALES E: " + str(prueba1.vocalesE()))
    print("NUMERO DE VOCALES I: " + str(prueba1.vocalesI()))
    print("NUMERO DE VOCALES O: " + str(prueba1.vocalesO()))
    print("NUMERO DE VOCALES U: " + str(prueba1.vocalesU()))
    tiempoFSerial = time.perf_counter()-tiempoISerial #FINALIZA CRONOMETRO
    print("TIEMPO DE EJECUCION: " +str(round(tiempoFSerial,3))) #MUESTRA TIEMPO DE EJECUCION SERIAL REDONDEADO A 3

    print("-------------------------------------------------")

    #PROGRAMA 2 : CONTAR VOCALES PARALELO
    tiempoIParalelo = time.perf_counter()  # INICIA CRONOMETRO
    #PROCESOS:
    vocalA = VocParalelo(ruta, "A")
    vocalE = VocParalelo(ruta, "E")
    vocalI = VocParalelo(ruta, "I")
    vocalO = VocParalelo(ruta, "O")
    vocalU = VocParalelo(ruta, "U")

    #INICIAR PROCESOS:
    vocalA.start()
    vocalE.start()
    vocalI.start()
    vocalO.start()
    vocalU.start()

    #INDICAR A SUBPROCESOS QUE ESPEREN AL PROCESO PADRE:
    vocalA.join()
    vocalE.join()
    vocalI.join()
    vocalO.join()
    vocalU.join()

    tiempoFParelelo = time.perf_counter()-tiempoIParalelo #FINALIZA CRONOMETRO
    print("TIEMPO DE EJECUCION: " +str(round(tiempoFParelelo,3))) #MUESTRA TIEMPO DE EJECUCION PARALELO REDONDEADO A TRES DECIMALES