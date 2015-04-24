#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int fileExist(char * fileName)
{
  if((access(fileName, F_OK)) == 0)
  {
    return 1;
  }
  else
  {
    return 0;
  }
}


void printUsage()
{
  printf("usage: disasm filename\n");
}


int main(int argc, char * argv[])
{
  if(argc != 2)
  {
    printUsage();
    exit(1);
  }
  
  if(!fileExist(argv[1]))
  {
    printf("\'%s\' not exist!\n", argv[1]);
    exit(1);
  }

  char str[300];
  sprintf(str, "mipsel-linux-objdump -D -m mips -b binary %s | sed \'1, 7d\'", argv[1]);
  system(str);

  return 0;
}
