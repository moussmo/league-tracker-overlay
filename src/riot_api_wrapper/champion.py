import requests
import urllib
from PIL import Image
from src.utils.utils import convert_to_url_format

class Champion():
    def __init__(self, engine, champion_id, champion_name):
        self.engine = engine
        self.id = champion_id
        self.name = champion_name

    def __str__(self):
        return self.name

    def get_vignette(self):
        vignette_name = self.name
        if vignette_name == "Smolder":
            vignette_name = 'Aatrox'
        vignette_name_formatted = convert_to_url_format(vignette_name)
        url = "https://ddragon.leagueoflegends.com/cdn/13.24.1/img/champion/{}.png".format(vignette_name_formatted)
        vignette = Image.open(urllib.request.urlopen(url))
        return vignette
    
    def get_processed_vignette(self, victory_boolean):
        vignette = self.get_vignette()
        processed_vignette = vignette
        return processed_vignette