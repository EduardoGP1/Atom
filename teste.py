import serial
import time
import keyboard

ser = serial.Serial('COM4', 2000000)# bytesize=8, parity=PARITY_NONE, stopbits=1,
                    #timeout=0, xonxoff=False, rtscts=False, write_timeout=0, dsrdtr=False,
                    #inter_byte_timeout=0, exclusive=0)
contador = 1

while contador <= 179:
    print(contador)
    contador = str(contador)#transforma em string, não sei se seria necessário se programa em c trocasse o "parseint" para outra função
    if keyboard.read_key() == "p":
        ser.write((contador + '\o').encode())#write retorna o tamanho do buffer
    #print (i)
    contador = int(contador)
    contador = contador + 2
    time.sleep (0.01)#tempo mínimo de timasleep conseguido atual é 1.1, menos q isso o robô trava
    if contador >=180:
        while contador >= 2:
            print(contador)
            contador = str(contador)
            ser.write((contador + '\o').encode())#Com a adoção do "+ '\o' no final da mensagem, o delay pode ser reduzido de 1.1 para 0.22
            contador = int(contador)
            contador = contador - 5
            time.sleep(0.21)# Sem um if é preciso usar um delay mínimo para o programa funcionar, se não o braço não consegue entender as informações e não funciona
ser.close()
