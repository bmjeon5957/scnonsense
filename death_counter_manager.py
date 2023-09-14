from conf import config
from enums import DeathCounterNames


class DeathCounterManagerGenerator:
    OUTPUT_FILE = "death_counter_managers.txt"

    @classmethod
    def generate_triggers(cls):
        for items in DeathCounterNames:
            pass
