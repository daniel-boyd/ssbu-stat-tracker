from kivymd.uix.screenmanager import ScreenManager
from .screens.select_player_character import SelectPlayerCharacter

# Extends the ScreenManager to allow for reinitializing screens, loading varying .kv files when dynamic layouts are needed
class SsbuScreenManager(ScreenManager):
    def reinitialize_screen(self, screen_class, screen_name, kv_file):
        """Reinitialize the specified screen by removing it and adding a new instance."""
        new_screen = screen_class(kv_file=kv_file, name=screen_name)
        self.remove_widget(self.get_screen(screen_name))
        self.add_widget(new_screen)
        self.current = new_screen.name