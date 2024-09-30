from kivy.uix.screenmanager import Screen
from kivymd.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

Builder.load_file("client/layouts/select_character.kv")

class CharacterButton(Button):
    character_name = StringProperty('')

class SelectCharacter(Screen):
    pass
