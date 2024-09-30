from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("client/layouts/main_menu.kv")

class MainMenu(MDScreen):
    def on_play_button_click(self):
        self.manager.transition.direction = "left"
        self.manager.current = 'select_player_count'
