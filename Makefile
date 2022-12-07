CC=gcc
CFLAGS=-Wall -Werror -g
LIBS= -lpthread
INCLUDE_HEADERS_DIRECTORY=-Iheaders

# ligne 9 :this will run the following command: gcc -Wall -Werror -g -o kmeans src/distance.o other_object_filespresent_above.o ... -lcunit -lpthread

all : all_exe all_exe2 all_exe3 all_data all_data3 all_python zip #run tout le projet

all_exe : philosophes prodcons lececriv  #compile les 3 fonctions POSIX

all_exe2 : philosophes2 prodcons2  lececriv2 testAndSet testAndTestAndSet #compile les 3 fonctions (test-and-set) + les fichiers tes-and-set et test-and-test-and-set

all_exe3 : philosophes3 prodcons3 lececriv3 #compile les 3 fonctions (test-and-test-and-set)

all_data: data_philo data_lececriv data_prodcons #compile tous les csv

all_data2: data_philo2 data_lececriv2 data_prodcons2 #compile tous les csv #déconseillé de run, prend bcp de temps

all_data3 : data_philo3 data_lececriv3 data_prodcons3 #compile tous les csv

all_python : python python2 python_inginious python2_inginious python_rapport #run tous les plots

clean_all : clean_exe clean_csv clean_python clean_zip #clean tout le projet

philosophes: Part1/src/philosophes.c  # compile philosophes 
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

philosophes2: Part2/src/philosophesOurSem.c Part2/src/Semimplem.c #compile philosophes2 (test-and-set)
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/


philosophes3: Part2/src/philosophesOurSem.c Part2/src/SemimplemTestAndSet.c #compile philosophes3 (test-and-test-and-set)
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

data_philo: #compile le csv de philo
	cd Part1/Timer;\
	./philosophes.sh >philosophes.csv;\
	mv philosophes.csv Data1_csv/
	cd ../..;

data_philo2: #compile le csv de philo2
	cd Part2/Timer;\
	./philosophesOurSem.sh > philosophes2.csv;\
	mv philosophes2.csv Data2_csv/
	cd ../..;

data_philo3: #compile le csv de philo2
	cd Part2/Timer;\
	./philosophesOurSemTestAndSet.sh > philosophes3.csv;\
	mv philosophes3.csv Data3_csv/
	cd ../..;

prodcons: Part1/src/prodcons.c  # compile prodcons
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

prodcons2: Part2/src/prodconsOurSem.c Part2/src/Semimplem.c #compile prodcons2 (test-and-set)
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

prodcons3: Part2/src/prodconsOurSem.c Part2/src/SemimplemTestAndSet.c #compile prodcons3 (test-and-test-and-set)
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

data_prodcons: #compile le csv de prodcons
	cd Part1/Timer;\
	./prodcons.sh > prodcons.csv;\
	mv prodcons.csv Data1_csv/
	cd ../..;

data_prodcons2: #compile le csv de prodcons2
	cd Part2/Timer;\
	./prodconsOurSem.sh > prodcons2.csv;\
	mv prodcons2.csv Data2_csv/
	cd ../..;

data_prodcons3: #compile le csv de prodcons2
	cd Part2/Timer;\
	./prodconsOurSemTestAndSet.sh > prodcons3.csv;\
	mv prodcons3.csv Data3_csv/
	cd ../..;

lececriv: Part1/src/lececriv.c  # compile lececriv 
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part1/src/

lececriv2: Part2/src/lececrivOurSem.c  Part2/src/Semimplem.c # compile lececriv2 (test-and-set)
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

lececriv3: Part2/src/lececrivOurSem.c  Part2/src/SemimplemTestAndSet.c #comile lececriv3 (test-and-test-and-set)
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/src/

data_lececriv: #compile le csv de lececriv
	cd Part1/Timer;\
	./lececriv.sh > lececriv.csv;\
	mv lececriv.csv Data1_csv/
	cd ../..;

data_lececriv2: #compile le csv de lececriv2
	cd Part2/Timer;\
	./lececrivOurSem.sh > lececriv2.csv;\
	mv lececriv2 Data2_csv/;\
	cd ../..;
	

data_lececriv3: #compile le csv de lececriv2
	cd Part2/Timer;\
	./lececrivOurSemTestAndSet.sh > lececriv3.csv;\
	mv lececriv3.csv Data3_csv/
	cd ../..;

