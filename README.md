# AnimeData

## Presentation

AnimeData is a python-based project developed by swarthur.

The project's goal is to offer an open-source and easy way to get data about its favourite animes and series.

AnimeData is composed of 2 main files :

1. *animedata.py* : Python module essential to exploit and modify the JSON database.
2. *animedata_source.json* : JSON file containing the anime database.

## Data available

In theory, the database can support any kind of information about an anime or a serie, but currently only a few of data types are added :

1. Anime :
    - name (only one)
2. Season :
    - release date
    - number of episodes
3. Episode :
    - name (only one)
    - release date
    - duration
    - number


Afin que cette librairie soit d'utilité générale, et pas seulement pour le projet AnimeTime, qui a poussé ce projet à naitre; un utlitaire est fourni, mettant a disposition les outils pour modifier, exploiter ou agrandir cette librairie de données, à la manière d'encyclopédie libre en ligne telles que Wikipédia.

Pour suggérer des modifications, cela se passe sur Github : <https://github.com/swarthur/AnimeData/>

Aussi, grâce à Github, l'utilitaire AnimeData permet de mettre à jour la librairie sans avoir a télécharger le projet dans son entièrté à nouveau.

Enfin, l'utlitaire permet d'enregistrer ses données dans un fichier personalisé.

ATTENTION : Des métadonnées et des formatages bien définis de la librairie sont nécéssaire au bon fonctionnement du programme. Ainsi, il est dangereux de modifier la librairie à la main mais l'utlitaire, exploite les données contenues dans le fichier JSON et renvoie des dictionnaires pour permettre a chacun de créer sa manière d'exploiter AnimeData. Pour  le moment, AnimeTime est une possibilité pour gérer ses animés grâce à AnimeData.
