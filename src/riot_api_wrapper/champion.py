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
        vignette = vignette.resize((60,60))
        if victory_boolean : 
            mat = (0.5,  0, 0, 0,
                   0, 1.1, 0, 0,
                   0, 0, 0.5, 0)
        else : 
            mat = (1.1,  0, 0, 0,
                   0, 0.5, 0, 0,
                   0, 0, 0.5, 0)
        processed_vignette = vignette.convert('RGB', mat)
        return processed_vignette
    
    def get_processed_vignette2(self, victory_boolean):
        vignette = self.get_vignette()
        vignette = vignette.resize((60,60))
        if victory_boolean:
            victory_mat = Image.new("RGB", (vignette.width, 8),(54,151,18))
        else : 
            victory_mat = Image.new("RGB", (vignette.width, 8),(162,33,33))
        processed_vignette = Image.new("RGB", (vignette.width, vignette.height + victory_mat.height))
        processed_vignette.paste(vignette, (0,0))
        processed_vignette.paste(victory_mat, (0, vignette.height))
        return processed_vignette
    
    