# project-mid-server.py
# Author: Christopher Karam

import socket   # Required to create a network
import sys      # Required to read command lines
from gpiozero import LED, Button

# Required Variables for Server ############################################

HOST = '192.168.0.2' # static IPv4 address of this pi, can be changed depending on what static ip is set
connected = False   # Boolean for connection aids in controling loops and methods


# Instance variables and methods ###########################################
#
# Here is where I set all methods and variables for my server program. Each method
# has an explination, but this is where application specific methods and variables should go

#led setup
led1 = LED(4)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)

#button setup
btn1 = Button(23)
btn2 = Button(24)
btn3 = Button(25)
btn4 = Button(13)
btn_reset = Button(26) #button to manually close the server

# Method that matches each character in data to the respective LED.
#
# Input: data received by the server that was converted to a string
def write_led(data):
    if data[0] == "1":
        led1.on()
    else :
        led1.off()
    if data[1] == "1":
        led2.on()
    else :
        led2.off()
    if data[2] == "1":
        led3.on()
    else :
        led3.off()
    if data[3] == "1":
        led4.on()
    else :
        led4.off()

# method to turn off all LEDs
def reset_leds():
    led1.off()
    led2.off()
    led3.off()
    led4.off()

# Method for reading button inputs.
# Creates a string of 1's and 0's of each button combined.
# 1 for pressed and 0 otherwise.
# Also reads the input of the reset button.
#
# Input: socket object
# Output: string
def checking_buttons(sock):
    if btn_reset.is_pressed :
        print("CLOSING SOCKET SERVER")
        connected = False
        return "close"

    if btn1.is_pressed :
        b1 = "1"
    else :
        b1 = "0"
    if btn2.is_pressed :
        b2 = "1"
    else :
        b2 = "0"
    if btn3.is_pressed :
        b3 = "1"
    else :
        b3 = "0"
    if btn4.is_pressed :
        b4 = "1"
    else :
        b4 = "0"
    return b1+b2+b3+b4

# Recommended ############################################################
#
# Should be included to check that the command line input is correct. The
# port number entered should be the same port entered on the client.

# Make sure the command line is correct
if len(sys.argv) != 2 :
    print("invalid command line: <port>")
    sys.exit(1)


# Main Body of Code #############################################################
#
# The try exception is so that the server can be terminated by the keyboard input
# ^C. The code below creates a socket s and tells it was ports to listen on.
# Because the host is the pi's own IP address it will be the server. Once the
# client tries to connect to the port, the server accepts and code can be executed
# to communicate over the network.

# Read in port from the command line
port = int(sys.argv[1])

try:
    #loop allows for re-opening socket after client closes
    while True :
        reset_leds()
        
        # creating the socket object of server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            #open the port and wait for the client connection
            s.bind((HOST, port))
            print("Waiting for connection...")
            s.listen(1)
            connection, addr = s.accept()

            # Runs only if the server is connected to a client
            with connection:
                print('Connected by', addr)
                connected = True
                while connected:
                    data = connection.recv(1024)

                    # if no data is sent from the client, connection is lost
                    if not data:
                        connected = False
                        print('Connection closed by', addr)
                        break

                    # data must be decoded to be read as a string
                    data = data.decode('utf-8')
                    write_led(data)

                    #sending and encoding a message to client
                    outMessage = checking_buttons(s)
                    outMessage = outMessage.encode('utf-8')
                    connection.sendall(outMessage)

        #closing the socket so it can be reopened at the next loop
        s.close()
        
except KeyboardInterrupt:
    print("\nKeyboard Interrupt! closing program")
            

