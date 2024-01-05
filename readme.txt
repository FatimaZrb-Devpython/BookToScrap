 Afin de créer et activer votre environemment virtuel, voici les étapes à suivre : 

1 - Ouvrez votre éditeur de code et clônez le repository BookToScrap : git clone https://github.com/FatimaZrb-Devpython/BookToScrap.git

2 - Mettez vous dans votre dossier à l'aide de la commande cd

3 - Pour créez votre environnement, utilisez dans votre terminal la commande python -m venv <environment name>

4 - Pour activer l'environnement, exécutez source env/bin/activate  (si vous êtes sous Windows, la commande sera  env\Scripts\activate.bat  ).

Si vous utilisez PowerShell, il faut exécuter la commande sans  .bat 

5 - Pour installez les paquets Python répertoriés dans le fichier requirements.txt, utilisez la commande : pip install -r requirements.txt

6 - Maintenant tous les paquets Python installé, vous pouvez lancer le programme en notant dans le terminal : python program_to_scrap.py