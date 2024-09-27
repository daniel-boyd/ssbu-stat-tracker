from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("client/layouts/character_select.kv")

class MainMenu(Screen):
    pass

class Settings(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass
