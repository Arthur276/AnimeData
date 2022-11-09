import json
import urllib.request
import tomli

with open("../../pyproject.toml", mode="rb") as pypr:
    ad_version = tomli.load(pypr)["project"]["version"]
print("Version du script python d'AnimeData : ", ad_version)
dev_mode = False
animedata = {"dev_branch" : "dev-0.1" ,
            "main_branch" : "main" ,
            "file_path" : "/src/animedata/animedata_source.json",
            "repository_url" : "https://raw.githubusercontent.com/cassphir/animedata/",
            "nom_fichier_source" : "animedata_source.json",
            "nom_fichier_local" : "animedata_local.json",
            "dict_nom_anime" : "nom_anime",
            "dict_saisons_episodes" : "saisons_episodes",
            "dict_duree_episode" : "duree_episode",
            "dict_date_sortie_episode" : "date_sortie_episode",
            "dict_nom_episode" : "nom_episode"}


def maj_anime_lib():
    """Met à jour la librairie AnimeData depuis Github"""
    #STATUS : OK
    if dev_mode:
        urllib.request.urlretrieve(animedata["repository_url"] + animedata["dev_branch"] + animedata["file_path"],animedata["nom_fichier_source"])
    else:
        urllib.request.urlretrieve(animedata["repository_url"] + animedata["main_branch"] + animedata["file_path"],animedata["nom_fichier_source"])
    with open(animedata["nom_fichier_source"],"r",encoding = "utf-8") as animedata_json:
        main_dict = json.load(animedata_json)
        print("Version AnimeData du fichier téléchargé :" + main_dict["ANIMEDATA-METADATA"]["animedata_version"],"#" + main_dict["ANIMEDATA-METADATA"]["lib_subversion"])
        print("Voici les animés disponible en ligne :")
        for element in main_dict.values():
            if element["type"] == "anime":
                print(element[animedata["dict_nom_anime"]])


def sauv_json(anime_dict):
    """Sauvegarde les données des animés contenues dans un dictionnaire dans un fichier JSON personalisé"""
    #STATUS : OK
    with open(animedata["nom_fichier_local"],"w",encoding = "utf-8") as local_json:
        for anime in anime_dict.values():
            if anime["type"] == "anime":
                dict_ok = True
            else:
                dict_ok = False
                break
        if dict_ok :
            json_dict = {"ANIMEDATA-METADATA":{"type" : "metadata","animedata_version" : ad_version}, **anime_dict}
        else:
            print("Dictionnaire transmis non conforme à la sauvegarde")
        json.dump(obj = json_dict, fp = local_json,ensure_ascii = False)


def get_json_dict(ad_source = False):
    """Récupère le dictionnaire contenant les données depuis le fichier local d'AnimeData ou un fichier personalisé"""
    #STATUS : OK
    if ad_source :
        fichier_cible = animedata["nom_fichier_source"]
    else:
        fichier_cible = animedata["nom_fichier_local"]
    with open(fichier_cible,"r",encoding ="utf-8") as animedata_json:
        anime_dict = json.load(animedata_json)
    return anime_dict
