#include <threads.h>
#include<pthread.h>

pthread_mutex_t mutex_readcount;
pthread_mutex_t mutex_writecount;
pthread_mutex_t mutex;

sem_t wsem;  // accès à la db
sem_t rsem;

int readcount=0; // nombre de readers
int writecount=;

sem_init(&wsem, 0, 1);
sem_init(&rsem,0,1);


void processing_CPU(void){
    int count = 0;
    for (int i = 0; i < 1000; i++)
    {
        count++;
    }    
}

void* writer(void* id){
    int id_int = (intptr_t) id;

    while(total_writings < writings){
            printf("le writer %d accède à sa fonction et est bloqué !!\n",id_int);
            pthread_mutex_lock(&mutex_writecount);
                  printf("le writer %d est débloqué, ouf !\n",id_int);
                  writecount++;
                  if(writecount == 1){
                      printf("le writer %d attend un reader et debloque le mutex\n",id_int);
                      sem_wait(&rsem); //attend plus de readers

                  }
            pthread_mutex_unlock(&mutex_writecount);
            
            printf("le writer %d attend un signal\n",id_int);
            sem_wait(&wsem);
              printf("le writer %d a reçu un signal et lance sa fonction\n",id_int);
              // section critique, un seul writer à la fois
              if(total_writings != writings){
                processing_CPU();
                total_writings++;
              }
            sem_post(&wsem);
            printf("le writer %d envoie un signal wsem et est bloqué\n",id_int);

            pthread_mutex_lock(&mutex_writecount);
                  printf("le writer %d est débloqué, deuxième ouf !\n",id_int);
                  writecount--;
                  if (writecount == 0){
                      printf("le writer %d envoie un signal rsem et debloque le mutex\n",id_int);
                      sem_post(&rsem); //autorise les readers
                  }
            pthread_mutex_unlock(&mutex_writecount);
            printf("le writer %d finit sa boucle\n",id_int);
                      

    }
    printf("le writer %d sort de sa boucle\n",id_int);
            
    return (NULL);
}



void* reader(void* id){
    int id_int = (intptr_t) id;

    while(total_readings < readings){
            printf("le reader %d accède à sa fonction et est bloqué !!\n",id_int);
            
            pthread_mutex_lock(&mutex); //un seul reader à la fois a acces à sem_wait
            printf("le reader %d est débloqué et attend un signal rsem\n",id_int);
                  
            sem_wait(&rsem); //n'avoir qu'un seul reader qui lit
            printf("le reader %d est bloqué et est a reçu son signal rsem\n",id_int);
                  
            pthread_mutex_lock(&mutex_readcount);
              // section critique
              readcount++;
              if (readcount==1)
              { // arrivée du premier reader
                printf("le reader %d est solo et attend wsem\n",id_int);
        
                sem_wait(&wsem);// je suis entrain de lire, vous ne pouvez plus écrire
              }
              if(writecount == 1){
                  printf("le reader %d est bloqué envoie un signal rsem\n",id_int);
                  sem_post(&wsem);
              }
            pthread_mutex_unlock(&mutex_readcount);
            sem_post(&rsem);

   pthread_mutex_unlock(&mutex);

            if(total_readings != readings){
                total_readings++;
                processing_CPU();
            }

   pthread_mutex_lock(&mutex_readcount);
     // section critique
     readcount--;
     if(readcount==0)
     { // départ du dernier reader
       sem_post(&wsem);
     }
   pthread_mutex_unlock(&mutex_readcount);
   process_data();
 }
}

int main(int argc, char* argv[]){
    double time; 
    clock_t t1,t2;
    t1 = clock();

    int nb_readers = atoi(argv[1]);
    int nb_writers = atoi(argv[2]);
    writings = atoi(argv[3]);
    readings = atoi(argv[4]);

    sem_init(&wsem,0,1);
    sem_init(&rsem,0,1);

    pthread_t Readers_threads[nb_readers];
    pthread_t Writers_threads[nb_writers];

    pthread_mutex_init(&mutex_writecount,NULL);
    pthread_mutex_init(&mutex_readcount,NULL);
    pthread_mutex_init(&mutex,NULL);

        // Create n Readers
    for (int i = 0; i < nb_writers; i++) {
        
        pthread_create(&Readers_threads[i], NULL, reader, (void *) (intptr_t) i);
        printf("Created Reader Thread = %ld count = %d \n", Readers_threads[i],i);
    }

    // Create n Write
    for (int i = 0; i < nb_readers; i++) {
        
        pthread_create(&Writers_threads[i], NULL, writer, (void *) (intptr_t) i);
        printf("Created Wrtier Thread = %ld count = %d \n", Writers_threads[i],i);
    }

        // join all of the producer threads
    for (int i = 0; i < nb_writers; i++) {
        
        pthread_join(Readers_threads[i], NULL);
        nb_writers--;
        printf("join Reader thread = %d \n", i);
    }

    // join all of the consumer threads
    for (int i = 0; i < nb_readers; i++) {
        
        pthread_join(Writers_threads[i], NULL);
        nb_readers--;
        printf("join Writer thread = %d \n", i);
    }


    sem_destroy(&wsem);
    sem_destroy(&rsem);
    pthread_mutex_destroy(&mutex_readcount);
    pthread_mutex_destroy(&mutex_writecount);
    pthread_mutex_destroy(&mutex);

    printf("Total items produced = %d and Total items consumed = %d\n", total_readings,total_writings);
    t2 = clock() - t1;
    time = ((double)t2)/CLOCKS_PER_SEC;
    printf("\nTemps de conversion :%.6f\n",time);
    return 1;
}