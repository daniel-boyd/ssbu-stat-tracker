from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDExtendedFabButton

Builder.load_file("client/layouts/set_player_stats.kv")

class StocksMDExtendedFabButton(MDExtendedFabButton):
    stocks = ""

class SetPlayerStats(MDScreen):
    pass