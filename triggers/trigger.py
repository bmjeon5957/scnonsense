from triggers.condition import Conditions
from triggers.action import Actions
from triggers.enums.builtin_names import TriggerPlayer


class Trigger:
    def __init__(
        self, players: list[TriggerPlayer], conditions: Conditions, actions: Actions
    ):
        self.players = players
        self.actions = actions
        self.conditions = conditions

    def get_players(self):
        _return = "\tplayers = {"

        player_length = len(self.players)
        for i in range(player_length):
            _return += self.players[i].value
            if i < player_length - 1:
                _return += ","

        _return += "}"

        return _return

    def get_trigger(self):
        _return = "Trigger {\n"
        _return += self.get_players() + ",\n"
        _return += self.conditions.get_triggers() + ",\n"
        _return += self.actions.get_triggers() + "\n"

        _return += "}\n"

        return _return

    def get_conditions(self):
        return self.conditions
