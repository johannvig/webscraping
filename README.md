# webscraping


Ce projet utilise Python pour effectuer le webscraping d'un site web donné. Le code utilise les bibliothèques selenium, fake_useragent, colorama, csv, pandas et requests pour effectuer les opérations de webscraping.

Installation

Cloner ce dépôt sur votre machine locale.
Assurez-vous d'avoir Python 3 installé sur votre machine.

Installez les bibliothèques requises à l'aide de la commande suivante :

pip install selenium fake_useragent colorama csv pandas requests
Téléchargez et installez Google Chrome sur votre machine locale.
Téléchargez et installez le chromedriver correspondant à la version de Google Chrome installée sur votre machine locale.
Déplacez le fichier chromedriver téléchargé dans le même dossier que le code Python.

Utilisation

Exécutez le fichier main.py en utilisant la commande suivante :

python main.py
Le programme va s'exécuter et effectuer le webscraping en utilisant les informations fournies dans le fichier webscraping.json et le fichier .csv.


Configuration

Le fichier webscraping.json contient les informations de configuration pour le programme de webscraping. Les différentes options sont :

url : L'URL du site web à scraper.
headless : Spécifie si le navigateur doit être en mode "headless" ou non. Les valeurs possibles sont "yes" ou "no".
proxyless : Spécifie si le programme doit utiliser un proxy pour le webscraping. Les valeurs possibles sont "yes" ou "no".
sleep_time : Le temps de pause entre chaque requête, en secondes.
max_retry : Le nombre maximal de tentatives à effectuer si une requête échoue.
timeout : Le temps maximal pour attendre qu'une page se charge, en secondes.

#🚨Avertissement
Le webscraping de sites web sans autorisation peut être illégal. Veuillez vous assurer d'avoir le droit de scraper le site web avant d'utiliser ce programme.
