class GameStats():
    """Klasa odpowiedzialna za monitorowanie danych statystycznych w grze 'Inwazja obcych' """

    def __init__(self, ai_game) -> None:
        """Inicjalizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Uruchomienie gry "inwazja obcych" w stanie nieaktywnym
        self.game_active = False

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmienic się w trakcie gry"""

        self.ships_left = self.settings.ship_limit