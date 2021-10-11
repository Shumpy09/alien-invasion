import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """Klasa przeznaczona do zarządzania statkiem kosmicznym"""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""
        super().__init__()
        self.screen = ai_game.screen                            # przypisanie ekranu atrybutowi egzemplarza klasy Ship
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()            # uzyskanie dostępu do atrybutu rect ekranu/ umieszczenie statku w odpowiednim miejscu

        # Wczytywanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')       # wczytanie obrazu statku
        self.rect = self.image.get_rect()                       # uzyskanie dostępu do atrybutu rect powierzchni/ pozwala na zmianę położenia statku

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom        # umieszczenie statku pośrodku, na dole ekranu (okna gry)

        # położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)

        # Opcje wskazujące na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Umieszczenie statku na środku przy dolnej krawędzi ekranu"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch"""
        # Uaktualnienie wartości współrzędnej X statku, a nie jego prostokata
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiektu rect na podstawie wartości self.x
        self.rect.x = self.x

    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)