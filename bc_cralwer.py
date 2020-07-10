import requests
import json, math, http, html, os, datetime

def main():
    get_data()
    # open_data()

def get_data():
    url = "http://www.bcliquorstores.com/ajax/browse?category=beer&maincategory=domestic+beer&sort=name.raw:asc&size=24&page=2"
    res = requests.get(url)
    # bc_dict = json.loads(res)

    bc_dict = res.json()

    path = '/home/django-apps/crypto/crypto/json/'
    with open(path+'bcliquor.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(bc_dict, jsonfile, ensure_ascii=False, indent=4, sort_keys=True)
    # print(bc_dict['hits'])

def open_data():
    print(os.path.abspath(__file__))
    # with open("C:\Users\Administrator\Downloads\bcliquor.txt", "r") as jsonfile;
    # json.loads(jsonfile)
    # print(f.read())

def get_date():
    time = datetime.datetime.now()
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    min = time.min
    time.strftime("")

main()


