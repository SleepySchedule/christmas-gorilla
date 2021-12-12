from typing import List, Optional
from christmas.sprites import Snowman


class Team:
    def __init__(self, name: str, players: List[Snowman]) -> None:
        self._name = name
        self._players = players
    
    
    def get_name(self) -> str:
        """Gets the team name."""
        return self._name
    

    def get_players(self) -> List[Snowman]:
        """Gets the list of players on the team."""
        return self._players

    
    def add_player(self, player: Snowman) -> None:
        """Adds player to the team.
        
        Args:
            player: The new snowman to add to the team.
        """
        
        self._players.append(player)


    def remove_player(self, player: Snowman) -> None:
        """Removes player from the team.

        Args:
            player: The snowman to be removed from the team.
        """

        self._players.remove(player)
