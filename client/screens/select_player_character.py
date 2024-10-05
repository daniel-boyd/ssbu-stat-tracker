from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from .. import shared

Builder.load_file("client/layouts/select_player_character.kv")

class SelectPlayerCharacter(MDScreen):
    selected_player = None

    def on_pre_enter(self):
        player_1_label = self.ids.player_1_label
        player_2_label = self.ids.player_2_label
        player_1_label.text = shared.get_current_match_value_from_key("player_1")
        player_2_label.text = shared.get_current_match_value_from_key("player_2")

    # Cleanup buttons and current_match keys on enter
    def cleanup(self):
        player_1_button = self.ids.player_1_button
        player_2_button = self.ids.player_2_button
        shared.set_current_match("player_1_character", "")
        shared.set_current_match("player_2_character", "")
        player_1_button.children[0].opacity = 0
        player_2_button.children[0].opacity = 0
        player_1_button.children[0].source = ''
        player_2_button.children[0].source = ''

    def on_back_button_clicked(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'select_character_mode'
        self.cleanup()

    def on_character_button_pressed(self, button):
        character_name = button.character_name
        selected_player_key = self.selected_player + '_character'
        shared.set_current_match(selected_player_key, character_name)
        self.populate_player_button_image(button.children[0].source)
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'down'
        self.manager.current = 'select_player_character'
        self.manager.transition.duration = 0.4
        current_match = shared.get_current_match()
        print(current_match)

    def populate_player_button_image(self, image_source):
        id = self.selected_player + '_button'
        button = self.ids.get(id) 
        image = button.children[0]
        image.source = image_source
        image.opacity = 1

    def player1_button_clicked(self):
        self.selected_player = "player_1"
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'select_character'
        self.manager.transition.duration = 0.4

    def player2_button_clicked(self):
        self.selected_player = "player_2"
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'select_character'
        self.manager.transition.duration = 0.4
    
    def start_button_clicked(self):
        current_match = shared.get_current_match()
        # For players 1-3, check if they have a character selected before allowing the match to start
        for index in range(1, 3):
            plr_char_str = f"player_{index}_character"
            if current_match[plr_char_str] == "":
                print(plr_char_str + " not selected")
                return
        self.manager.transition.direction = 'left'
        self.manager.current = 'match'
