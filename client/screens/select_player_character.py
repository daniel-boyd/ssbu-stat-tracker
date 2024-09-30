from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from .. import shared

Builder.load_file("client/layouts/select_player_character.kv")

class SelectPlayerCharacter(MDScreen):
    selected_player_key = None

    def on_back_button_clicked(self):
        self.manager.current = 'select_character_mode'

    def on_character_button_pressed(self, button):
        character_name = button.character_name
        shared.set_current_match(self.selected_player_key, character_name)
        self.manager.current = 'select_player_character'
        current_match = shared.get_current_match()
        print(current_match)

    def player1_button_clicked(self):
        self.selected_player_key = "player_1_character"
        self.manager.current = 'select_character'

    def player2_button_clicked(self):
        self.selected_player_key = "player_2_character"
        self.manager.current = 'select_character'
    
    def start_button_clicked(self):
        current_match = shared.get_current_match()
        # For players 1-3, check if they have a character selected before allowing the match to start
        for index in range(1, 3):
            plr_char_str = f"player_{index}_character"
            if current_match[plr_char_str] == "":
                print(plr_char_str + " not selected")
                return
        self.manager.current = 'match_screen'
