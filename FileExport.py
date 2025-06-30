"""import pandas as pd

dataFood = pd.read_csv('food.csv', delimiter=';')
dataSnack = pd.read_csv('snack.csv', delimiter=';')
dataCharacters = pd.read_csv('characters.csv', delimiter=';')

ChosenGender = 'Male'
ChosenPersonality = 'Docile personalities'

foodDict = {}
snackDict = {}
charactersDict = {}
charactersDictNaN = {}

for index, row in dataFood.iterrows():
    if row['Personality Like'] == ChosenPersonality:
        foodDict[row['Name']] = row['DLC']

for index, row in dataSnack.iterrows():
    if row['Personality Like'] == ChosenPersonality:
        snackDict[row['Name']] = row['DLC']

for index, row in dataCharacters.iterrows():
    if row['Character Personality'] == ChosenPersonality and row['Character Gender'] in (ChosenGender, 'Either'):
        charactersDict[row['Character Name']] = row['DLC']

for index, row in dataCharacters.iterrows():
    if pd.isna(row['Character Personality']) and row['Character Gender'] in (ChosenGender, 'Either'):
        charactersDictNaN[row['Character Name']] = row['DLC']

#print(foodDict)
#print(snackDict)
print(charactersDict)
print(charactersDictNaN)
#print(dataCharacters.to_string())"""