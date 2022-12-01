#include "../Headers/OurSem.h"
#include <stdlib.h>


int enter(int* x){
    asm(
        "enterhere:"
        "movl $1, %%eax;"
        "xchgl %%eax, (%1);"

        "testl %%eax, %%eax;"
        "jnz enterhere;"

        :"=r"(x)  /* x is output operand */
        :"r"(x)   /* x is input operand */
        :"%eax" /* %eax is clobbered register */
    );
}

int leave(int* x){
    asm(
        "movl $0, %%eax;"
        "xchgl %%eax, (%1);"

        :"=r"(x)  /* x is output operand */
        :"r"(x)   /* x is input operand */
        :"%eax" /* %eax is clobbered register */
    );
}


void TestAndTestAndSet(int * lock){

    while (enter(lock))
    {
        while (*lock){}  
    }
    
}



void OurSemPost(int* x){
    leave(x);
}

void OurSemWait(int* x){
    TestAndTestAndSet(x);
}