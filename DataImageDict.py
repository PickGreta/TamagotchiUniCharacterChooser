from PIL import Image

FoodImageDict = {
    "Chicken & Waffles": "/static/images/VeryBerryLand/ChickenWafflesUni.png",
    "Berry Salad": "/static/images/VeryBerryLand/MixFruitSalad.png",
    "Berry Porridge": "/static/images/VeryBerryLand/BerryPorridgeUni.png",
    "Ice Cream Sandwich": "/static/images/VeryBerryLand/IceCreamSandwichUni.png",

    "Festival Nachos": "/static/images/LoveMeloConcert/FestivalNachosUni.png",
    "Macaroni & Cheese": "/static/images/LoveMeloConcert/MacaroniCheeseUni.png",
    "Trumpet Hot Dog": "/static/images/LoveMeloConcert/TrumpetHotDogUni.png",
    "Rhythm Noodles": "/static/images/LoveMeloConcert/RhythmNoodlesUni.png",

    "Tamamori Noodles": "/static/images/TamamoriFashionShow/TamamoriNoodlesUni.png",
    "Spacy Curry": "/static/images/TamamoriFashionShow/SpacyCurryUni.png",
    "Dress Salad": "/static/images/TamamoriFashionShow/DressSaladUni.png",
    "Palette Sushi": "/static/images/TamamoriFashionShow/PaletteSushiUni.png",

    "Hangyodon Bun": "/static/images/SanrioCharacters/HangyodonBunUni.png",
    "Wisdom Tree Salad": "/static/images/SanrioCharacters/WisdomTreeUni.png",
    "Pochacco Rice Ball": "/static/images/SanrioCharacters/PochaccoRiceBallUni.png",
    "Strawberry Burger": "/static/images/SanrioCharacters/StrawberryBurgerUni.png",

    "Angel Pie": "/static/images/AngelFestival/AngelPieUni.png",
    "Bell Brioche": "/static/images/AngelFestival/BellBriocheUni.png",
    "Heart Omelette": "/static/images/AngelFestival/HeartOmeletteUni.png",
    "Ribbon Bread": "/static/images/AngelFestival/RibbonBreadUni.png",

    "Squid Ink Pie": "/static/images/MonsterCarnival/SquidInkPieUni.png",
    "Monster Sandwich": "/static/images/MonsterCarnival/MonsterSandwichUni.png",
    "Ogre Rice Ball": "/static/images/MonsterCarnival/OgreRiceBallUni.png",
    "Goblin Bun": "/static/images/MonsterCarnival/GoblinBunUni.png",

    "Kaguya Sushi": "/static/images/FairyTaleLibrary/KaguyaSushi_Uni_sprite.png",
    "Excaliburger": "/static/images/FairyTaleLibrary/Excaliburger_Uni_sprite.png",
    "Goose Dip": "/static/images/FairyTaleLibrary/GooseDip_Uni_sprite.png",
    "Rapunzel Pasta": "/static/images/FairyTaleLibrary/RapunzelPasta_Uni_sprite.png",

    "Fried Chicken": "/static/images/PokoPeaLand/FriedChicken_Uni_sprite.png",
    "Gyoza": "/static/images/PokoPeaLand/Gyoza_Uni_sprite.png",
    "Mapo Curry": "/static/images/PokoPeaLand/MapoCurry_Uni_sprite.png",
    "Endless Takoyaki": "/static/images/PokoPeaLand/EndlessTakoyaki_Uni_sprite.png",
    "Tofu": "/static/images/PokoPeaLand/Tofu_Uni_sprite.png",

    "Soccer Rice Ball": "/static/images/DoriTamaSchool/SoccerRiceBallUni.png",
    "DoriTama Lunch": "/static/images/DoriTamaSchool/DoriTamaLunchUni.png",
    "Yakisoba Bread": "/static/images/DoriTamaSchool/YakisobaBreadUni.png",
    "Yumecantchi Bento": "/static/images/DoriTamaSchool/YumecantchiBentoUni.png",

}

