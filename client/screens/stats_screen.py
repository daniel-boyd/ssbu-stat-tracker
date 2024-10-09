from .. import shared
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDExtendedFabButton

Builder.load_file("client/layouts/stats_screen.kv")

class StatsScreen(MDScreen):

    def on_pre_enter(self):
        player_1_stats = self.ids.player_1_stats
        player_2_stats = self.ids.player_2_stats
        player_1_stats.text = shared.get_current_match_value_from_key("players")[1]
        player_2_stats.text = shared.get_current_match_value_from_key("players")[2]
        player_1_name = shared.get_current_match_value_from_key("players")[1]
        player_2_name = shared.get_current_match_value_from_key("players")[2]
            # Set player names?
        player_1_stats.txt = player_1_name
        player_2_stats.txt = player_2_name

        player_stocks = shared.get_current_match_value_from_key("player_stocks")
        player_1_stocks_taken = str(player_stocks.get(player_1_name,0))
        player_2_stocks_taken = str(player_stocks.get(player_2_name,0))
        self.ids.player_1_stocks_taken.text = player_1_stocks_taken
        self.ids.player_2_stocks_taken.text = player_2_stocks_taken
            # Player Deaths start
        player_deaths = shared.get_current_match_value_from_key("player_deaths")
        player_1_deaths = str(player_deaths.get(player_1_name,0))
        player_2_deaths = str(player_deaths.get(player_2_name,0))
        self.ids.player_1_deaths.text = player_1_deaths
        self.ids.player_2_deaths.text = player_2_deaths
            #Clutches 1v1 start
        player_1v1_clutches = shared.get_current_match_value_from_key("player_1v1_clutches")
        player_1_1v1_clutches = str(player_1v1_clutches.get(player_1_name,0))
        player_2_1v1_clutches = str(player_1v1_clutches.get(player_2_name,0))
        self.ids.player_1_1v1_clutches.text = player_1_1v1_clutches
        self.ids.player_2_1v1_clutches.text = player_2_1v1_clutches
            #Clutches 1v2 start
        player_1v2_clutches = shared.get_current_match_value_from_key("player_1v2_clutches")
        player_1_1v2_clutches = str(player_1v2_clutches.get(player_1_name,0))
        player_2_1v2_clutches = str(player_1v2_clutches.get(player_2_name,0))
        self.ids.player_1_1v2_clutches.text = player_1_1v1_clutches
        self.ids.player_2_1v2_clutches.text = player_2_1v1_clutches

pass