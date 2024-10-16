import datetime
import random

# FORMATS:
# "standard_2p_pick"
# "standard_2p_random"
# "standard_3p_picks"
# "standard_3p_random"
# "handicap_2p_pick"
# "handicap_2p_random"
# "handicap_3p_pick"
# "handicap_3p_random"

global current_match

def reset_current_match():
    current_match = current_match_template

def get_current_match():
    return current_match

def get_current_match_value_from_key(key):
    return current_match[key]

def set_current_format():
    current_match["format"] = current_match["game_mode_str"] + '_' + current_match["num_players_str"] + '_' + current_match["character_mode_str"]

def append_list_member(key, value):
    current_match[key].append(value)

def set_current_match(key, value):
    current_match[key] = value

def remove_key_from_current_match(key):
    try:
        del current_match[key]
    except KeyError:
        pass

# key == player_name, value == player_id
def add_player(key, value):
    current_match["players"][key] = value

def get_random_character():
    return random.choice(character_list)

def get_character_by_name(character_name):
    for name, image in character_list:
        if name == character_name:
            return (name, image)
    return None

# Make updating stat dictionaries easier
def set_stat(stat, player, value):
    current_match[stat][player] = value

def increment_stat(stat, player, value):
    current_match[stat][player] += value

def append_player_character_list(player, character):
    current_match["player_characters"][player].append(character)

current_match_template = {
    "game_mode_str": "standard",
    "num_players_str": "2p",
    "character_mode_str": "pick",
    "format": "standard_2p_pick",
    "length": 0,
    "players": {},
    "player_characters": {},
    "player_stocks": {},
    "player_deaths": {},
    "player_1v1_clutches": {},
    "player_1v2_clutches": {},
    "current_stage": "",
    "bot_1_info_list": [],
    "bot_2_info_list": [],
    "stages": [],
    "date": datetime.datetime.now(),
    "duration": 0,
    "concluded": False
}

current_match = current_match_template

character_list = [
    ("Mario", "resources/character_images/mario.png"),
    ("Donkey Kong", "resources/character_images/donkeykong.png"),
    ("Link", "resources/character_images/link.png"),
    ("Samus", "resources/character_images/samus.png"),
    ("Dark Samus", "resources/character_images/darksamus.png"),   
    ("Josh", "resources/character_images/Josh.png"),
    ("Kirby", "resources/character_images/kirby.png"),
    ("Fox", "resources/character_images/fox.png"),
    ("Pikachu", "resources/character_images/pikachu.png"),
    ("Luigi", "resources/character_images/luigi.png"),
    ("Ness", "resources/character_images/ness.png"),
    ("Captain Falcon", "resources/character_images/captainfalcon.png"),
    ("Jigglypuff", "resources/character_images/jigglypuff.png"),
    ("Peach", "resources/character_images/peach.png"),
    ("Daisy", "resources/character_images/daisy.png"),
    ("Bowser", "resources/character_images/bowser.png"),
    ("Ice Climbers", "resources/character_images/iceclimbers.png"),
    ("Sheik", "resources/character_images/sheik.png"),
    ("Zelda", "resources/character_images/zelda.png"),
    ("Dr. Mario", "resources/character_images/drmario.png"),
    ("Pichu", "resources/character_images/pichu.png"),
    ("Falco", "resources/character_images/falco.png"),
    ("Marth", "resources/character_images/woman.png"),
    ("Lucina", "resources/character_images/lucina.png"),
    ("Young Link", "resources/character_images/younglink.png"),
    ("Ganondorf", "resources/character_images/ganon.png"),
    ("Mewtwo", "resources/character_images/mewtwo.png"),
    ("Roy", "resources/character_images/roy.png"),
    ("Chrom", "resources/character_images/chrom.png"),
    ("Mr. Game and Watch", "resources/character_images/mrgameandwatch.png"),
    ("Meta Knight", "resources/character_images/metaknight.png"),
    ("Pit", "resources/character_images/pit.png"),
    ("Dark Pit", "resources/character_images/darkpit.png"),
    ("Zero Suit Samus", "resources/character_images/zss.png"),
    ("Wario", "resources/character_images/wario.png"),
    ("Snake", "resources/character_images/snake.png"),
    ("Ike", "resources/character_images/ike.png"),
    ("Pokemon Trainer", "resources/character_images/pt.png"),
    ("Diddy Kong", "resources/character_images/diddy.png"),
    ("Lucas", "resources/character_images/lucas.png"),
    ("Sonic", "resources/character_images/sonic.png"),
    ("King Dedede", "resources/character_images/ddd.png"),
    ("Olimar", "resources/character_images/olimar.png"),
    ("Lucario", "resources/character_images/lucario.png"),
    ("R.O.B", "resources/character_images/rob.png"),
    ("Toon Link", "resources/character_images/toonlink.png"),
    ("Wolf", "resources/character_images/wolf.png"),
    ("Villager", "resources/character_images/villager.png"),
    ("Mega Man", "resources/character_images/megaman.png"),
    ("Wii Fit Trainer", "resources/character_images/wiifit.png"),
    ("Rosalina & Luma", "resources/character_images/rosa.png"),
    ("Little Mac", "resources/character_images/littlemac.png"),
    ("Greninja", "resources/character_images/greninja.png"),
    ("Palutena", "resources/character_images/palutena.png"),
    ("Pac-Man", "resources/character_images/pacman.png"),
    ("Robin", "resources/character_images/robin.png"),
    ("Shulk", "resources/character_images/shulk.png"),
    ("Bowser Jr.", "resources/character_images/jr.png"),
    ("Duck Hunt Dog", "resources/character_images/duckhunt.png"),
    ("Ryu", "resources/character_images/ryu.png"),
    ("Ken", "resources/character_images/ken.png"),
    ("Cloud", "resources/character_images/cloud.png"),
    ("Corrin", "resources/character_images/corrin.png"),
    ("Bayonetta", "resources/character_images/bayo.png"),
    ("Inkling", "resources/character_images/inkling.png"),
    ("Ridley", "resources/character_images/ridley.png"),
    ("Simon", "resources/character_images/simon.png"),
    ("Richter", "resources/character_images/richter.png"),
    ("King K. Rool", "resources/character_images/kingk.png"),
    ("Isabelle", "resources/character_images/isabelle.png"),
    ("Incineroar", "resources/character_images/incin.png"),
    ("Piranha Plant", "resources/character_images/pplant.png"),
    ("Joker", "resources/character_images/joker.png"),
    ("Hero", "resources/character_images/hero.png"),
    ("Banjo Kazooie", "resources/character_images/banjo.png"),
    ("Terry", "resources/character_images/terry.png"),
    ("Byleth", "resources/character_images/byleth.png"),
    ("Min Min", "resources/character_images/minmin.png"),
    ("Steve", "resources/character_images/steve.png"),
    ("Sephiroth", "resources/character_images/sephiroth.png"),
    ("Pyra and Mythra", "resources/character_images/pyra.png"),
    ("Kazuya", "resources/character_images/kazuya.png"),
    ("Sora", "resources/character_images/sora.png"),
    ("Mii Brawler", "resources/character_images/brawler.png"),
    ("Mii Gunner", "resources/character_images/gunner.png"),
    ("Mii Swordfighter", "resources/character_images/sword.png"),
]