SnackImageDict = {
    "Apple Cake": "/static/images/VeryBerryLand/Onapplecake.png",
    "Strawberry Rice Cake": "/static/images/VeryBerryLand/StrawberryRiceCakeUni.png",
    "Patissier Cake": "/static/images/VeryBerryLand/PatissierCakeUni.png",
    "Fruit Candy": "/static/images/VeryBerryLand/FruitCandyUni.png",

    "Drum Popcorn": "/static/images/LoveMeloConcert/DrumPopcornUni.png",
    "Sachertorte": "/static/images/LoveMeloConcert/SachertorteUni.png",
    "Lovely Frappe": "/static/images/LoveMeloConcert/LovelyFrappeUni.png",
    "Music Donut": "/static/images/LoveMeloConcert/MusicDonutUni.png",

    "Boots-Glass Tea": "/static/images/TamamoriFashionShow/BootsGlassTeaUni.png",
    "Puff Macaron": "/static/images/TamamoriFashionShow/PuffMacaronUni.png",
    "Top Hat Éclair": "/static/images/TamamoriFashionShow/TopHatEclairUni.png",
    "Sunglasses Chocolate": "/static/images/TamamoriFashionShow/SunglassesChocolateUni.png",

    "Flower Sherbet": "/static/images/SanrioCharacters/FlowerSherbertUni.png",
    "Melody Strawberry": "/static/images/SanrioCharacters/MelodyStrawberryUni.png",
    "Cotton Cogimyun": "/static/images/SanrioCharacters/CottonCogimyunUni.png",
    "Star Pancake": "/static/images/SanrioCharacters/StarPancakeUni.png",

    "White Chocolate": "/static/images/AngelFestival/WhiteChocolateUni.png",
    "Unicorn Parfait": "/static/images/AngelFestival/UnicornParfaitUni.png",
    "Rain Candy": "/static/images/AngelFestival/RainCandyUni.png",
    "Pegasus Cotton Candy": "/static/images/AngelFestival/PegasusCottonCandyUni.png",

    "Black Chocolate": "/static/images/MonsterCarnival/BlackChocolateUni.png",
    "Slimy Jelly": "/static/images/MonsterCarnival/SlimyJellyUni.png",
    "Eye Ball Jelly": "/static/images/MonsterCarnival/EyeballJellyUni.png",
    "Snake Churros": "/static/images/MonsterCarnival/SnakeChurrosUni.png",

    "Caramelized Apple": "/static/images/FairyTaleLibrary/CaramelizedApple_Uni_sprite.png",
    "Whale Jelly": "/static/images/FairyTaleLibrary/WhaleJelly_Uni_sprite.png",
    "Momotaro Compote": "/static/images/FairyTaleLibrary/MomotaroCompote_Uni_sprite.png",
    "Pumpkin Pudding": "/static/images/FairyTaleLibrary/PumpkinPudding_Uni_sprite.png",

    "Peanuts-kun Jellies": "/static/images/PokoPeaLand/PeanutskunJellies_Uni_sprite.png",
    "Tanuki Cake": "/static/images/PokoPeaLand/TanukiCake_Uni_sprite.png",
    "Poko Latte": "/static/images/PokoPeaLand/PokoLatte_Uni_sprite.png",
    "Ramune": "/static/images/PokoPeaLand/Ramune_Uni_sprite.png",
    "Beetle Parfait": "/static/images/PokoPeaLand/BeetleParfait_Uni_sprite.png",
    "Soda Tasters": "/static/images/PokoPeaLand/SodaTasters_Uni_sprite.png",

    "School Bus Cookie": "/static/images/DoriTamaSchool/SchoolBusCookieUni.png",
    "Tape Cake": "/static/images/DoriTamaSchool/TapeCakeUni.png",
    "Basketball Cookie": "/static/images/DoriTamaSchool/BasketballCookieUni.png",
    "DoriTama Cake": "/static/images/DoriTamaSchool/DoriTamaCakeUni.png",

}

