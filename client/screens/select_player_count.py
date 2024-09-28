from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition.transition import MDSlideTransition

Builder.load_file("client/layouts/select_player_count.kv")

class SelectPlayerCount(MDScreen):
    def on_back_button_clicked(self):
        self.manager.current = 'main_menu'
