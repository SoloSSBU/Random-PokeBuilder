from random import shuffle
from urllib.request import urlopen
import ssl
import webbrowser
from getmons import getMon
import pyperclip as pc

x = ["Snorlax", "KangasKhan", "Maushold", "Arcanine", "Charizard", "Ceruledge", "Hitmontop", "Annihilape", "Lucario", "Blastoise", "Feraligatr", "Politoed", "Gyarados",
 "Dragonite", "Corviknight", "Breloom", "Ludicolo", "Torterra", "Venusaur", "Drapion", "Clodsire", "Raichu", "Jolteon", "Ampharos", "Swampert", "Phanpy", "Garchomp", "Gardevoir", "Espeon", "Metagross", "Golem", "Tyranitar",
 "Shuckle", "Lapras", "Cetitan", "ninetales-alola", "Scizor", "Heracross", "Shedinja", "Goodra", "Druddigon",
 "Dracovish", "Gengar", "Gholdengo", "Dusknoir", "Umbreon", "Obstagoon", "KingGambit",
 "Empoleon", "Aggron", "sandslash-alola", "Azumarill", "Sylveon", "Dachsbun"]

types = {
    "Snorlax": ["Normal"], 
    "KangasKhan": ["Normal"], 
    "Maushold": ["Normal"], 
    "Arcanine": ["Fire"], 
    "Charizard": ["Fire", "Flying"], 
    "Ceruledge": ["Fire", "Ghost"], 
    "Hitmontop": ["Fighting"], 
    "Annihilape": ["Fighting", "Ghost"], 
    "Lucario": ["Fighting", "Steel"], 
    "Blastoise": ["Water"], 
    "Feraligatr": ["Water"], 
    "Politoed": ["Water"], 
    "Gyarados": ["Water", "Flying"], 
    "Dragonite": ["Dragon", "Flying"], 
    "Corviknight": ["Flying", "Steel"], 
    "Breloom": ["Grass", "Fighting"], 
    "Ludicolo": ["Grass", "Water"], 
    "Torterra": ["Grass", "Ground"], 
    "Venusaur": ["Grass", "Poison"], 
    "Drapion": ["Poison", "Dark"], 
    "Clodsire": ["Poison", "Ground"], 
    "Raichu": ["Electric"], 
    "Jolteon": ["Electric"], 
    "Ampharos": ["Electric"], 
    "Swampert": ["Ground", "Water"], 
    "Phanpy": ["Ground"], 
    "Garchomp": ["Ground", "Dragon"], 
    "Gardevoir": ["Psychic", "Fairy"], 
    "Espeon": ["Psychic"], 
    "Metagross": ["Psychic", "Steel"], 
    "Golem": ["Rock", "Ground"], 
    "Tyranitar": ["Rock", "Dark"], 
    "Shuckle": ["Rock", "Bug"], 
    "Lapras": ["Water", "Ice"], 
    "Cetitan": ["Ice"], 
    "ninetales-alola": ["Ice", "Fairy"], 
    "Scizor": ["Steel", "Bug"], 
    "Heracross": ["Bug", "Fighting"], 
    "Shedinja": ["Bug"], 
    "Goodra": ["Dragon"], 
    "Druddigon": ["Dragon", "Flying"], 
    "Dracovish": ["Dragon", "Water"], 
    "Gengar": ["Ghost", "Poison"], 
    "Gholdengo": ["Ghost", "Steel"], 
    "Dusknoir": ["Ghost"], 
    "Umbreon": ["Dark"], 
    "Obstagoon": ["Dark", "Normal"], 
    "KingGambit": ["Dark", "Steel"], 
    "Empoleon": ["Water", "Steel"], 
    "Aggron": ["Steel"], 
    "sandslash-alola": ["Steel"], 
    "Azumarill": ["Water", "Fairy"], 
    "Sylveon": ["Fairy"], 
    "Dachsbun": ["Fairy"]
}


newtypes = []
shuffle(x)
i = 0
loadouts = ""
for y in x:
    print(y)
    url = 'https://www.smogon.com/dex/sv/pokemon/' + y + '/'
    if i < 6:
        #ssl._create_default_https_context = ssl._create_unverified_context
        #webbrowser.open(url)

        #make sure that the new pokemon's types are unique to the team
        type = types[y]
        addToTeam = True
        newtypesinterim = []
        for x in type:
            if x in newtypes:
                i -= 1
                addToTeam = False
                break
            else:
                newtypesinterim.append(x)
        if addToTeam:
            newtypes += newtypesinterim
            loadouts += getMon(y)

        """
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        title_index = html.find("<title>")
        start_index = title_index + len("<title>")
        end_index = html.find("</title>")
        title = html[start_index:end_index]
        print("start:" + str(start_index))
        print("end" + str(end_index))
        print(title)
        print(html[:100])
        """

    i += 1

pc.copy(loadouts)