import datetime
from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDExtendedFabButton
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText

Builder.load_file("client/layouts/match.kv")

class BotMDExtendedFabButton(MDExtendedFabButton):
    bot_id = ""

# REFACTOR: make current_match("players") list of players rather than player_1 player_2
# Instead of player_1_button, player_2_button; player_button_1, player_button_2 -- they will be used dynamically for different players in 3p
# refac for select_player_names, ...

# TODO: VERIFY PLAYER STATS GET SET BEFORE ALLOWING CONTINUE
# TODO: IMPLEMENT RANDOM PLAYER CHARS
class Match(MDScreen):

    # Format info
    # in-line comments signify format if var is False
    is_3p = False # 2p
    is_random = False # picks
    is_handicap = False # standard
    # Increment on win if 3p
    current_state = 0
    states_3p = [
        (1, 2),
        (3, 1),
        (2, 3),
        (1, 2)
    ]

    # Match Info
    # Player stats are dictionaries with player id as the key and stat as the value
    # Get dnl's stocks: player_stocks[shared.get_current_match_value_from_key["players"]["dnl"]]
    current_count = 0
    current_stage = ""

    player_stocks = {}
    player_died = {}
    player_1v1_clutched = {}
    player_1v2_clutched = {}
    # "name": "char_name" represents current character of each player, for random, list is saved in current_match
    player_characters = {}
    player_character_image_sources = {}
    bot_1_stocks = 0
    bot_2_stocks = 0
    bot_1_died = False
    bot_2_died = False
    bot_1_1v1_clutched = False
    bot_2_1v1_clutched = False
    bot_1_1v2_clutched = False
    bot_2_1v2_clutched = False
    current_bot_1_character = ""
    current_bot_2_character = ""
    current_bot_1_character_image_source = ""
    current_bot_2_character_image_source = ""
    selected_player = ""
    current_starting_percentage = 0

    # Flags
    start_time_reset = True

    # Pre-declarations
    dialog = None
    
    def on_pre_enter(self):
        # Runs once
        if self.start_time_reset:
            self.init_player_stats()
            self.set_format()
            self.set_player_characters()
            self.reset_stats_in_memory()
            self.populate_bot_button_images()
            shared.set_current_match("date", datetime.datetime.now())
            self.start_time_reset = False

        player_label_1 = self.ids.player_label_1
        player_label_2 = self.ids.player_label_2
        player_label_1.text = shared.get_current_match_value_from_key("players")[1]
        player_label_2.text = shared.get_current_match_value_from_key("players")[2]

    # If random remove current_match player char members, add current_match char lists
    def set_format(self):
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            # 3p Random: Remove p1 & p2 char strings, add name1, name2, name3 char lists
            if shared.get_current_match_value_from_key("character_mode_str") == "random":
                pass
            # 3p Pick: add p3 char string
            else:
                pass
        # 2p
        else:
            # 2p Random: Remove p1 & p2 char strings, add p1, p2 char lists
            if shared.get_current_match_value_from_key("character_mode_str") == "random":
                pass
        # Handicap: add highest_starting_percent int
        if shared.get_current_match_value_from_key("game_mode_str") == "handicap":
            shared.set_current_match("highest_starting_percentage", 0)

    # Create stat dictionaries with stat values mapped to player names
    # Dynamicically populated for varying names and player count
    def reset_stats_in_memory(self):
        players = shared.get_current_match()["players"]
        for player_id, player_name in players.items():
            print(player_name)
            self.player_stocks[player_name] = 0
            self.player_died[player_name] = False
            self.player_1v1_clutched[player_name] = False
            self.player_1v2_clutched[player_name] = False

    # For 3p: cycle out stale player for new player
    def cycle_players(self):
        # Get player 1, 2, or 3 based on the current active player state,
        # Set the player_name property of the button so that selected_player can be set to the correct player
        # Set the player_labels for aesthetics :)
        self.ids.player_button_1.player_name = shared.get_current_match_value_from_key("players")[self.states_3p[0]]
        self.ids.player_button_2.player_name = shared.get_current_match_value_from_key("players")[self.states_3p[1]]
        self.ids.player_label_1.text = shared.get_current_match_value_from_key("players")[self.states_3p[0]]
        self.ids.player_label_2.player_name = shared.get_current_match_value_from_key("players")[self.states_3p[1]]

    def set_player_characters(self):

        if shared.get_current_match_value_from_key("character_mode_str") == "random":
            # Randomize player chars
            player_rand_1 = shared.get_random_character()
            player_rand_2 = shared.get_random_character()

            if shared.get_current_match_value_from_key("num_players_str") == "3p":
                # Yeah, this looks ridiculous. It's setting the characters of the two active players based on the active state
                self.player_characters[shared.get_current_match_value_from_key("players")[self.states_3p[self.current_state[0]]]] = player_rand_1[0]
                self.player_character_image_sources[shared.get_current_match_value_from_key("players")[self.states_3p[self.current_state[0]]]] = player_rand_1[1]
                self.player_characters[shared.get_current_match_value_from_key("players")[self.states_3p[self.current_state[1]]]] = player_rand_2[0]
                self.player_character_image_sources[shared.get_current_match_value_from_key("players")[self.states_3p[self.current_state[1]]]] = player_rand_2[1]
            else:
                self.player_characters[shared.get_current_match_value_from_key("players")[1]] = player_rand_1[0]
                self.player_character_image_sources[shared.get_current_match_value_from_key("players")[1]] = player_rand_1[1]
                self.player_characters[shared.get_current_match_value_from_key("players")[2]] = player_rand_2[0]
                self.player_character_image_sources[shared.get_current_match_value_from_key("players")[2]] = player_rand_2[1]

            player_button_1 = self.ids.get("player_button_1")
            player_image_1 = player_button_1.children[0]
            player_image_1.source = self.player_character_image_sources[shared.get_current_match_value_from_key("players")[1]]
            player_image_1.opacity = 1
            player_button_2 = self.ids.get("player_button_2")
            player_image_2 = player_button_2.children[0]
            player_image_2.source = self.player_character_image_sources[shared.get_current_match_value_from_key("players")[2]]
            player_image_2.opacity = 1

        # If mode is picks, set player_button_1 and player_button_2 images to player_1 and player_2 character selection images
        else:
            # Get player chars and image sources
            player_rand_1 = shared.get_character_by_name()
            player_rand_2 = shared.get_character_by_name()

            if shared.get_current_match_value_from_key("num_players_str") == "3p":
                # LEFT OFF: Get the two active players, retrieve their characters using player_characters, and populate their images
                
            else:
                self.player_characters[shared.get_current_match_value_from_key("players")[1]] = player_rand_1[0]
                self.player_character_image_sources[shared.get_current_match_value_from_key("players")[1]] = player_rand_1[1]
                self.player_characters[shared.get_current_match_value_from_key("players")[2]] = player_rand_2[0]
                self.player_character_image_sources[shared.get_current_match_value_from_key("players")[2]] = player_rand_2[1]

            player_1_image_source, player_2_image_source = self.manager.get_screen('select_player_character').get_player_image_sources()
            player_button_1 = self.ids.get('player_button_1')
            player_button_2 = self.ids.get('player_button_2')
            player_image_1 = player_button_1.children[0]
            player_image_2 = player_button_2.children[0]
            player_image_1.source = player_1_image_source
            player_image_2.source = player_2_image_source
            player_image_1.opacity = 1
            player_image_2.opacity = 1
        
    def stage_screen_button_clicked(self):
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'stage_list'
        self.manager.transition.duration = 0.4

    def stage_button_clicked(self, stage, image_source):
        self.current_stage = stage
        print(image_source)
        button = self.ids.get('stage_button')
        image = button.children[0]
        image.source = image_source
        image.opacity = 1
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'down'
        self.manager.current = 'match'
        self.manager.transition.duration = 0.4

    def player_button_clicked(self, button):
        # TODO: set player_name concurrently with setting chars (if 3p)
        self.selected_player = button.player_id
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'set_player_stats'
        self.manager.transition.duration = 0.4

    def bot_character_clicked(self):
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'left'
        self.manager.current = 'set_player_stats'
        self.manager.transition.duration = 0.4

    def populate_bot_button_images(self):

        # Randomize bot chars
        bot_1_rand = shared.get_random_character()
        bot_2_rand = shared.get_random_character()
        self.current_bot_1_character = bot_1_rand[0]
        self.current_bot_1_character_image_source = bot_1_rand[1]
        self.current_bot_2_character = bot_2_rand[0]
        self.current_bot_2_character_image_source = bot_2_rand[1]
        bot_1_button = self.ids.get("bot_1_button")
        bot_1_image = bot_1_button.children[0]
        bot_1_image.source = self.current_bot_1_character_image_source
        bot_1_image.opacity = 1
        bot_2_button = self.ids.get("bot_2_button")
        bot_2_image = bot_2_button.children[0]
        bot_2_image.source = self.current_bot_2_character_image_source
        bot_2_image.opacity = 1

    # TODO: extend for 3p
    def stocks_button_clicked(self, button):
        if self.selected_player == "player_1":
            self.player_1_stocks = int(button.stocks)
        elif self.selected_player == "player_2":
            self.player_2_stocks = int(button.stocks)
        elif self.selected_player == "bot_1":
            self.bot_1_stocks = int(button.stocks)
        elif self.selected_player == "bot_2":
            self.bot_2_stocks = int(button.stocks)

    def on_died_checkbox_active(self, checkbox, active):
        if self.selected_player == "player_1":
            self.player_1_died = active
        elif self.selected_player == "player_2":
            self.player_2_died = active
        elif self.selected_player == "bot_1":
            self.bot_1_died = active
        elif self.selected_player == "bot_2":
            self.bot_2_died = active

    def on_clutched_1v1_checkbox_active(self, checkbox, active):
        if self.selected_player == "player_1":
            self.player_1_1v1_clutched = active
        elif self.selected_player == "player_2":
            self.player_2_1v1_clutched = active
        elif self.selected_player == "bot_1":
            self.bot_1_1v1_clutched = active
        elif self.selected_player == "bot_2":
            self.bot_2_1v1_clutched = active

    def on_clutched_1v2_checkbox_active(self, checkbox, active):
        if self.selected_player == "player_1":
            self.player_1_1v2_clutched = active
        elif self.selected_player == "player_2":
            self.player_2_1v2_clutched = active
        elif self.selected_player == "bot_1":
            self.bot_1_1v2_clutched = active
        elif self.selected_player == "bot_2":
            self.bot_2_1v2_clutched = active

    def on_confirm_button_clicked(self):
        self.selected_player = ""
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'match'
        self.manager.transition.duration = 0.4
        died_checkbox = self.manager.get_screen('set_player_stats').ids.get("died_checkbox")
        clutched_1v1_checkbox = self.manager.get_screen('set_player_stats').ids.get("clutched_1v1_checkbox")
        clutched_1v2_checkbox = self.manager.get_screen('set_player_stats').ids.get("clutched_1v2_checkbox")
        died_checkbox.active = False
        clutched_1v1_checkbox.active = False
        clutched_1v2_checkbox.active = False

    def reset_stats(self):
        self.current_stage = ""
        self.player_1_stocks = 0
        self.player_2_stocks = 0
        self.player_1_died = False
        self.player_2_died = False
        self.player_1_1v1_clutched = False
        self.player_2_1v1_clutched = False
        self.player_1_1v2_clutched = False
        self.player_2_1v2_clutched = False
        self.bot_1_stocks = 0
        self.bot_2_stocks = 0
        self.bot_1_died = False
        self.bot_2_died = False
        self.bot_1_1v1_clutched = False
        self.bot_2_1v1_clutched = False
        self.bot_1_1v2_clutched = False
        self.bot_2_1v2_clutched = False
        self.current_bot_1_character = ""
        self.current_bot_2_character = ""
        self.selected_player = ""

    # To be called on pre enter
    # Set shared stat dictionaries with player names as keys and default values
    def init_player_stats(self):
        num_players = 2
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            num_players = 3
        index = 1
        while index <= num_players:
            player_name = shared.get_current_match_value_from_key("players")[index]
            shared.set_stat("player_stocks", player_name, 0)
            shared.set_stat("player_deaths", player_name, 0)
            shared.set_stat("player_1v1_clutches", player_name, 0)
            shared.set_stat("player_1v2_clutches", player_name, 0)
            shared.set_stat("player_characters", player_name, [])
            index += 1

    # Save and reset player member vars
    def update_player_stats(self):
        num_players = 2
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            num_players = 3
        index = 1
        while index <= num_players:
            # Increment current_match stocks
            player_name = shared.get_current_match_value_from_key("players")[index]
            print(self.player_stocks)
            shared.increment_stat("player_stocks", player_name, self.player_stocks[player_name])
            # Increment current_match deaths
            if self.player_died[player_name]:
                shared.increment_stat("player_deaths", player_name, 1)
            # Increment current_match 1v1_clutches
            if self.player_1v1_clutched[player_name]:
                shared.increment_stat("player_1v1_clutches", player_name, 1)
            # Increment current_match 1v2 clutches
            if self.player_1v2_clutched[player_name]:
                shared.increment_stat("player_1v2_clutches", player_name, 1)
            # Append current_match character
            if shared.get_current_match_value_from_key("character_mode_str") == "pick":
                print("The ONE!")
                print(self.player_characters)
                shared.append_player_character_list(player_name, self.player_characters[player_name])
            elif shared.get_current_match_value_from_key("character_mode_str") == "random":
                shared.set_stat("player_characters", self.player_characters[player_name])
            index += 1

        # Stats saved to current_match, reset them in self
        self.reset_stats_in_memory()

    # Save and reset match member vars and bot member vars
    def update_current_match(self):

        start_date_time = shared.get_current_match_value_from_key("date")
        shared.set_current_match("duration", datetime.datetime.now() - start_date_time)

        shared.set_current_match("length", self.current_count)

        # char name, stocks, 1v1 clutched, 1v2 clutched
        bot_1_info_list = ["", 0, False, False]
        bot_2_info_list = ["", 0, False, False]

        # set bot stocks
        bot_1_info_list[0] = self.current_bot_1_character
        bot_2_info_list[0] = self.current_bot_2_character
        bot_1_info_list[1] = self.bot_1_stocks
        bot_2_info_list[1] = self.bot_2_stocks
        if self.bot_1_1v1_clutched:
            bot_1_info_list[2] = True     
        if self.bot_2_1v1_clutched:
            bot_2_info_list[2] = True   
        if self.bot_1_1v2_clutched:
            bot_1_info_list[3] = True                  
        if self.bot_2_1v2_clutched:
            bot_2_info_list[3] = True

        # append bot info
        shared.append_list_member("bot_1_info_list", bot_1_info_list)
        shared.append_list_member("bot_2_info_list", bot_2_info_list)
        
        # append stage list
        shared.append_list_member("stages", self.current_stage)

    def won_button_clicked(self):

        if self.current_bot_1_character == "" or self.current_bot_2_character == "" or self.current_stage == "":
            return
        
        self.update_player_stats()
        self.update_current_match()

        # Increment the player state and update necessary vars and properties
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            self.current_state += 1
            self.cycle_players()
        
        self.current_count += 1

        if shared.get_current_match_value_from_key("character_mode_str") == "handicap":
            self.current_starting_percentage += 10
            shared.set_current_match("highest_starting_percentage", self.current_starting_percentage)

        counter_label = self.ids.get("counter_label")
        counter_label.text = str(self.current_count)
        bot_1_button = self.ids.get('bot_1_button')
        bot_2_button = self.ids.get('bot_2_button')
        stage_button = self.ids.get('stage_button')
        bot_1_image = bot_1_button.children[0]
        bot_2_image = bot_2_button.children[0]
        stage_image = stage_button.children[0]
        bot_1_image.source = ''
        bot_2_image.source = ''
        stage_image.source = ''
        bot_1_image.opacity = 0
        bot_2_image.opacity = 0
        stage_image.opacity = 0
        self.reset_stats()
        self.populate_bot_button_image()

    def dialog_close(self, *args):
        print("DISMISSED")
        if self.dialog:
            try:
                self.dialog.dismiss(force=True)  # Attempt to dismiss the dialog
                self.dialog = None  # Reset the dialog reference
            except Exception as e:
                print(f"Error dismissing dialog: {e}")

    def end_button_clicked(self):
        if self.dialog is None:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Confirm",
                ),
                MDButton(
                    MDButtonText(
                        text="Yes"
                    )
                ),
                MDButton(
                    MDButtonText(
                        text="No",
                        on_release=self.dialog_close
                    )
                ),
                size_hint=(0.2, 1)
            )
        
        self.dialog.open()  # Open the dialog

    def cleanup(self):
        self.start_time_reset = True