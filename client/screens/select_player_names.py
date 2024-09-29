from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.vkeyboard import VKeyboard
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

Builder.load_file("client/layouts/select_player_names.kv")

class SelectPlayerNames(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Config.set("kivy", "keyboard_mode", "dock")
        self.number_of_players = 2
        self.text_fields = []
        self.caps_lock = False

    def on_back_button_clicked(self):
        self.manager.current = 'select_player_count'

    def on_continue_button_clicked(self):
        # Don't allow empty names
        for text_field in self.text_fields:
            if text_field.text == "":
                return
        self.manager.current = 'select_gamemode'
                

    def on_enter(self):
        self.update_text_fields()

    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]

        current_focused = None
        for text_field in self.text_fields:
            if text_field.focus:
                current_focused = text_field
                break

        if current_focused is not None:
            if keycode == "backspace":
                current_focused.text = current_focused.text[:-1]
                return
            elif keycode == "capslock" or keycode == "CAPSLOCK":
                self.caps_lock = not self.caps_lock
                return
            elif keycode == "enter":
                return
            elif keycode == "spacebar":
                return
            elif keycode == "shift":
                return
            
            if self.caps_lock:
                keycode = keycode.upper()

            current_focused.text += keycode

    def update_text_fields(self):
        self.ids.player_labels_box.clear_widgets()
        self.ids.text_field_box.clear_widgets()

        for index in range(self.number_of_players):
            player_label = MDLabel(
                text=f"Player {index + 1}",
                size_hint_y=None,
                height="30dp",
                halign="center"
            )
            self.ids.player_labels_box.add_widget(player_label)

            text_field = MDTextField(
                mode="outlined",
                size_hint_y=None,
                height="240dp",
                hint_text="Enter Name",
            )
            self.ids.text_field_box.add_widget(text_field)

            self.text_fields.append(text_field)
