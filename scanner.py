#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguements.")
	print("Syntax: python3 scanner.py <IP Address>")

#Add a banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #wont wait for longer time if port is not found
		result = s.connect_ex((target,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:           #Will display "Exiting program" when you ctrl + c
	print("\nExiting program.")
	sys.exit()	
	
except socket.gaierror:             #Will display "Hostname could not be resolved" if hostname isn't resolved
	print("Hostname could not be resolved.") 
	sys.exit()		

except socket.error:                #Will display "Could not connect to server" if it's unable to connect to the server
	print("Could not connect to server.")
	sys.exit()	
	 