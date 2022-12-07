Plusieurs commandes sont disponibles dans le Makefile

Les plus gobales sont :

	$make all : permet de run tout le programme, de plots les graphs dans les différents fichers Part1 et Part2 et de zip l'ensemble dans un fichier target.zip. 
	$make clean_all : permet de supprimer tout ce qu'a créé make all
	
Ces commandes sont simplement l'exécution à la suite d'autres commandes, plus simples à savoir :

Pour make all :

	$make all_exe : permet de créer les 3 exécutables philosophes, lececriv et prodcons
	
		Elle même est la suite de 3 exécutions :
		
		$make philosophes : crée l'exécutable philosophes
		$make lececriv : crée l'exécutable lececriv
		$make prodcons : crée l'exécutable prodcons
	
	$make all_exe2 : permet de créer les 3 exécutables philosophes, lececriv et prodcons
	
		Elle même est la suite de 5 exécutions :
		
		$make philosophes2 : crée l'exécutable philosophes
		$make lececriv2 : crée l'exécutable lececriv
		$make prodcons2 : crée l'exécutable prodcons
		$make testAndSet : crée l'exécutable testAndSet
		$make testAndTestAndSet : crée l'exécutable testAndTestAndSet

	$make all_data : permet de créer les 3 fichiers excels utiles aux graphes de la partie 1
	
		Elle même est la suite de 3 exécutions :
		
		$make data_philo : crée le fichier philosophes.csv
		$make data_lececriv : crée le fichier lececriv.csv
		$make data_prodcons : crée le fichier prodcons.csv
		
	$make all_data2 : fais la même chose que $make all_data avec l'implémentation active Test-And-Test-And-Set.

	$make all_data2 : fais la même chose que $make all_data avec l'implémentation active Test-And-Set.
		
	$make python : crée tous les graphes pythons 
	
	$make zip : transforme le projet entier en format zip
	
	$make  clean_all : Clean all appelle toutes les autres cleans. 

		$make clean_exe : supprime tous les exécutables
		$make clean_csv : supprime tous les fichiers .csv
		$make clean_python : supprime tous les plots
		$make clean_zip : supprime le fichier zip


