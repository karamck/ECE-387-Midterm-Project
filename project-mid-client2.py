# project-mid-client2.py
# Author: Christopher Karam

import socket       # Required to create a network
import sys          # Required to read command lines
from gpiozero import LED, Button

# Recommended for controling loops and methods
connected = False

# Instance variables and methods ###############################################
#
# Here is where I set all methods and variables for my client program. Each
# method has an explination, but this is where all application specific
# methods and variables would go.

#button setup
btn1 = Button(4)
btn2 = Button(17)
btn3 = Button(27)
btn4 = Button(22)
btn_close = Button(26) #button to manualy close the server

#led setup
led1 = LED(23)
led2 = LED(24)
led3 = LED(25)
led4 = LED(13)



# Method for reading button inputs.
# Creates a string of 1's and 0's of each button combined.
# 0 for pressed and 1 otherwise (compare to project-mid-client1.py).
# Also checks if the close button was pressed to close the socket.
#
# Input: the socket object
# Output: string containing each button's state
def checking_buttons(sock):
    if btn_close.is_pressed :
        print("CLOSING CONNECTION!")
        sock.close()
        connected = False
        return None
    
    if btn1.is_pressed :
        b1 = "0"
    else :
        b1 = "1"
    if btn2.is_pressed :
        b2 = "0"
    else :
        b2 = "1"
    if btn3.is_pressed :
        b3 = "0"
    else :
        b3 = "1"
    if btn4.is_pressed :
        b4 = "0"
    else :
        b4 = "1"
    return b1+b2+b3+b4

# Method that matches each character in data to the respective LED.
# (Compare to project-mid-client1.py)
#
# Input: data received by the server that was concverted to a string
def write_led(data):
    if data[0] == "0" :
        led1.on()
    else :
        led1.off()
    if data[1] == "0" :
        led2.on()
    else :
        led2.off()
    if data[2] == "0" :
        led3.on()
    else :
        led3.off()
    if data[3] == "0" :
        led4.on()
    else :
        led4.off()
        
# Recommended #################################################################
#
# Should be included to check that the command line input is correct. The port
# entered should be the same as the server program and the host should be the
# IPv4 of the server pi.

# make sure the command line input is correct
if len(sys.argv) != 3:
    print("invalid command line: <host> <port>")
    sys.exit(1)

# Main Body of Code #########################################################
#
# This code is slightly simpler than the server because all it needs to do
# is connect. There is no waiting or accepting involved. Once it is connected
# simply start a loop until the connection is lost and communicate with the server.

# setting the host and port to their intended values
host, port = sys.argv[1], int(sys.argv[2])

# Creating the socket object of the client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Connect to the server
    s.connect((host,port))
    connected = True
    print('Connected to', (host,port))
    while connected:

        # Sending a message to the server, breaks if close button was pressed
        outMessage = checking_buttons(s)
        if not outMessage:
            break
        outMessage = outMessage.encode('utf-8')
        s.sendall(outMessage)

        # Check for if the server closed or told the client to close, If not, control the LEDs
        data = s.recv(1024)
        data = data.decode('utf-8')
        if len(data) == 0 or len(data) > 4 :
            print("Server closed")
            break
        write_led(data)


