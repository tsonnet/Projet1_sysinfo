Plusieurs commandes sont disponibles dans le Makefile

Les plus gobales sont :

	$make all : permet de run tout le programme
	$make clean_all : permet de supprimer tout ce qu'a créé make all
	
Ces commandes sont simplement l'exécution à la suite d'autres commandes, plus simples à savoir :

Pour make all :

	$make all_exe : permet de créer les 3 exécutables philosophes, lececriv et prodcons
	
		Elle même est la suite de 3 exécutions :
		
		$make philosophes : crée l'exécutable philosophes
		$make lececriv : crée l'exécutable lececriv
		$make prodcons : crée l'exécutable prodcons
	
	$make all_data : permet de créer les 3 fichiers excels utiles aux graphes
	
		Elle même est la suite de 3 exécutions :
		
		$make data_philo : crée le fichier philosophes.csv
		$make data_lececriv : crée le fichier lececriv.csv
		$make data_prodcons : crée le fichier prodcons.csv
		
	$make python : crée tous les graphes pythons 
	
	$make zip : transforme le projet entier en format zip
	
Pour clean_all :

	$make clean_exe : supprime tous les exécutables
	$make clean_csv : supprime tous les fichiers .csv
	$make clean_python : supprime tous les plots
	$make clean_zip : supprime le fichier zip


