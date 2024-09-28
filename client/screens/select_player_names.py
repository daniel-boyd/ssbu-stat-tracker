from kivy.lang import Builder
from kivy.uix.vkeyboard import VKeyboard
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText

Builder.load_file("client/layouts/select_player_names.kv")

class SelectPlayerNames(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.number_of_players = 2
        self.text_fields = []
        # self.vkeyboard = VKeyboard(size_hint=(1, 0.4), pos_hint={"center_x": 0.75, "y": 0.2})
        # self.vkeyboard.bind(on_key_down=self.on_key_down)
        # self.add_widget(self.vkeyboard)

    def on_back_button_clicked(self):
        self.manager.current = 'select_player_count'

    def on_continue_button_clicked(self):
        self.manager.current = 'select_player_count'

    def on_enter(self):
        self.update_text_fields()

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
            # text_field.bind(focus=self.on_focus)
            self.ids.text_field_box.add_widget(text_field)

            self.text_fields.append(text_field)

    # def on_focus(self, instance, value):
    #     if value:
    #         self.vkeyboard.active = True
    #         self.vkeyboard.bind(on_key_down=self.on_key_down)
    #     else:
    #         self.vkeyboard.active = False 

    # def on_key_down(self, keyboard, keycode, text, modifiers):
    #     current_field = [field for field in self.text_fields if field.focus]
    #     if current_field:
    #         current_field[0].text += text
    #     return False
