import configparser
import os
import subprocess 
config = configparser.ConfigParser()
config.read("config.ini")
IP = config.center["IP"]
subprocess.run(["clear"])
print(list(IP))
IN=input("Which computer would you like to connect to| ")
ssh=(IP[IN])
subprocess.run(["ssh", ssh])
