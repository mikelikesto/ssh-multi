#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   char command[50];

   strcpy( command, "python /home/$USER/ssh-multi.py" );
   system(command);

   return(0);
} 
