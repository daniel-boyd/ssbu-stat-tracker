from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen
from .. import shared

class SelectPlayerCharacter(MDScreen):
    selected_player = None
    is_pre_enter_called = False

    def __init__(self, kv_file=None, **kwargs):
        super().__init__(**kwargs)
        if kv_file:
            self.load_kv_file(kv_file)

    def on_pre_enter(self):
        if self.is_pre_enter_called:
            return
        self.is_pre_enter_called = True
        kv_file = ""
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            kv_file = './layouts/select_player_character_3p.kv'
        else:
            kv_file = './layouts/select_player_character_2p.kv'
        self.manager.reinitialize_screen(SelectPlayerCharacter, 'select_player_character', kv_file)

    def on_enter(self):
        self.is_pre_enter_called = False

    def load_kv_file(self, kv_file):
        """Load the specified .kv file."""
        Builder.unload_file('./layouts/select_player_character_3p.kv')
        Builder.unload_file('./layouts/select_player_character_2p.kv')
        Builder.load_file(kv_file)

    # Cleanup buttons and current_match keys on enter
    def cleanup(self):
        Builder.unload_file('./layouts/select_player_character_3p.kv')
        Builder.unload_file('./layouts/select_player_character_2p.kv')
        player_1_button = self.ids.player_1_button
        player_2_button = self.ids.player_2_button
        shared.set_current_match("player_1_character", "")
        shared.set_current_match("player_2_character", "")
        player_1_button.children[0].opacity = 0
        player_2_button.children[0].opacity = 0
        player_1_button.children[0].source = ''
        player_2_button.children[0].source = ''

        # 3p cleanup
        if shared.get_current_match_value_from_key("num_players_str") == "3p":
            player_3_button = self.ids.player_3_button
            shared.set_current_match("player_3_character", "")
            player_3_button.children[0].opacity = 0
            player_3_button.children[0].source = ''

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

    def player3_button_clicked(self):
        self.selected_player = "player_3"
        self.manager.transition.duration = 0.1
        self.manager.transition.direction = 'up'
        self.manager.current = 'select_character'
        self.manager.transition.duration = 0.4
    
    def start_button_clicked(self):
        # For players 1-3, check if they have a character selected before allowing the match to start
        for index in range(1, 3):
            plr_char_str = f"player_{index}_character"
            if shared.get_current_match_value_from_key(plr_char_str) == "":
                return
        self.manager.transition.direction = 'left'
        self.manager.current = 'match_screen'