testAndSet: Part2/TestAndSet/TestAndSet.c  #Compile test-and-set
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/TestAndSet/

testAndTestAndSet: Part2/TestAndTestAndSet/TestAndTestAndSet.c  # Compile test-and-test-and-set
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ $^ $(LIBS) 
	mv $@ Part2/TestAndTestAndSet/


%.o: %.c                  # if for example you want to compute example.c this will create an object file called example.o in the same directory as example.c. Don't forget to clean it in your "make clean"
	$(CC) $(INCLUDE_HEADERS_DIRECTORY) $(CFLAGS) -o $@ -c $<


python: #compile les graphes de la partie1 pour les 3 programmes
	python3 Part1/Timer/script_python.py subplot Part1/Timer/Data1_csv/philosophes.csv Part1/Timer/Data1_csv/lececriv.csv Part1/Timer/Data1_csv/prodcons.csv ordi_part1
	mv *.png Part1/Plots/

python_inginious: #compile les trois programmes avec le super ordi
	python3 Part1/Timer/script_python.py subplot Part1/Timer/ResultPArt1/philosophes.csv Part1/Timer/ResultPArt1/lececriv.csv Part1/Timer/ResultPArt1/prodcons.csv inginious_part1
	mv *.png Part1/Plots/

python2: #compile les graphes de la partie2 pour les 2 programmes
	python3 Part1/Timer/script_python.py subplot Part2/Timer/Data2_csv/philosophes2.csv Part2/Timer/Data2_csv/lececriv2.csv Part2/Timer/Data2_csv/prodcons2.csv ordi_test_and_test_and_set
	python3 Part1/Timer/script_python.py subplot Part2/Timer/Data3_csv/philosophes3.csv Part2/Timer/Data3_csv/lececriv3.csv Part2/Timer/Data3_csv/prodcons3.csv ordi_test_and_set
	mv *.png Part2/Plots/

python2_inginious: #compile les trois programmes de la part2 avec le super ordi
	python3 Part1/Timer/script_python.py subplot Part2/Timer/Data_inginious/ProdconsTestAndSet.csv Part2/Timer/Data_inginious/PhiloTestAndSet.csv Part2/Timer/Data_inginious/LececrivTestAndSet.csv inginious_test_and_set
	mv *.png Part2/Plots/

python_rapport: #comile les graphes utiles au rapport
	python3 Part1/Timer/script_python.py plot2 Part2/TestAndSet/test_and_set.csv Part2/TestAndTestAndSet/test_and_test_and_set.csv Comparaison
	python3 Part1/Timer/script_python.py plot3 Part2/Timer/Data_inginious/ProdconsTestAndSet.csv Part2/Timer/Data_inginious/ProdconsTestAndTestAndSet.csv Part1/Timer/ResultPArt1/prodcons.csv ProducteurConsommateur
	python3 Part1/Timer/script_python.py plot3 Part2/Timer/Data_inginious/PhiloTestAndSet.csv Part2/Timer/Data_inginious/PhiloTestAndTestAndSet.csv  Part1/Timer/ResultPArt1/philosophes.csv Philosophes
	python3 Part1/Timer/script_python.py plot3 Part2/Timer/Data_inginious/LececrivTestAndSet.csv Part2/Timer/Data_inginious/LececrivTestAndTestAndSet.csv Part1/Timer/ResultPArt1/lececriv.csv LecteurEcrivain
	mv *.png Part2/Plots/

zip: #transforme le projet en format zip
	zip -r target2.zip Part1 Part2 Makefile README.md Experiments experiments.sh

clean_exe: #supprime tous les exécutables
	rm -f Part1/src/prodcons Part1/src/lececriv Part1/src/philosophes
	rm -f Part2/src/prodcons2 Part2/src/lececriv2 Part2/src/philosophes2
	rm -f Part2/src/prodcons3 Part2/src/lececriv3 Part2/src/philosophes3
	rm -f Part2/TestAndSet/testAndSet Part2/TestAndTestAndSet/testAndTestAndSet

clean_csv: #supprime tous les csv
	rm -f Part1/Timer/Data1_csv/*.csv
	rm -f Part2/Timer/Data3_csv/*.csv

clean_python: #supprime tous les plots
	rm -f Part1/Plots/*.png
	rm -f Part1/Timer/*.png
	rm -f Part2/Plots/*.png
	rm -f Part2/Timer/*.png

clean_zip:
	rm -f target.zip

.PHONY: clean