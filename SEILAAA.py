from pyfirmata import Arduino, util 
import time
from math import log



Uno = Arduino('COM3')
it = util.Iterator(Uno)
it.start()

c1LedVer = 2
c2LedVer = 6
c3LedVer = 7
statusLed1 = 0
statusLed2 = 0
statusLed3 = 0
statusAquecimento1 = 0
statusAquecimento2 = 0
statusAquecimento3 = 0
termistor = Uno.get_pin('a:0:i')
buzzer = 11
rele = 10
botao = 9


# -------------------------------- LIGA/DESLIGA LEDS VERMELHOS(COMODOS)----------------------
def ligaLed():
    global statusLed1
    global statusLed2
    global statusLed3
    
    
    ligaLed = input("Voce quer acender/apagar qual comodo?(c1,c2,c3)")
  
    if ligaLed == 'c1' and statusLed1 == 0:  # C1:  PORTA 2
        Uno.digital[2].write(1)
        print('LED do C1 ligado:')
        time.sleep(1)
        statusLed1 = 1
        print(statusLed1)
    elif ligaLed == 'c1' and statusLed1 == 1:
      Uno.digital[2].write(0)
      print('LED c1 Desligado:')
      time.sleep(1)
      statusLed1 = 0

    if ligaLed == 'c2' and statusLed2 == 0:  # C2:  PORTA 6
        Uno.digital[6].write(1)
        print('LED do C2 ligado:')
        time.sleep(1)
        statusLed2 = 1
    elif ligaLed == 'c2' and statusLed2 == 1:
        Uno.digital[6].write(0)
        print('LED c2 Desligado:')
        statusLed2 = 0
        time.sleep(1)

   if ligaLed == 'c3' and statusLed3 == 0 :  # C1:  PORTA 3
        Uno.digital[7].write(1)
        print('LED do C3 ligado:')
        time.sleep(1)
        statusLed3 = 1
    elif ligaLed == 'c3' and statusLed3 == 1:
      Uno.digital[7].write(0)
      print('LED c3 Desligado:')
      time.sleep(1)
      statusLed3 = 0

    

#--------------------------------------------- LIGA/DESLIGA LEDS DE AQUECIMENTO(LEDS BRANCOS)-----------------------

def aquecimento():
    global statusAquecimento1
    global statusAquecimento2
    global statusAquecimento3
    
    aquecimento = input("Voce quer acender/apagar qual led de Aquecimento?(l1,l2,l3)")
    print('a')
  
    if aquecimento == 'l1' and statusAquecimento1 == 0: # LED BRANCO 1 -  PORTA: 3
        Uno.digital[3].write(1)
        print('LED 1 do Aquecimento ligado:')
        time.sleep(1)
        statusAquecimento1 = 1
        print(statusAquecimento1)
    elif aquecimento == 'l1' and statusAquecimento1 == 1:
      Uno.digital[3].write(0)
      print('LED 1 do Aquecimento Desligado:')
      time.sleep(1)
      statusAquecimento1 = 0
      

    if aquecimento == 'l2' and statusAquecimento2 == 0: # LED BRANCO 2 -  PORTA: 4
        Uno.digital[4].write(1)
        print('LED 2 do Aquecimento ligado:')
        time.sleep(1)
        statusAquecimento2 = 1
    elif aquecimento == 'l2' and statusAquecimento2 == 1:
        Uno.digital[4].write(0)
        print('LED 2 do Aquecimento Deligado:')
        statusAquecimento2 = 0
        time.sleep(1)

    if aquecimento == 'l3' and statusAquecimento3 == 0 :
        Uno.digital[5].write(1)
        print('LED 3 do Aquecimento ligado:')
        time.sleep(1)
        statusAquecimento3 = 1
    elif aquecimento == 'l3' and statusAquecimento3 == 1:  # LED BRANCO 3 -  PORTA: 5
      Uno.digital[5].write(0)
      print('LED 3 do Aquecimento Desligado:')
      time.sleep(1)
      status3 = 0
while True:
    aquecimento()
    ligaLed()
    termistor.enable_reporting()
    valor = str(termistor.read())

    if valor != 'None':
       valor = float(valor)
       temp = obterTempCelsius(valor)
       print (round(obterTempCelsius(valor), 1), 
       '°C')
       Uno.pass_time(5.0)
# ---------------------------------------------------- BUZZER/ RELÉ PARA ATIVAR COOLER -------------------------------------------


    if temp > 25:
        print("Buzzer ativado")
        Uno.digital[11].write(1)
        time.sleep(1)# pausa de 0.01 segundos
        print("Cooler ativado..")
        Uno.digital[10].write(1) 
    else:
        Uno.digital[11].write(0)
        Uno.digital[10].write(0)

#--------------------------------------------- SENSOR DE TEMPERATURA (Termistor) -----------------------

def obterTempCelsius (valor):
    tempK = log(10000.0 * (1.0 / valor - 1))
    tempK = 1 / (0.001129148 + (0.000234125 +
    (0.0000000876741 * tempK * tempK )) * 
    tempK)
    tempC = tempK - 273.15
    return tempC







































    
