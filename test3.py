import time
with open('/dev/hidg0', 'wb') as f:
    f.write(bytes([0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00])) 