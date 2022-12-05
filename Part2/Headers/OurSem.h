#ifndef OurSem
#define OurSem

#include <stdlib.h>

struct Our_semInit{
    int Lock;
    int val;
};

int unlock(int* x);
int lock(int* x);

void OurSemWait(struct Our_semInit* sem);
void OurSemPost(struct Our_semInit* sem);
int OurSemDestroy(struct Our_semInit * sem);


#endif