import serial
import time

ser = serial.Serial('COM4', 2000000)
contador = 1

while contador <= 179:
    print(contador)
    contador = str(contador)
    ser.write(contador.encode())
    print(ser.out_waiting)
    contador = int(contador)
    contador = contador + 5
    time.sleep (3)
    if contador >=180:
        while contador >= 2:
            print(contador)
            contador = str(contador)
            ser.write(contador.encode())
            contador = int(contador)
            contador = contador - 5
            time.sleep(1.1)
ser.close
