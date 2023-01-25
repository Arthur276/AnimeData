# watchdata

## Presentation

watchdata is a python-based project developed by swarthur.

The project's goal is to offer an open-source and easy way to get data about its favourite animes and series.

watchdata is composed of 2 main files :

1. *watchdata.py* : Python module essential to exploit and modify the JSON database.
2. *watchdata_source.json* : JSON file : series database.

## Data available

Some series data may be missing, especially if the series has been added a long time ago. However, each series should be compatible with the latest version of watchdata.

## How to use this library

In order to make this project useful for everyone, anybody can use the provided tool to get, add or modify its animes or series, **from a compatible manager**.
> Currently, only AnimeTime is compatible with watchdata.

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

watchdata uses metadata, and corruped metadata stops the tool from loading the data.

The watchdata loading-friendly files are :

* watchdata_source.json : source file of the database
* watchdata_local.json : custom file, similar to the source file but containing custom data from an series manager.

The watchdata saving-friendly files is:

* watchdata_local.json : custom file used to save anime's custom data from a compatible anime manager.
