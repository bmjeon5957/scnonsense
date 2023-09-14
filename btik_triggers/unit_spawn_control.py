from base import BaseTriggerGenerator
from map_data.switches import Switches
from triggers.action import SetSwitch
from triggers.enums.builtin_names import SwitchAction


class UnitSpawnGenerator(BaseTriggerGenerator):
    OUTPUT_FILE = "spawn_triggers.txt"

    @classmethod
    def generate_triggers(cls):
        pass

    @classmethod
    def randomizer(cls):
        randomized_switches = [
            Switches.SWITCH_255,
            Switches.SWITCH_254,
            Switches.SWITCH_253,
            Switches.SWITCH_252,
            Switches.SWITCH_251,
            Switches.SWITCH_250,
            Switches.SWITCH_249,
            Switches.SWITCH_248,
        ]

        SetSwitch(switch=switch, state=SwitchAction.RANDOM)
