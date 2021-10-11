class GameStats():
    """Klasa odpowiedzialna za monitorowanie danych statystycznych w grze 'Inwazja obcych' """

    def __init__(self, ai_game) -> None:
        """Inicjalizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Uruchomienie gry "inwazja obcych" w stanie nieaktywnym
        self.game_active = False
       
        # Najlepszy wynik nigdy nie powinien zostać wyzerowany
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmienic się w trakcie gry"""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1