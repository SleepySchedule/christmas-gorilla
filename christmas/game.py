from christmas.base_game import BaseGame


class Game(BaseGame):
    def create(self) -> None:
        from christmas.title_view import TitleView
        Game.set_current_view(TitleView())