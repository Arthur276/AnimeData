import animedata as ad

if __name__ == "__main__":
    ad.dev_mode = True
    #ad.update_anime_lib()
    json_dict = ad.load_json_dict(True)
    print(json_dict)
    ad.save_json(json_dict)