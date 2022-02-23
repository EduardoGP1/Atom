import cv2
import serial
import time

ser = serial.Serial('COM6', 9600, timeout=10)
a=0

while a==0:

    valor_lido = input("digite o grau de movimento e tecla enter: ")
    ser.write(b'valor_lido')     # write a string
    time.sleep (1)
    print (ser.read(80))
ser.close()