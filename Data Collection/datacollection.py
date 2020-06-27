import serial
import time
import csv

ser = serial.Serial('/dev/cu.HC-05-DevB', baudrate=9600)
ser.flushInput()

ser2 = serial.Serial('/dev/cu.HC-05-SPPDev', baudrate=9600)
ser2.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode("utf-8")
        first_char = len(decoded_bytes) - len(decoded_bytes.lstrip())
        cleaned_bytes = decoded_bytes[first_char:len(decoded_bytes)-1]
        print(cleaned_bytes)

        ser_bytes2 = ser2.readline()
        decoded_bytes2 = ser_bytes2.decode("utf-8")
        first_char2 = len(decoded_bytes2) - len(decoded_bytes2.lstrip())
        cleaned_bytes2 = decoded_bytes2[first_char2:len(decoded_bytes2) - 1]
        print(cleaned_bytes2)

        if decoded_bytes != "" and decoded_bytes2 != "":

            with open("test_data.csv","a") as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([time.asctime(time.gmtime(time.time())),cleaned_bytes,cleaned_bytes2])
    except Exception as e:
        print("Keyboard Interrupt")
        print(e)
        #break
