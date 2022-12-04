CC=gcc
CFLAGS=-Wall -Werror -g
LIBS= -lpthread
INCLUDE_HEADERS_DIRECTORY=-Iheaders

# ligne 9 :this will run the following command: gcc -Wall -Werror -g -o kmeans src/distance.o other_object_filespresent_above.o ... -lcunit -lpthread

all: philosophes prodcons lececriv  #compile les 3 fonctions

all_data: data_philo data_lececriv data_prodcons #compile tous les csv

philosophes: Part1/src/philosophes.c  # compile philosophes # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

data_philo: #compile le csv de philo
	cd Part1/Timer
	./philosophes.sh >> philosophes.csv

prodcons: Part1/src/prodcons.c  # compile prodcons # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

data_prodcons: #compile le csv de prodcons
	cd Part1/Timer
	./prodcons.sh >> prodcons.csv

lececriv: Part1/src/lececriv.c  # compile lececriv # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

data_lececriv: #compile le csv de lececriv
	cd Part1/Timer
	./lececriv.sh >> lececriv.csv

%.o: %.c                  # if for example you want to compute example.c this will create an object file called example.o in the same directory as example.c. Don't forget to clean it in your "make clean"
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ -c $<

clean: #supprime tous les exécutables
	rm -f Part1/src/prodcons Part1/src/lececriv Part1/src/philosophes

clean_csv: #supprime tous les csv
	rm -f Part1/Timer/*.csv

.PHONY: clean