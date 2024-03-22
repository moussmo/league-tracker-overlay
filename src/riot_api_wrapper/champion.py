import requests
from src.utils.utils import translate_champion_id_to_name, convert_to_url_format

class Champion():
    def __init__(self, engine, champion_id):
        self.engine = engine
        self.champion_id = champion_id

    def _get_image_portrait(self):
        champion_name = translate_champion_id_to_name(self.champion_id)
        champion_name_formatted = convert_to_url_format(champion_name)
        url = "https://ddragon.leagueoflegends.com/cdn/14.6.1/data/en_US/champion/{}_0.json".format(champion_name_formatted)
        response = requests.get(url, self.engine.get_default_headers())


    def get_processed_image(self, victory_boolean): 
        image = self._get_image_portrait()
        pass
