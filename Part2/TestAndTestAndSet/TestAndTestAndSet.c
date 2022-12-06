#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>




int lock=0;

int enterTestAndSet(int* x){
    int to_ret;
    asm(
        "movl $1, %%eax;"
        "xchgl %%eax, (%1);"
        "movl %%eax, %0"

        :"=r"(to_ret)  /* x is output operand */
        :"r"(x)   /* x is input operand */
        :"%eax"/* %eax is clobbered register */
    );
    return to_ret;
}

void leave(int* x){
    asm(
        "movl $0, %%eax;"
        "xchgl %%eax, (%1);"

        :"=r"(x)  /* x is output operand */
        :"r"(x)   /* x is input operand */
        :"%eax" /* %eax is clobbered register */
    );
}




void TestAndTestAndSet(int *x){

    while(enterTestAndSet(x))
    {
        while (*x){}  
    } 
}

void* Action(void* N){
    int Nit = *((int*) N);
    for(int i=0; i< Nit ;i++){

        TestAndTestAndSet(&lock);
        for (int j=0; j<10000; j++);
        leave(&lock);

    }
    return N;
}

int main(int argc, char* argv[]){
    int Nthread = atoi(argv[1]);
    pthread_t *thread = malloc(Nthread*sizeof(pthread_t));
    int ActionPerThread = 6400/Nthread;
    for(int i =0; i < Nthread; i++){
        pthread_create(thread+i,NULL,Action,(void *)&ActionPerThread);
    }
    for(int i =0; i< Nthread; i++){
        pthread_join(thread[i],NULL);
    }
    free(thread);
    return 0;
}