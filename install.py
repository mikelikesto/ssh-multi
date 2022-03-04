import os
import subprocess
subprocess.run(["gcc ssh-multi.c -o sshm"])
subprocess.run(["sudo mv sshm /bin"])
subprocess.run(["mv ssh-multi.py /home/$USER"])
subprocess.run(["mv config.py /home/$USER"])