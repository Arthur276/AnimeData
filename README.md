# AnimeData

## Presentation

AnimeData is a python-based project developed by swarthur.

The project's goal is to offer an open-source and easy way to get data about its favourite animes and series.

AnimeData is composed of 2 main files :

1. *animedata.py* : Python module essential to exploit and modify the JSON database.
2. *animedata_source.json* : JSON file containing the anime database.

## Data available

In theory, the database can support any kind of information about an anime or a serie but every type may not be available to every anime.

## How to use this library

In order to make this project useful for everyone, anybody can use the provided tool to get, add or modify its animes or series, **from a compatible manager**.
> Currently, only AnimeTime is compatible with AnimeData.

### How does the tool works ?

The tool's input needs to be an dictionnary, specially formatted, with special keys provided in a dictionnary in the module.

Example of formatted python dictionnary :

```py
json_dict = {"anime_name":{
    "seasons_episodes":{
        "episode_number":{
            "episode_name" : "episode_name",
            "episode_duration" : 00,
            "episode_release_date" : [MM,DD,YYYY]
            }
        ...} # Others episodes
        }
    ...} # Others animes 
```

### Does another JSON file is compatible ?

AnimeData uses metadata, and corruped metadata stops the tool from loading the data.

The AnimeData loading-friendly files are :

* animedata_source.json : source file of the database
* animedata_local.json : custom file, similar to the source file but containing custom data from an anime manager.

The AnimeData saving-friendly files is:

* animedata_local.json : custom file used to save anime's custom data from a compatible anime manager.



Pour suggérer des modifications, cela se passe sur Github : <https://github.com/swarthur/AnimeData/>

Aussi, grâce à Github, l'utilitaire AnimeData permet de mettre à jour la librairie sans avoir a télécharger le projet dans son entièrté à nouveau.

Enfin, l'utlitaire permet d'enregistrer ses données dans un fichier personalisé.

ATTENTION : Des métadonnées et des formatages bien définis de la librairie sont nécéssaire au bon fonctionnement du programme. Ainsi, il est dangereux de modifier la librairie à la main mais l'utlitaire, exploite les données contenues dans le fichier JSON et renvoie des dictionnaires pour permettre a chacun de créer sa manière d'exploiter AnimeData. Pour  le moment, AnimeTime est une possibilité pour gérer ses animés grâce à AnimeData.
