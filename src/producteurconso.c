#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <semaphore.h>

#define SIZE 8
#define MODULO 500

int prod = 0;
int buffer[SIZE];
int nb_of_producers = 0;
int nb_of_consumers = 0;

int total_production = 0;
int total_consumption = 0;

pthread_mutex_t mutex_buffer; //le buffer est une variable partagée
                              //il faut la mettre dans un mutex

/* Sémpahore

 fonction post : utilisée pour modifier la valeur d'un sémaphore

 Si pas de threads en attente => incrémentation de 1
 Sinon, passe le thread à l'état ready

 fonction wait : utlisée pour tester la valeur d'un sémaphore

 Si la valeur du sémaphore est positive, elle est décrémentée de 1
 Sinon, le thread est bloqué jusqu'à ce qu'un thread face appel à post

*/

int number_of_element = 0;
sem_t empty; //compte le nombre de places vides, intitialisé à 8
sem_t full; //compte le nomnre de places utilisées,intitialisé à 0

void processing_CPU(void){
    int count = 0;
    for (int i = 0; i < 10000; i++)
    {
        count++;
    }    
}

void insert(int index,int item,int id){

    buffer[index] = item;

    //printf(" Buffer item %d added by Producer %d :  Buffer = [", item, id);
    //for (int i = 0; i < SIZE - 1; i += 1) {
      
      //printf("%d,", buffer[i]);
    //}
    //printf("%d]\n", buffer[7]);
}

void remove_element(int index,int id){
    //printf("le consommateur %d accède à sa fonction\n",id);
    //int item_to_remove = buffer[index];
    buffer[index] = 0;

    //printf(" Buffer item %d remove by the Consumer %d :  Buffer = [", item_to_remove, id);
    //for (int i = 0; i < SIZE - 1; i += 1) {
      
      //printf("%d,", buffer[i]);
    //}
    //printf("%d]\n", buffer[7]);
}

void *producers(void *id){
    int id_int = (intptr_t) id;

    int item = (int) random() % MODULO;
    while (total_production < prod){
        //printf("le producteur attend le signal, il a produit %d unités\n",total_production);
        sem_wait(&empty); //attend une place dans le buffer
        pthread_mutex_lock(&mutex_buffer);
            if(total_production != prod){
                insert(number_of_element,item,id_int);
                number_of_element = (number_of_element +1);
                total_production++;
            }
        pthread_mutex_unlock(&mutex_buffer);
        sem_post(&full) ; //incrémente le nombre de place de 1
        //printf("le producteur envoie le signal\n");
        processing_CPU();
    }
    //printf("le producteur sort de la boucle\n");  

    return(NULL);   
}

// Consommateur
void *consumers(void *id){
    int id_int = (intptr_t) id;

    while(total_consumption < prod){
        //printf("Le consommateur %d est bloqué !!!!\n",id_int);
        sem_wait(&full); // attent que le buffer se remplisse
        //printf("Le consommateur %d reçoit le signal\n",id_int);
        pthread_mutex_lock(&mutex_buffer);
                
                if(total_consumption != prod){
                    remove_element(number_of_element-1,id_int);
                    number_of_element = (number_of_element-1);
                    total_consumption++;
                }
                
        pthread_mutex_unlock(&mutex_buffer);
        sem_post(&empty); // il y a une place libre en plus
        //printf("le consommateur %d envoie le signal, il a consommé %d unités\n",id_int,total_consumption);
        processing_CPU();
    }
    //printf("le consommateur %d sort de sa boucle\n",id_int);
    
    if(nb_of_consumers > 1){
        sem_post(&full); //si par malheur un consommateur est encore bloqué
    }
    
    return(NULL);
    
}


int main(int argc, char* argv[]){
    //int err = 0;
    //double time; 
    //clock_t t1,t2;
    //t1 = clock();

    nb_of_consumers = atoi(argv[1]);
    nb_of_producers = atoi(argv[2]);
    prod = atoi(argv[3]);

    pthread_t Consumers_threads[nb_of_consumers];
    pthread_t Producers_threads[nb_of_producers];

    sem_init(&empty, 0, SIZE);
    sem_init(&full, 0, 0);

    pthread_mutex_init(&mutex_buffer,NULL);

        // Create n producers
    for (int i = 0; i < nb_of_producers; i++) {
        
        pthread_create(&Producers_threads[i], NULL, producers, (void *) (intptr_t) i);
        //printf("Created Producer Thread = %ld count = %d \n", Producers_threads[i],i);
    }

    // Create n consumers
    for (int i = 0; i < nb_of_consumers; i++) {
        
        pthread_create(&Consumers_threads[i], NULL, consumers, (void *) (intptr_t) i);
        //printf("Created Consumer Thread = %ld count = %d \n", Consumers_threads[i],i);
    }

        // join all of the producer threads
    for (int i = 0; i < nb_of_producers; i++) {
        
        pthread_join(Producers_threads[i], NULL);
        nb_of_producers--;
        //printf("join Producer thread = %d \n", i);
    }

    // join all of the consumer threads
    for (int i = 0; i < nb_of_consumers; i++) {
        
        pthread_join(Consumers_threads[i], NULL);
        nb_of_consumers--;
        //printf("join Consumer thread = %d \n", i);
    }


    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex_buffer);

    printf("Total items produced = %d and Total items consumed = %d\n", total_production,total_consumption);
    //t2 = clock() - t1;
    //time = ((double)t2)/CLOCKS_PER_SEC;
    //printf("\nTemps de conversion :%.6f\n",time);
    return 0;

}