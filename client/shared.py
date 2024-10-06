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