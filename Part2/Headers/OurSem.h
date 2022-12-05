#ifndef OurSem
#define OurSem

#include <stdlib.h>

struct Our_semInit{
    int Lock;
    int val;
};
<<<<<<< HEAD

int unlock(int* x);
int lock(int* x);
=======
void unlock(int* x);
int* lock(int* x);
void OurSemWait(struct Our_semInit* sem);
void OurSemWait(struct Our_semInit* sem);
>>>>>>> refs/remotes/origin/main

void OurSemWait(struct Our_semInit* sem);
void OurSemPost(struct Our_semInit* sem);
int OurSemDestroy(struct Our_semInit * sem);


#endif