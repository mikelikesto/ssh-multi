import os
import subprocess
subprocess.run(["gcc sshm.c -o sshm && sudo mv sshm /bin && mv ssh-multi.py /home/$USER && mv config.py /home/$USER"])
#subprocess.run(["sudo mv sshm /bin"])
#subprocess.run(["mv ssh-multi.py /home/$USER"])
#subprocess.run(["mv config.py /home/$USER"])
