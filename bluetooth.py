import serial

bluetoothSerial = serial.Serial("/dev/rfcomm0")
bluetoothSerial.baudrate = 9600
bluetoothSerial.bytesize = serial.EIGHTBITS

forward = bytearray()
forward.append(0x10)
forward.append(0x30)

rotate_left = bytearray()
rotate_left.append(0x20)
rotate_left.append(0x10)

rotate_right = bytearray()
rotate_right.append(0x30)
rotate_right.append(0x10)

bluetoothSerial.write(rotate_left)
bluetoothSerial.write(forward)
bluetoothSerial.write(rotate_right)

bluetoothSerial.close()
