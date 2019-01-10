/************************************************************************/
// include files

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/************************************************************************/
// function prototypes
int fexists(char *fileName);
int morph(char *number);

/************************************************************************/
// main function

int main(int argc,char  **argv){
    char number[32];
    unsigned int numInBin;
    FILE *fid=NULL;
    if(argc != 2){
        printf("Usage: singlePrime filename\n");
        return 2;
    }
    if(fexists(argv[1])){
        fid = fopen(argv[1],"rb");
        fread(&numInBin, sizeof(unsigned int),1,fid);
        fclose(fid);
        sprintf(number,"%u",numInBin);
        morph(number);
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
