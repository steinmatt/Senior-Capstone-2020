import serial 
import numpy as np 
import pandas as pd 
from PIL import Image 

# First: Set up connection to USB Device. 

'''
NOTE: Port is currently commented out. 
This must be changed to the port used for connection of the device. 
(Sometimes changes, unknown why - may be depenent on what USB input used)
'''

ser = serial.Serial() 
ser.baudrate = 115200 
#ser.port = "/dev/ttyUSB7"
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE # set # of stop bits: 1 

# Second: Import picture 
img = np.fromfile('sample-picture.jpg')
img = np.ndarray.flatten(img) 

# Third: Split Flattened picture 128/8 = 16 byte chunks. 
t_length = 16  # number of bytes per tranmission 
s = int(img.shape[0]) / t_length  
img = np.reshape(img, (int(s), t_length)) 

print(img.shape)
print(img) 

# Fourth: Loop to transmit one chunk of data at a time 
for i in range(int(s)): 
    ser.write(img[i])