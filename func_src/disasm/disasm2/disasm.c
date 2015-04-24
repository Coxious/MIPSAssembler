#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


#define MAX_SIZE 1000


char getValue(char ch)
{
  if( (ch >= '0') && (ch <= '9') )
  {
    return ch - '0';
  }
  else if( (ch >= 'a') && (ch <= 'f') )
  {
    return ch - 'a' + 10;
  }
  else if( (ch >= 'A') && (ch <= 'F') )
  {
    return ch - 'A' + 10;
  }
  else
  {
    return -1;
  }
}


int getByte(char * buffer)
{
  int high, low;
  
  high = getValue(buffer[0]);
  low  = getValue(buffer[1]);
  
  if( (high == -1) || (low == -1) )
  {
    return -1;
  }
  
  return ( (high << 4) + low );
}


int main(int argc, char * argv[])
{
  int fd, i, n;
  char buffer[MAX_SIZE];
  char tempFile[20];
  char str[300];
  while(1)
  {
    strcpy(tempFile, "tmp_XXXXXX");
    
    if( (fd=mkstemp(tempFile)) == -1)
    {
      perror("temp file create failed!\n");
      exit(1);
    }
  
    printf("> ");
    fgets(buffer, MAX_SIZE, stdin);
  
    /* get rid of the last character: '\n' */
    for(i=0; i<strlen(buffer)-1; i+=2)
    {
      n = getByte(buffer + i);
      if(n == -1)
      {
        printf("unknown character!\n");
        goto next;
      }
      write(fd, (char *)&n, 1);
    }
    
    next:
    sprintf(str, "mipsel-linux-objdump -D -m mips -b binary %s | sed \'1, 7d\'", tempFile);
    system(str);
    close(fd);
    /* delete temp file */
    unlink(tempFile);
  }

  return 0;
}
