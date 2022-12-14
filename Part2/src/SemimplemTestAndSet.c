#include "../Headers/OurSem.h"
#include <stdlib.h>
#include <stdio.h>

int lock(int* x){
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
    return *x;
}

void unlock(int* x){
    asm(
        "movl $0, %%eax;"
        "xchgl %%eax, (%1);"

        :"=r"(x)  /* x is output operand */
        :"r"(x)   /* x is input operand */
        :"%eax" /* %eax is clobbered register */
    );
}



struct Our_semInit* InitOurSem(int x){
    struct Our_semInit* my_sem = malloc(sizeof(struct Our_semInit));
    my_sem->val=x;
    my_sem->Lock=0;
    return my_sem;
}

int OurSemDestroy(struct Our_semInit * sem){
    free(sem);
    return 0;
}

void OurSemPost(struct Our_semInit* sem){
    lock(&(sem->Lock));
    sem->val+=1;
    unlock(&(sem->Lock));

}


void OurSemWait(struct Our_semInit* sem){
    while (1)
    {
        if(sem->val>0){
            lock(&(sem->Lock));    
            if(sem->val>0){
                sem->val-=1;
                unlock(&(sem->Lock));
                break;
            }        
            unlock(&(sem->Lock));
        }
    }
}