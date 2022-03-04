import configparser
import os
import subprocess 
config = configparser.ConfigParser()
config.read("/home/$USER/config.ini")
IP = config["IP"]
print(list(IP))
IN=input("Which computer would you like to connect to| ")
ssh=(IP[IN])
subprocess.run(["ssh", ssh])
