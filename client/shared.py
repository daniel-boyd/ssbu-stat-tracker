import datetime

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
    "player_1_kills": 0,
    "player_2_kills": 0,
    "player_1_deaths": 0,
    "player_2_deaths": 0,
    "player1_1v1_clutches": 0,
    "player2_1v1_clutches": 0,
    "player1_1v2_clutches": 0,
    "player2_1v2_clutches": 0,
    "date": datetime.datetime.now(),
    "duration": 0,
    "concluded": False
}

def get_current_match():
    return current_match

def set_current_format():
    current_match["format"] = current_match["game_mode_str"] + '_' + current_match["num_players_str"] + '_' + current_match["character_mode_str"]


def set_current_match(key, value):
    current_match[key] = value