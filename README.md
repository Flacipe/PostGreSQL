Nous allons débuter par l'installation des services suivants sur notre VM qui est une ubuntu 16.04: apache2, mysql server, phpmyadmin.

Étape 1 Installation : 

Ouvrez un Terminal (ou une Console). Tappez cette commande : sudo apt-get update. Puis tappez cette commande : sudo apt-get upgrade.

Une fois ces deux commandes terminées, nous allons procéder a l'installation des services dont nous avons besoin : sudo apt-get install phpmyadmin, mysql server, apache2
Pour les identifiants, entrez ceux de votre choix (Que nous appellerons ID pour l'identifiant et MDP pour le mot de passe).
Pour finir tappez ces commandes : sudo service mysql restart
								sudo service Apache2 start

Pour vérifier si l'installation a marché, rendez-vous sur cette adresse localhost/phpmyadmin vous devriez avoir une page de connexion qui s'affiche où vos identifiants sont ID/MDP


Étape 2 Création de backups:

(Pour cette étape, l'utilisateur que vous utiliserez devra avoir le droit de SELECT, DROP, CREATE sur votre base)

Avant de lancer le script, il vous faudra aller modifier le fichier dbnames.txt situé dans le dossier backup. Il vous faut écrire le nom de votre ou vos bases de données dont vous voulez une backup. (Sensible à la casse)
/!\ Si dbnames.txt est vide, un dossier de backup sera créé, mais il sera vide.

Pour faire une backup de vos base de données, il vous faudra lancer le fichier backupMySql.py à l'aide de la commande :

sudo python backupMySql.py

Le programme vous demandera d'entrer l'adresse de l'hôte de votre base de données, l'ID de votre utilisateur et son MDP le tout entre simple quote à chaque fois.

La backup sera ensuite créée dans le dossier /backup/dbbackup/ sous le nom de la date du jour au format "MMDDYYYY-HHMMSS"

Étape 3 Restauration : 

Pour effectuer la restauration, il vous faudra lancer le script restoreDatabase.py à l'aide de la commande :

sudo python restoreDatabase.py

Il vous faudra entrer le nom du dossier contenant vos bases de données, toujours entre simple quotes.
