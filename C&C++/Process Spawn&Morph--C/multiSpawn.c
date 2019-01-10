/************************************************************************/
// include files
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wait.h>
#include <unistd.h>

/************************************************************************/
// function prototypes
int fexists(char *fileName);
int morph(char *number);

/************************************************************************/
// main function
int main(int argc,char  **argv){
    //mark states the result of program
    //    0 - none prime numbers in the input file
    //    1 - at least one prime numbers in the input file
    int mark = 0;
    int pid,cpid,status,numOfElements;
    char numberInChar[32];
    unsigned int* numInBin;
    int* pidArray;
    FILE *fid=NULL;
    if(argc != 2){
        printf("Usage: singlePrime filename\n");
        return 2;
    }
    if(fexists(argv[1])){
        fid = fopen(argv[1],"rb");
        
        //caculate the vaild number of elements in file
        fseek(fid,0,SEEK_END);
        numOfElements = (int)(ftell(fid)/sizeof(unsigned int));
        fseek(fid,0,SEEK_SET);

        //allocate the memories
        pidArray = (int*)malloc(sizeof(int)*numOfElements);
        numInBin = (unsigned int*)malloc(sizeof(unsigned int)*numOfElements);
        
        //read the ellements from file
        fread(numInBin, sizeof(unsigned int),numOfElements,fid);
        fclose(fid);
        //spwan children process
        for(int i=0;i<numOfElements;i++){
            sprintf(numberInChar,"%u",numInBin[i]);
            //printf("%s\n",numberInChar);
            pid = fork();
            if(pid==0){
                //child process
                morph(numberInChar);
            }else{
            //parent process
                pidArray[i] = pid;
                //printf("%d\n",*pidArray);
            }
        }
        
        
        //wait children processes termination
        while(1){
            cpid = waitpid(-1, &status, 0);
            if (cpid == -1){
                break;
            }
            if(status){
                for(int i=0; i<numOfElements;i++){

                    if (pidArray[i] == cpid){
                        printf("%u\n",numInBin[i]);
                        mark = 1;
                        break;
                    }
                }
            }
        }
        
        //free the memories
        free(numInBin);
        free(pidArray);
        return mark;
    }
    printf("file %s does not exist\n",argv[1]);
    return 3;
}


/************************************************************************/
// Return whether the given file exists in the current directory.
int fexists(char *fileName)
{
   FILE *fp = NULL;
    int rc = 0;

	// open the file

    fp = fopen(fileName, "rb");

	// determine the recturn code
	if(fp == NULL){
		rc = 0;
	}else{
		fclose(fp);
		rc = 1;
	}


    return(rc);
}

/************************************************************************/
// create the array of shell commands and morph the program
int  morph(char *number){
    char *param[3];
    param[0] = "isPrime";
    param[1] = number;
    param[2] = NULL;
    execv("isPrime",param);
    printf("failed to morph\n");
    return -1;
}
