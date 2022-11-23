#include <threads.h>

pthread_mutex_t mutex_readcount;
pthread_mutex_t mutex_writecount;
pthread_mutex_t mutex;

sem_t wsem;  // accès à la db
sem_t rsem;

int readcount=0; // nombre de readers
int writecount=;

sem_init(&wsem, 0, 1);
sem_init(&rsem,0,1);

void writer(void)
{
 while(true)
 {
   prepare_data();
   pthread_mutex_lock(&mutex_writecount);
        writecount++;
        //if == 1
        sem_wait(&rsem); //attend plus de readers
   pthread_mutex_unlock(&mutex_writecount);

   sem_wait(&wsem);
     // section critique, un seul writer à la fois
     write_database();
   sem_post(&wsem);

   pthread_mutex_lock(&mutex_writecount);
        writecount--;
        //if == 0
        sem_post(&rsem); //autorise les readers
   pthread_mutex_unlock(&mutex_writecount);

 }
}



void reader(void)
{
 while(true)
 {
   pthread_mutex_lock(&mutex); //un seul reader à la fois a acces à sem_wait
   
   sem_wait(&rsem); //n'avoir qu'un seul reader qui lit
   pthread_mutex_lock(&mutex_readcount);
     // section critique
     readcount++;
     if (readcount==1)
     { // arrivée du premier reader
       sem_wait(&wsem);// je suis entrain de lire, vous ne pouvez plus écrire
     }
     if(writecount == 1){
         sem_post(&wsem)
     }
   pthread_mutex_unlock(&mutex_readcount);
   sem_post(&rsem);

   pthread_mutex_unlock(&mutex);

   read_database();

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

void main(int argc, char* argv[]){

}