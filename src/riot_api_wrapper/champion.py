import requests
import urllib
from PIL import Image
from src.utils.utils import convert_to_url_format

class Champion():
    def __init__(self, engine, champion_id):
        self.engine = engine
        self.id = champion_id
        self.name = self._translate_champion_id_to_champion_name()

    def __str__(self):
        return self.name
    
    def _translate_champion_id_to_image_name(self):
        url = "https://ddragon.leagueoflegends.com/cdn/9.3.1/data/en_US/champion.json"
        all_champions_data = requests.get(url).json()['data']
        image_name = 'Aatrox.jpg' #default
        for champion in all_champions_data :
            if all_champions_data[champion]['key'] == self.id : 
                image_name = all_champions_data[champion]['image']['full']
        return image_name 

    def _translate_champion_id_to_champion_name(self):
        url = "https://ddragon.leagueoflegends.com/cdn/9.3.1/data/en_US/champion.json"
        all_champions_data = requests.get(url).json()['data']
        champion_name = 'Aatrox.jpg' #default
        for champion in all_champions_data :
            if all_champions_data[champion]['key'] == self.id : 
                champion_name = champion_name
        return champion_name

    def get_vignette(self):
        vignette_name = self._translate_champion_id_to_image_name()
        vignette_name_formatted = convert_to_url_format(vignette_name).replace('jpg', 'png')
        url = "https://ddragon.leagueoflegends.com/cdn/13.24.1/img/champion/{}".format(vignette_name_formatted)
        vignette = Image.open(urllib.request.urlopen(url))
        return vignette
    
    def get_processed_vignette(self, victory_boolean):
        vignette = self.get_vignette()
        processed_vignette = vignette
        return processed_vignette