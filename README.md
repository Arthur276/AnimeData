# animedata

## Introduction

Using a provided database about animes, animedata aims to provide an efficient and easy way **to get and store animes' data**.

The project written in python loads from a JSON file the data and returns it as a dictionnary. Specially formatted for animes' data storage, **the dictionnary needs to be used with a compatible program**.

## Installation and get started

### Install animedata

* Using Pypi :

    ```bash
    pip install animedata
    ```

* Or download the source code from Github and extract it in your workspace.

### Get started

NOTE: The path of the modules is indicated in parentheses

* Update the database from Github : *(animedata.common.lib_interactions)*

    ```python
    get_ad_lib(branch)
    ```

* Load database content into a dictionnary : *(animedata.common.lib_interactions)*

    ```py
    get_ad_lib_content(ad_source)
    ```

* Save a database content into a JSON file : *(animedata.common.saving_process)*

    ```py
    save_json(anime_dict)
    ```

* Check if a dictionnary is correctly formatted : *(animedata.common.dict_checking)*

    ```py
    check_dict(anime_dict)
    ```

### Formatted dictionnary

In order to be compatible with animedata's functions, a dictionnary should be formatted as following :

```py
anime_dict = {"ANIMEDATA-METADATA": {#metadata...
                },
              "anime_1" : {
                "anime_name" : "anime_1",
                #other attributes...
                },
            {#other animes...
            }
        }
```

NOTE :

* Compatible keys are stored in ad_table in *animedata.common.metadata*

* An anime's key msut to be the same as anime_name value.

## About

[Github](https://github.com/swarthur/animedata)
