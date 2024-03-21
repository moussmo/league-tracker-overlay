import json
import urllib.request

class Account():
    def __init__(self, game_name, tag_line):
        self.game_name = game_name
        self.tag_line = tag_line
        self.puuid = self.get_puuid()

    def get_puuid(self):
        url = "/riot/account/v1/accounts/by-riot-id/{}/{}".format(self.game_name, self.tag_line)
        method = "GET"
        req = urllib.request.Request(url, method=method)
        with urllib.request.urlopen(req) as response :
            body = json.load(response.read())

        

        