from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDExtendedFabButton

Builder.load_file("client/layouts/match.kv")

class BotMDExtendedFabButton(MDExtendedFabButton):
    bot_id = ""

class Match(MDScreen):
    current_count = 0
    current_stage = ""
    current_bot_1_character = ""
    current_bot_2_character = ""
    selected_bot = ""
    
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

    def bot_button_clicked(self, button):
        self.selected_bot = button.bot_id
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'select_bot'
        self.manager.transition.duration = 0.4

    def bot_character_clicked(self, button):
        if self.selected_bot == "bot_1":
            self.current_bot_1_character = button.character_name
        else:
            self.current_bot_2_character = button.character_name
        self.populate_bot_button_image(button.children[0].source)
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'left'
        self.manager.current = 'match'
        self.manager.transition.duration = 0.4

    def populate_bot_button_image(self, image_source):
        id = self.selected_bot + '_button'
        button = self.ids.get(id) 
        image = button.children[0]
        image.source = image_source
        image.opacity = 1