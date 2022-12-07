CC=gcc
CFLAGS=-Wall -Werror -g
LIBS= -lpthread
INCLUDE_HEADERS_DIRECTORY=-Iheaders

# ligne 9 :this will run the following command: gcc -Wall -Werror -g -o kmeans src/distance.o other_object_filespresent_above.o ... -lcunit -lpthread

all : all_exe2 #all_data python python_inginious zip

all_exe : philosophes prodcons lececriv  #compile les 3 fonctions

all_exe2 : philosophes2 philosophes3 prodcons2 prodcons3 lececriv2 lececriv3 testAndSet testAndTestAndSet 

all_data: data_philo data_lececriv data_prodcons #compile tous les csv

all_data2: data_philo2 data_lececriv2 data_prodcons2 #compile tous les csv

clean_all : clean_exe clean_csv clean_python clean_zip

philosophes: Part1/src/philosophes.c  # compile philosophes # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

philosophes2: Part2/src/philosophesOurSem.c Part2/src/Semimplem.c
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/


philosophes3: Part2/src/philosophesOurSem.c Part2/src/SemimplemTestAndSet.c
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

data_philo: #compile le csv de philo
	cd Part1/Timer;\
	./philosophes.sh >philosophes.csv;\
	cd ../..;

data_philo2: #compile le csv de philo
	cd Part2/Timer;\
	./philosophesOurSem.sh > philosophes2.csv;\
	cd ../..;
prodcons: Part1/src/prodcons.c  # compile prodcons # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

prodcons2: Part2/src/prodconsOurSem.c Part2/src/Semimplem.c
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

prodcons3: Part2/src/prodconsOurSem.c Part2/src/SemimplemTestAndSet.c
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

data_prodcons: #compile le csv de prodcons
	cd Part1/Timer;\
	./prodcons.sh > prodcons.csv;\
	cd ../..;

data_prodcons2: #compile le csv de prodcons
	cd Part2/Timer;\
	./prodconsOurSem.sh > prodcons2.csv;\
	cd ../..;

lececriv: Part1/src/lececriv.c  # compile lececriv # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

lececriv2: Part2/src/lececrivOurSem.c  Part2/src/Semimplem.c # compile lececriv # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

lececriv3: Part2/src/lececrivOurSem.c  Part2/src/SemimplemTestAndSet.c
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/
data_lececriv: #compile le csv de lececriv
	cd Part1/Timer;\
	./lececriv.sh > lececriv.csv;\
	cd ../..;

data_lececriv2: #compile le csv de lececriv
	cd Part2/Timer;\
	./lececrivOurSem.sh > lececriv2.csv;\
	cd ../..;

testAndSet: Part2/TestAndSet/TestAndSet.c  # compile philosophes # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/TestAndSet/

testAndTestAndSet: Part2/TestAndTestAndSet/TestAndTestAndSet.c  # compile philosophes # add your other object files needed to compile your program here. !! The ordering is important !! if file_a.o depends on file_b.o, file_a.o must be placed BEFORE file_b.o in the list !
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/TestAndTestAndSet/


%.o: %.c                  # if for example you want to compute example.c this will create an object file called example.o in the same directory as example.c. Don't forget to clean it in your "make clean"
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ -c $<


python: 
	python3 Part1/Timer/script_python.py continue plot Part1/Timer/philosophes.csv Part1/Timer/lececriv.csv Part1/Timer/prodcons.csv ordi
	python3 Part1/Timer/script_python.py boxplot plot Part1/Timer/philosophes.csv Part1/Timer/lececriv.csv Part1/Timer/prodcons.csv ordi
	python3 Part1/Timer/script_python.py continue subplot Part1/Timer/philosophes.csv Part1/Timer/lececriv.csv Part1/Timer/prodcons.csv ordi
	python3 Part1/Timer/script_python.py boxplot subplot Part1/Timer/philosophes.csv Part1/Timer/lececriv.csv Part1/Timer/prodcons.csv ordi
	mv *.png Part1/Plots/

python_inginious:
	python3 Part1/Timer/script_python.py continue plot Part1/Timer/ResultPArt1/philosophes.csv Part1/Timer/ResultPArt1/lececriv.csv Part1/Timer/ResultPArt1/prodcons.csv inginious
	python3 Part1/Timer/script_python.py boxplot plot Part1/Timer/ResultPArt1/philosophes.csv Part1/Timer/ResultPArt1/lececriv.csv Part1/Timer/ResultPArt1/prodcons.csv inginious
	python3 Part1/Timer/script_python.py continue subplot Part1/Timer/ResultPArt1/philosophes.csv Part1/Timer/ResultPArt1/lececriv.csv Part1/Timer/ResultPArt1/prodcons.csv inginious
	python3 Part1/Timer/script_python.py boxplot subplot Part1/Timer/ResultPArt1/philosophes.csv Part1/Timer/ResultPArt1/lececriv.csv Part1/Timer/ResultPArt1/prodcons.csv inginious
	mv *.png Part1/Plots/

python2:
	python3 Part1/Timer/script_python.py continue plot Part2/Timer/philosophes2.csv Part2/Timer/lececriv2.csv Part2/Timer/prodcons2.csv ordi
	python3 Part1/Timer/script_python.py boxplot plot Part2/Timer/philosophes2.csv Part2/Timer/lececriv2.csv Part2/Timer/prodcons2.csv ordi
	python3 Part1/Timer/script_python.py continue subplot Part2/Timer/philosophes2.csv Part2/Timer/lececriv2.csv Part2/Timer/prodcons2.csv ordi
	python3 Part1/Timer/script_python.py boxplot subplot Part2/Timer/philosophes2.csv Part2/Timer/lececriv2.csv Part2/Timer/prodcons2.csv ordi
	mv *.png Part2/Plots/

zip:
	zip -r target2.zip Part1 Part2 Makefile README.md Experiments experiments.sh

clean_exe: #supprime tous les exécutables
	rm -f Part1/src/prodcons Part1/src/lececriv Part1/src/philosophes
	rm -f Part2/src/prodcons2 Part2/src/lececriv2 Part2/src/philosophes2
	rm -f Part2/src/prodcons3 Part2/src/lececriv3 Part2/src/philosophes3
	rm -f Part2/TestAndSet/testAndSet Part2/TestAndTestAndSet/testAndTestAndSet
clean_csv: #supprime tous les csv
	rm -f Part1/Timer/*.csv
	rm -f Part2/Timer/*.csv
clean_python:
	rm -f Part1/Plots/*.png
	rm -f Part1/Timer/*.png

clean_python2:
	rm -f Part2/Plots/*.png
	rm -f Part2/Timer/*.png

clean_zip:
	rm -f target.zip

.PHONY: clean