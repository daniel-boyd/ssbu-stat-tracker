from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDExtendedFabButton

Builder.load_file("client/layouts/match.kv")

class BotMDExtendedFabButton(MDExtendedFabButton):
    bot_id = ""

# TODO: VERIFY PLAYER STATS GET SET BEFORE ALLOWING CONTINUE
class Match(MDScreen):
    current_count = 0
    current_stage = ""
    player_1_stocks = 0
    player_2_stocks = 0
    player_1_died = False
    player_2_died = False
    player_1_1v1_clutched = False
    player_2_1v1_clutched = False
    player_1_1v2_clutched = False
    player_2_1v2_clutched = False
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
    selected_player = ""
    
    def on_pre_enter(self):
        player_1_label = self.ids.player_1_label
        player_2_label = self.ids.player_2_label
        player_1_label.text = shared.get_current_match_value_from_key("player_1")
        player_2_label.text = shared.get_current_match_value_from_key("player_2")
        player_1_label.text = "dnl"
        player_2_label.text = "cnl"
        self.set_player_character_images()

    def set_player_character_images(self):
        player_1_image_source, player_2_image_source = self.manager.get_screen('select_player_character').get_player_image_sources()
        player_1_button = self.ids.get('player_1_button')
        player_2_button = self.ids.get('player_2_button')
        player_1_image = player_1_button.children[0]
        player_2_image = player_2_button.children[0]
        player_1_image.source = player_1_image_source
        player_2_image.source = player_2_image_source
        player_1_image.opacity = 1
        player_2_image.opacity = 1


    def stage_screen_button_clicked(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'stage_list'

    def stage_button_clicked(self, stage, image_source):
        self.current_stage = stage
        print(image_source)
        button = self.ids.get('stage_button')
        image = button.children[0]
        image.source = image_source
        image.opacity = 1
        self.manager.transition.direction = 'down'
        self.manager.current = 'match'

    def player_button_clicked(self, button):
        self.selected_player = button.player_id
        if self.selected_player == "bot_1" or self.selected_player == "bot_2":
            self.manager.transition.duration = 0.1
            self.manager.transition.direction = 'up'
            self.manager.current = 'select_bot'
            self.manager.transition.duration = 0.4
        else:
            self.manager.transition.duration = 0.1
            self.manager.transition.direction = 'up'
            self.manager.current = 'set_player_stats'
            self.manager.transition.duration = 0.4

    def bot_character_clicked(self, button):
        if self.selected_player == "bot_1":
            self.current_bot_1_character = button.character_name
        else:
            self.current_bot_2_character = button.character_name
        self.populate_bot_button_image(button.children[0].source)
        self.setting_bot_stats = True
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'left'
        self.manager.current = 'set_player_stats'
        self.manager.transition.duration = 0.4

    def populate_bot_button_image(self, image_source):
        id = self.selected_player + '_button'
        button = self.ids.get(id) 
        image = button.children[0]
        image.source = image_source
        image.opacity = 1

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
        print(self.selected_player)
        print(active)
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
            self.bot_1_1v1_clutched = active

    def on_clutched_1v2_checkbox_active(self, checkbox, active):
        if self.selected_player == "player_1":
            self.player_1_1v2_clutched = active
        elif self.selected_player == "player_2":
            self.player_2_1v2_clutched = active
        elif self.selected_player == "bot_1":
            self.bot_1_1v2_clutched = active
        elif self.selected_player == "bot_2":
            self.bot_1_1v2_clutched = active

    def on_confirm_button_clicked(self):
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
        self. player_1_1v1_clutched = False
        self.player_2_1v1_clutched = False
        self.player_1_1v2_clutched = False
        self.player_2_1v2_clutched = False
        self.bot_1_stocks = 0
        self.bot_2_stocks = 0
        self. bot_1_died = False
        self.bot_2_died = False
        self.bot_1_1v1_clutched = False
        self.bot_2_1v1_clutched = False
        self.bot_1_1v2_clutched = False
        self.bot_2_1v2_clutched = False
        self.current_bot_1_character = ""
        self.current_bot_2_character = ""
        self.selected_player = ""

    def update_current_match(self):
        # TODO: append stages, append bots
        shared.set_current_match("length", self.current_count)
        player_1_current_stocks = int(shared.get_current_match_value_from_key("player_1_stocks"))
        player_2_current_stocks = int(shared.get_current_match_value_from_key("player_2_stocks"))
        print(type(player_1_current_stocks))
        shared.set_current_match("player_1_stocks", player_1_current_stocks + self.player_1_stocks)
        shared.set_current_match("player_2_stocks", player_2_current_stocks + self.player_2_stocks)
        if self.player_1_died:
            shared.set_current_match("player_1_died", str(int(shared.get_current_match_value_from_key("player_1_died")) + 1))
        if self.player_2_died:
            shared.set_current_match("player_2_died", str(int(shared.get_current_match_value_from_key("player_2_died")) + 1))
        if self.player_1_1v1_clutched:
            shared.set_current_match("player1_1v1_clutches", str(int(shared.get_current_match_value_from_key("player_1_1v1_clutches")) + 1))                       
        if self.player_2_1v1_clutched:
            shared.set_current_match("player2_1v1_clutches", str(int(shared.get_current_match_value_from_key("player_2_1v1_clutches")) + 1))
        # TODO: ADD BOT CLUTCHES TO CURRENT_MATCH
        # shared.set_current_match("bot1_1v2_clutches", str(int(shared.get_current_match_value_from_key("player_1_1v2_clutches")) + 1)
        # shared.set_current_match("player_2_1v2_clutches", str(int(shared.get_current_match_value_from_key("player_2_1v2_clutches")) + 1)

    def won_button_clicked(self):

        if self.current_bot_1_character == "" or self.current_bot_2_character == "" or self.current_stage == "":
            return
        
        self.update_current_match()

        shared.pretty_print_current_match()

        self.current_count += 1
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