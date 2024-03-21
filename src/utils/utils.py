import urllib

def convert_to_url_format(text):
    return urllib.parse.quote_plus(text)