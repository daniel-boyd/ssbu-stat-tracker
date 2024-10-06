from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

Builder.load_file("client/layouts/select_bot.kv")

class BotButton(Button):
    character_name = StringProperty('')

class SelectBot(Screen):
    pass
