
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   char command[150];

   strcpy( command, "gcc sshm.c -o sshm && sudo mv sshm /bin && mv ssh-multi.py /home/$USER && mv config.py /home/$USER" );
   system(command);

   return(0);
} 
