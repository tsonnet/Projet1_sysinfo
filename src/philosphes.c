#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>


int PHILOSOPHES=0;
int NBaguette=0;
pthread_t* phil;
pthread_mutex_t* baguette;

void* philosophe ( void* arg )
{
    int id = *((int*)arg);
    int n=0;
    int left = id;
    int right = (left + 1) % NBaguette;
    while(n < 100000) {
        // philosophe pense
        if(left<right) {
            pthread_mutex_lock(&baguette[left]);
            pthread_mutex_lock(&baguette[right]);
        }
        else {
            pthread_mutex_lock(&baguette[right]);
            pthread_mutex_lock(&baguette[left]);
        }
        //mange(id);
        pthread_mutex_unlock(&baguette[left]);
        pthread_mutex_unlock(&baguette[right]);
        n++;
    }
    return (NULL);
}


int main(int argc, char* argv[]){
    if (argc > 1){
        PHILOSOPHES = atoi(argv[1]);
    }
    NBaguette=PHILOSOPHES;
    if(PHILOSOPHES == 1) NBaguette = PHILOSOPHES+1;
    int* id = malloc(sizeof(int)*PHILOSOPHES+1);
    phil = malloc(PHILOSOPHES*sizeof(pthread_t)+1);
    baguette = malloc(sizeof(pthread_mutex_t)*NBaguette+1);
    for( int i=0 ; i< PHILOSOPHES;i++){
        pthread_mutex_init(baguette+i,NULL);
    }
    for(int i =0; i< PHILOSOPHES;i++){
        id[i]=i;
        pthread_create(phil+i, NULL ,philosophe,(void *) &(id[i]));
    }
    for(int i =0; i< PHILOSOPHES;i++){
        pthread_join(phil[i],NULL);
    }
    free(phil);
    free(baguette);
    free(id);
    return 0;
}