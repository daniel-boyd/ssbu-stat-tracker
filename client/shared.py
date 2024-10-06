import datetime
import random

global current_match

# FORMATS:
# "standard_2p_pick"
# "standard_2p_random"
# "standard_3p_picks"
# "standard_3p_random"
# "handicap_2p_pick"
# "handicap_2p_random"
# "handicap_3p_pick"
# "handicap_3p_random"

current_match = {
    "game_mode_str": "standard",
    "num_players_str": "2p",
    "character_mode_str": "pick",
    "format": "standard_2p_pick",
    "length": 0,
    "player_1": "",
    "player_2": "",
    "player_1_character": "",
    "player_2_character": "",
    "player_1_stocks": 0,
    "player_2_stocks": 0,
    "player_1_died": 0,
    "player_2_died": 0,
    "player_1_1v1_clutches": 0,
    "player_2_1v1_clutches": 0,
    "player_1_1v2_clutches": 0,
    "player_2_1v2_clutches": 0,
    "current_stage": "",
    "bot_1_info_list": [],
    "bot_2_info_list": [],
    "stages": [],
    "date": datetime.datetime.now(),
    "duration": 0,
    "concluded": False
}

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
    ("Mr Game and Watch", "resources/character_images/mrgameandwatch.png"),
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
    ("ROB", "resources/character_images/rob.png"),
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
    ("Duck Hunt", "resources/character_images/duckhunt.png"),
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
    ("Banjo", "resources/character_images/banjo.png"),
    ("Terry", "resources/character_images/terry.png"),
    ("Byleth", "resources/character_images/byleth.png"),
    ("Min Min", "resources/character_images/minmin.png"),
    ("Steve", "resources/character_images/steve.png"),
    ("Sephiroth", "resources/character_images/sephiroth.png"),
    ("Pyra and Mythra", "resources/character_images/pyra.png"),
    ("Kazuya", "resources/character_images/kazuya.png"),
    ("Sora", ""),
    ("Mii Brawler", "resources/character_images/brawler.png"),
    ("Mii Gunner", "resources/character_images/gunner.png"),
    ("Mii Swordfighter", "resources/character_images/sword.png"),
]

def pretty_print_current_match():
    # Assuming current_match is already defined with the necessary structure
    match_info = f"""
    Current Match Information:
    ---------------------------
    Game Mode: {current_match["game_mode_str"]}
    Number of Players: {current_match["num_players_str"]}
    Character Mode: {current_match["character_mode_str"]}
    Format: {current_match["format"]}
    Length: {current_match["length"]}
    
    Players:
    ---------------
    Player 1: {current_match["player_1"]}
        Character: {current_match["player_1_character"]}
        Stocks: {current_match["player_1_stocks"]}
        Died: {current_match["player_1_died"]}
        1v1 Clutches: {current_match["player_1_1v1_clutches"]}
        1v2 Clutches: {current_match["player_1_1v2_clutches"]}
    
    Player 2: {current_match["player_2"]}
        Character: {current_match["player_2_character"]}
        Stocks: {current_match["player_2_stocks"]}
        Died: {current_match["player_2_died"]}
        1v1 Clutches: {current_match["player_2_1v1_clutches"]}
        1v2 Clutches: {current_match["player_2_1v2_clutches"]}
    
    Current Stage: {current_match["current_stage"]}
    
    Bots:
    -----------------
    Bot 1:
        {current_match["bot_1_info_list"]}
    
    Bot 2:
        {current_match["bot_2_info_list"]}
    
    Stages: {', '.join(current_match["stages"]) if current_match["stages"] else "None"}
    
    Date: {current_match["date"].strftime('%Y-%m-%d %H:%M:%S')}
    Duration: {current_match["duration"]} seconds
    Concluded: {'Yes' if current_match["concluded"] else 'No'}
    """

    print(match_info)


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

def add_player_3():
    current_match["num_players_str"] = "3p"
    current_match["player_3"] = ""
    current_match["player_3_character"] = ""
    current_match["player_3_stocks"] = 0
    current_match["player_3_died"] = 0
    current_match["player3_1v1_clutches"] = 0
    current_match["player3_1v2_clutches"] = 0

def remove_player_3():
    current_match["num_players_str"] = "2p"
    remove_key_from_current_match("player_3")
    remove_key_from_current_match("player_3_character")
    remove_key_from_current_match("player_3_stocks")
    remove_key_from_current_match("player_3_died")
    remove_key_from_current_match("player3_1v1_clutches")
    remove_key_from_current_match("player3_1v2_clutches")

def get_random_character():
    return random.choice(character_list)