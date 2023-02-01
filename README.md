# showdata

## Presentation

showdata is a python-based project developed by swarthur.

The project's goal is to offer an open-source and easy way to get data about its favourite animes and series.

showdata is composed of 2 main files :

1. *showdata.py* : Python module essential to exploit and modify the JSON database.
2. *showdata_source.json* : JSON file : series database.

## Data available

Some series data may be missing, especially if the series has been added a long time ago. However, each series should be compatible with the latest version of showdata.

## How to use this library

In order to make this project useful for everyone, anybody can use the provided tool to get, add or modify its animes or series, **from a compatible manager**.
> Currently, only AnimeTime is compatible with showdata.

### How does the tool works ?

The tool's input needs to be an dictionnary, specially formatted, with special keys provided in a dictionnary in the module.

Example of formatted python dictionnary :

```py
json_dict = {"series_name":{
    "seasons_episodes":{
        "episode_number":{
            "episode_name" : "episode_name",
            "episode_duration" : 00,
            "episode_release_date" : [MM,DD,YYYY]
            }
        ...} # Others episodes
        }
    ...} # Others series 
```

### Does another JSON file is compatible ?

showdata uses metadata, and corruped metadata stops the tool from loading the data.

The showdata loading-friendly files are :

* showdata_source.json : source file of the database
* showdata_local.json : custom file, similar to the source file but containing custom data from an series manager.

The showdata saving-friendly files is:

* showdata_local.json : custom file used to save anime's custom data from a compatible anime manager.
