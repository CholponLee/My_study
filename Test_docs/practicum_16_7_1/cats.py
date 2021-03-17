import json
from cat import Cat
from urllib.request import urlopen


with urlopen('http://130.193.37.179/api/pet/?page=1&page_size=6&species__name=%D0%BA%D0%BE%D1%88%D0%BA%D0%B0') \
        as response:
    data = json.load(response)

for item in data['results']:
    cat = Cat(item['name'], item['breed']['name'], item['gender']['name'], item['age'])
    cat.get_all()
