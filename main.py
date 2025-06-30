import json

from PIL.ImageFile import ImageFile
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd

from DataImageDict import FoodImageDict, SnackImageDict, CharacterImageDict
from domain_objects import Food, Snack, Character, Item

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/results", response_class=HTMLResponse)
async def get_results(request: Request):
    data = await request.json()
    gender = data["gender"].capitalize()
    personality = data["personality"].capitalize() + " personalities"

    dataFood = pd.read_csv('food.csv', delimiter=';')
    dataSnack = pd.read_csv('snack.csv', delimiter=';')
    dataCharacters = pd.read_csv('characters.csv', delimiter=';')

    foodDict:dict[str, Food] = {}
    snackDict:dict[str, Snack] = {}
    charactersDict:dict[str, Character] = {}
    charactersDictNaN:dict[str, Character] = {}

    for _, row in dataFood.iterrows():
        if row['Personality Like'] == personality:
            foodDict[row['Name']] = Food(name = row['Name'], dlc =row['DLC'])

    for _, row in dataSnack.iterrows():
        if row['Personality Like'] == personality:
            snackDict[row['Name']] = Snack(name = row['Name'], dlc =row['DLC'])

    for _, row in dataCharacters.iterrows():
        if row['Character Personality'] == personality and row['Character Gender'] in (gender, 'Either'):
            charactersDict[row['Character Name']] = Character(name = row['Character Name'], dlc =row['DLC'])

    for _, row in dataCharacters.iterrows():
        if pd.isna(row['Character Personality']) and row['Character Gender'] in (gender, 'Either'):
            charactersDictNaN[row['Character Name']] = Character(name = row['Character Name'], dlc =row['DLC'])

    def add_images(items: dict[str, Item], item_images: dict[str, str]):
        for item_name in item_images:
            if item_name in items:
                print(f"Matching: {item_name} -> {item_images[item_name]}")
                items[item_name].image = item_images[item_name]
            else:
                print(f"No match for: {item_name}")

    add_images(foodDict, FoodImageDict)
    add_images(snackDict, SnackImageDict)
    add_images(charactersDict, CharacterImageDict)
    add_images(charactersDictNaN, CharacterImageDict)
    add_images(charactersDictNaN, CharacterImageDict)

    return JSONResponse({
        "foods": [food.model_dump() for food in foodDict.values()],
        "snacks": [snack.model_dump() for snack in snackDict.values()],
        "characters": [character.model_dump() for character in charactersDict.values()],
        "unknown_personality_characters": [character.model_dump() for character in charactersDictNaN.values()]
    })