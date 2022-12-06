#ifndef OurSem
#define OurSem

#include <stdlib.h>

struct Our_semInit{
    int Lock;
    int val;
};

void unlock(int* x);
int lock(int* x);

void OurSemWait(struct Our_semInit* sem);
void OurSemPost(struct Our_semInit* sem);
int OurSemDestroy(struct Our_semInit * sem);
struct Our_semInit* InitOurSem(int x);


#endif