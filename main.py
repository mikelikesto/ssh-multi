import configparser #imports configparser, an module that makes it possiable to read config files
import os
import subprocess #imports subprocess, which makes it possiable to do system commands

config = configparser.ConfigParser()#sets the name config to = configparser
config.read("config.ini")#reads the config file
IP = config["IP"]#sets the row IP to = IP 
print(list(IP))#prints avablibe ips on the IP row
IN=input("Which computer would you like to connect to| ")#ask the user what computer do they want to connect to and sets the users in put to "IN"
ssh=(IP[IN])#sets the name ssh to = IP{the row ip} and IN {the users input}
subprocess.run(["ssh", ssh]) # runs ssh with the verable ssh {the set ip}