CharacterImageDict = {
    "Hotcaketchi": "/static/images/VeryBerryLand/HotcaketchiUniSprite.png",
    "Ichigotchi": "/static/images/VeryBerryLand/Ichigotchi_Uni_sprite.png",
    "Ringotchi": "/static/images/VeryBerryLand/Ringotchi_Uni_sprite.png",
    "Patitchi": "/static/images/VeryBerryLand/Patitchi_Uni_sprite.png",
    "Cornetchi": "/static/images/VeryBerryLand/Cornetchi_Uni_sprite.png",
    "Tanghulutchi": "/static/images/VeryBerryLand/Tanghulutchi_Temp_Uni_sprite_v2.png",

    "Chekeratchi": "/static/images/LoveMeloConcert/ChekeratchiUniSprite.png",
    "Drumcrubitchi": "/static/images/LoveMeloConcert/Drumcrubitchi_Uni_sprite.png",
    "Lovelitchi": "/static/images/LoveMeloConcert/Lovelitchi_Uni_sprite.png",
    "Melodytchi": "/static/images/LoveMeloConcert/Melodytchi_Uni_sprite.png",
    "Pianitchi": "/static/images/LoveMeloConcert/Pianitchi_Uni_sprite.png",
    "Rhythristchi": "/static/images/LoveMeloConcert/RhythristchiSprite.png",

    "Spacytchi": "/static/images/TamamoriFashionShow/Spacytchi_Uni_sprite.png",
    "Mystartchi": "/static/images/TamamoriFashionShow/Mystartchi_Uni_sprite.png",
    "Boots Brothers": "/static/images/TamamoriFashionShow/BootsbrothersSprite.png",
    "Moriritchi": "/static/images/TamamoriFashionShow/Moriritchi_Uni_sprite.png",
    "Coffretchi": "/static/images/TamamoriFashionShow/Coffretchi_Uni_sprite.png",
    "Dresstchi": "/static/images/TamamoriFashionShow/DresstchiSprite.png",

    "Mame Kitty": "/static/images/SanrioCharacters/Mame_Kitty_Uni_sprite.png",
    "Patchi Purin": "/static/images/SanrioCharacters/PatchipurinUniSprite.png",
    "Usahana Memetchi": "/static/images/SanrioCharacters/Usahana_Memetchi_Sprite_-_Sanrio_Uni.png",
    "Cinnamon Moriritchi": "/static/images/SanrioCharacters/Cinnamon_Moriritchi_Uni_sprite.png",
    "Kuromi Melodytchi": "/static/images/SanrioCharacters/Kuromi_Melodytchi_Uni_sprite.png",
    "Hangyodon Sebiretchi": "/static/images/SanrioCharacters/Hangyodon_Sebiretchi_Uni_sprite.png",
    "MyMelo Lovelitchi": "/static/images/SanrioCharacters/My_Melo_Lovelitchi_-_Sanrio_Uni.png",
    "Pochacco Mimitchi": "/static/images/SanrioCharacters/Pochacco_Mimitchi_Sprite_-_Sanrio_Uni.png",
    "Cogimyun Woopatchi": "/static/images/SanrioCharacters/Cogimyun_Woopatchi_Sprite_-_Sanrio.png",
    "Little Unimarutchi": "/static/images/SanrioCharacters/Little_Unimarutchi_Sprite_-_Sanrio_Uni.png",

    "Mame-El": "/static/images/AngelFestival/MametchielSprite.png",
    "Pegasustchi": "/static/images/AngelFestival/PegasupatchiSprite.png",
    "Flowerdite": "/static/images/AngelFestival/FlowerditeSprite.png",
    "Sebirecupid": "/static/images/AngelFestival/SebirecupitSprite.png",
    "Yumemittie": "/static/images/AngelFestival/YumemiteSprite.png",
    "Unimarucorn": "/static/images/AngelFestival/UnimarcornSprite.png",

    "Mamegon": "/static/images/MonsterCarnival/Mamegon_Uni_sprite.png",
    "Slimypatchi": "/static/images/MonsterCarnival/Slimy_Patch_Uni_sprite.png",
    "Meduupa": "/static/images/MonsterCarnival/Meduupa_Uni_sprite.png",
    "Gobpyon": "/static/images/MonsterCarnival/Gobupyon_Uni_sprite.png",
    "Giveuptchi": "/static/images/MonsterCarnival/GiveuptchiSprite.png",
    "Onimarutchi": "/static/images/MonsterCarnival/OnimarutchiSpriteUni.png",

    "Mamecchio": "/static/images/FairyTaleLibrary/Mamecchio_Uni_sprite.png",
    "Piggypatchis": "/static/images/FairyTaleLibrary/Piggypatchis_Uni_sprite.png",
    "Kikigoku": "/static/images/FairyTaleLibrary/Kikigoku_Uni_sprite.png",
    "Pyonderella": "/static/images/FairyTaleLibrary/Pyonderella_Uni_sprite.png",
    "Milkyukihime": "/static/images/FairyTaleLibrary/Milkyukihime_Uni_sprite.png",
    "Neliakaguya": "/static/images/FairyTaleLibrary/Neliakaguya_Uni_sprite.png",

    "Peanutskun": "/static/images/PokoPeaLand/Peanutskun_Uni_sprite.png",
    "Chancho": "/static/images/PokoPeaLand/Chancho_Uni_sprite.png",
    "Peanutsoyaji": "/static/images/PokoPeaLand/PeanutsOyajitchi_Uni_sprite.png",
    "Banana-hairtchi": "/static/images/PokoPeaLand/Bananahairtchi_Uni_sprite.png",
    "Tanuki Ninja": "/static/images/PokoPeaLand/TanukiNinja_Uni_sprite.png",
    "Ponpoko": "/static/images/PokoPeaLand/Ponpoko_Uni_sprite.png",
    "Gachikoi-P": "/static/images/PokoPeaLand/GachikoiPonpoko_Uni_sprite.png",

    "Kuromametchi": "/static/images/DoriTamaSchool/Kuromametchi_Uni_sprite.png",
    "Octpasketchi": "/static/images/DoriTamaSchool/Octpasketchi_Uni_sprite_V2.png",
    "Tapepentchi": "/static/images/DoriTamaSchool/Tapepentchi_Uni_sprite.png",
    "Yumemitchi": "/static/images/DoriTamaSchool/Yumemitchi_Uni_sprite.png",
    "Kiraritchi": "/static/images/DoriTamaSchool/Kiraritchi_Uni_sprite.png",
    "Miraitchi": "/static/images/DoriTamaSchool/Miraitchi_Uni_sprite_V2.png",
    "Clulutchi": "/static/images/DoriTamaSchool/Clulutchi_Uni_sprite_V2.png",
}

print(CharacterImageDict["Kuromametchi"])