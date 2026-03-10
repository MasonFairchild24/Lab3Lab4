import requests
import random

BASE_URL = "https://www.dnd5eapi.co/api/2014"

def monster_list():
    apiresponse = requests.get(f"{BASE_URL}/monsters")
    data = apiresponse.json()
    return data["results"]   # FIXED

def monster_details(index):
    apiresponse = requests.get(f"{BASE_URL}/monsters/{index}")
    return apiresponse.json()   # FIXED

def sample_monsters(samplesize=40):
    monsters = monster_list()
    return random.sample(monsters, samplesize)