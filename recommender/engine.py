# recommender/engine.py

import json
from .utils import load_outfits

def recommend_outfit(weather, occasion, gender):
    outfits = load_outfits("data/outfits.json")

    for outfit in outfits:
        if (outfit["weather"] == weather and 
            outfit["occasion"] == occasion and 
            outfit["gender"] == gender):
            return f"Recommended outfit: {', '.join(outfit['items'])}"

    return "Sorry, no outfit found for that combination."
