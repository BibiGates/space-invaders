import pygame
import classes.constants as const
from classes.hord import Hord

class Scene:
    """"""

    def __init__(self, window):
        """"""

        self._window = window
        self._running = True
        self._menu_on_quit = const.QUIT

    def on_execute(self):
        """Retourne l'id du menu cible."""

        clock = pygame.time.Clock()

        while self._running:
            # get events
            for e in pygame.event.get():
                self.on_event(e)

            # update
            self.on_update()

            # display
            self._window.fill((0,0,0))
            self.on_render()
            pygame.display.flip()

            clock.tick(30)

        return self._menu_on_quit
# End of Scene class

class MenuScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)
# End of MenuScene class

class GameScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)

        self._on_menu_quit = const.MAIN_MENU
        self.__hord = Hord()
        # self.__player = Player()

    def on_event(self, event):
        """"""
        if event.type == pygame.QUIT:
            self._running = False

    def on_update(self):
        """"""
        self.__hord.on_update(pygame.time.get_ticks())

    def on_render(self):
        """"""
        self.__hord.on_render(self._window)


# End of GameScene class

class SettingsScene(Scene):
    """"""

    def __init__(self, window):
        """"""

        Scene.__init__(self, window)
# End of SettingsScene class
