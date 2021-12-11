from christmas.base_game import BaseGame


class MyGame(BaseGame):
    def create(self) -> None:
        from christmas.title_view import TitleView
        MyGame.set_current_view(TitleView())