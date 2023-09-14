from importlib.resources import Resource
import math
from base import BaseTriggerGenerator
from map_data.units import DeathCounters, Unit
from triggers.action import (
    Actions,
    Comment,
    GiveUnits,
    MoveLocation,
    PreserveTrigger,
    SetCountdownTimer,
    SetDeaths,
    SetResources,
)
from triggers.condition import Bring, Conditions, CountdownTimer, Deaths
from triggers.enums.builtin_names import (
    CompareOperator,
    MathOperator,
    ResourceType,
    TriggerPlayer,
)
from map_data.locations import Locations
from triggers.trigger import Trigger


class TaxTriggerGenerator(BaseTriggerGenerator):
    OUTPUT_FILE = "tax_triggers.txt"

    TAX_TIME = 30
    COUNTERDOWN_START = 40

    @classmethod
    def generate_triggers(cls):
        cls.clear_output()
        city_owner: list[Trigger] = cls.determine_city_owner()

        countdown_triggers = cls.countdown_timer()

        for trigger in countdown_triggers:
            t = trigger.get_trigger()
            cls.write_output(t)

        # 5 sets of city owner trigger
        for i in range(0, 5):
            # for each trigger
            for trigger in city_owner:
                t = trigger.get_trigger()
                cls.write_output(t)

        give_beacon = cls.tax_per_beacon().get_trigger()
        cls.write_output(give_beacon)

        convert_trigger = cls.convert_dc_to_minerals()

        for trigger in convert_trigger:
            t = trigger.get_trigger()
            cls.write_output(t)

    @classmethod
    def countdown_timer(cls) -> list[Trigger]:
        players = [TriggerPlayer.P5]

        conditions = Conditions(
            conditions=[CountdownTimer(compare=CompareOperator.EXACTLY, amount=0)]
        )

        actions = Actions(
            actions=[
                SetCountdownTimer(math=MathOperator.SET, amount=40),
                PreserveTrigger(),
                Comment(text='"Countdown Timer"'),
            ]
        )

        return [Trigger(players=players, conditions=conditions, actions=actions)]

    @classmethod
    def determine_city_owner(cls) -> list[Trigger]:
        # 1. Move Location to each beacon

        triggersets = []

        players = [TriggerPlayer.FORCE1, TriggerPlayer.FORCE3]
        conditions = Conditions(
            conditions=[
                Bring(
                    player=TriggerPlayer.P9,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    location=Locations.ANYWHERE,
                ),
                CountdownTimer(
                    compare=CompareOperator.AT_LEAST, amount=cls.TAX_TIME + 1
                ),
            ]
        )

        actions = Actions(
            actions=[
                MoveLocation(
                    location=Locations.CITY_PROCESSOR,
                    unit=Unit.TERRAN_BEACON,
                    player=TriggerPlayer.P9,
                    in_location=Locations.ANYWHERE,
                ),
                PreserveTrigger(),
                Comment(text='"Tax Trigger Move Location"'),
            ]
        )

        triggersets.append(
            Trigger(players=players, conditions=conditions, actions=actions)
        )

        # 1. Determine Owner of the beacon. Is it owned by enemy?
        players = [TriggerPlayer.FORCE2]
        conditions = Conditions(
            conditions=[
                Bring(
                    player=TriggerPlayer.CURRENT_PLAYER,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.P9,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    location=Locations.CITY_PROCESSOR,
                ),
                CountdownTimer(
                    compare=CompareOperator.AT_LEAST, amount=cls.TAX_TIME + 1
                ),
            ]
        )

        actions = Actions(
            actions=[
                GiveUnits(
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    from_player=TriggerPlayer.P9,
                    location=Locations.CITY_PROCESSOR,
                    to_player=TriggerPlayer.P8,
                ),
                PreserveTrigger(),
                Comment(text='"Tax Trigger Owned by CPU"'),
            ]
        )

        triggersets.append(
            Trigger(players=players, conditions=conditions, actions=actions)
        )

        # 2. Determine Owner of the beacon. Is it owned by player?
        players = [TriggerPlayer.FORCE1]
        conditions = Conditions(
            conditions=[
                Bring(
                    player=TriggerPlayer.CURRENT_PLAYER,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.P9,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.FORCE2,
                    compare=CompareOperator.EXACTLY,
                    amount=0,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.FORCE3,
                    compare=CompareOperator.EXACTLY,
                    amount=0,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                CountdownTimer(
                    compare=CompareOperator.AT_LEAST, amount=cls.TAX_TIME + 1
                ),
            ]
        )

        actions = Actions(
            actions=[
                GiveUnits(
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    from_player=TriggerPlayer.P9,
                    location=Locations.CITY_PROCESSOR,
                    to_player=TriggerPlayer.CURRENT_PLAYER,
                ),
                PreserveTrigger(),
                Comment(text='"Tax Trigger Owned by Player"'),
            ]
        )

        triggersets.append(
            Trigger(players=players, conditions=conditions, actions=actions)
        )

        # 3. Determine Owner of the beacon. Is it owned by Ally Computer
        players = [TriggerPlayer.FORCE3]
        conditions = Conditions(
            conditions=[
                Bring(
                    player=TriggerPlayer.CURRENT_PLAYER,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.P9,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.FORCE2,
                    compare=CompareOperator.EXACTLY,
                    amount=0,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                CountdownTimer(
                    compare=CompareOperator.AT_LEAST, amount=cls.TAX_TIME + 1
                ),
            ]
        )

        actions = Actions(
            actions=[
                GiveUnits(
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    from_player=TriggerPlayer.P9,
                    location=Locations.CITY_PROCESSOR,
                    to_player=TriggerPlayer.CURRENT_PLAYER,
                ),
                PreserveTrigger(),
                Comment(text='"Tax Trigger Owned by Allied Computer"'),
            ]
        )

        triggersets.append(
            Trigger(players=players, conditions=conditions, actions=actions)
        )

        # 4. Determine Owner of the beacon. Just owned by nobody(computer?)
        players = [TriggerPlayer.FORCE3]
        conditions = Conditions(
            conditions=[
                Bring(
                    player=TriggerPlayer.P9,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    location=Locations.ANYWHERE,
                ),
                Bring(
                    player=TriggerPlayer.FORCE1,
                    compare=CompareOperator.EXACTLY,
                    amount=0,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                Bring(
                    player=TriggerPlayer.FORCE3,
                    compare=CompareOperator.EXACTLY,
                    amount=0,
                    unit=Unit.BUILDINGS,
                    location=Locations.CITY_PROCESSOR,
                ),
                CountdownTimer(
                    compare=CompareOperator.AT_LEAST, amount=cls.TAX_TIME + 1
                ),
            ]
        )

        actions = Actions(
            actions=[
                GiveUnits(
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    from_player=TriggerPlayer.P9,
                    location=Locations.CITY_PROCESSOR,
                    to_player=TriggerPlayer.P8,
                ),
                PreserveTrigger(),
                Comment(text='"Tax Trigger Owned by Nobody"'),
            ]
        )

        triggersets.append(
            Trigger(players=players, conditions=conditions, actions=actions)
        )

        return triggersets

    @classmethod
    def tax_per_beacon(cls):
        players = [TriggerPlayer.FORCE1, TriggerPlayer.FORCE2, TriggerPlayer.FORCE3]

        conditions = Conditions(
            conditions=[
                Bring(
                    player=TriggerPlayer.CURRENT_PLAYER,
                    compare=CompareOperator.AT_LEAST,
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    location=Locations.ANYWHERE,
                ),
                CountdownTimer(compare=CompareOperator.AT_MOST, amount=cls.TAX_TIME),
            ]
        )

        actions = Actions(
            actions=[
                GiveUnits(
                    amount=1,
                    unit=Unit.TERRAN_BEACON,
                    from_player=TriggerPlayer.CURRENT_PLAYER,
                    location=Locations.ANYWHERE,
                    to_player=TriggerPlayer.P9,
                ),
                SetDeaths(
                    player=TriggerPlayer.CURRENT_PLAYER,
                    math=MathOperator.ADD,
                    amount=500,
                    unit=DeathCounters.TAX_MINERAL_DC,
                ),
                PreserveTrigger(),
                Comment(text='"Give Beacon to Neutral"'),
            ]
        )

        return Trigger(players=players, conditions=conditions, actions=actions)

    @classmethod
    def convert_dc_to_minerals(cls) -> list[Trigger]:
        players = [TriggerPlayer.FORCE1, TriggerPlayer.FORCE2]
        convert_triggers = []
        for i in range(16, -1, -1):
            conditions = Conditions(
                conditions=[
                    Deaths(
                        player=TriggerPlayer.CURRENT_PLAYER,
                        compare=CompareOperator.AT_LEAST,
                        amount=math.pow(2, i),
                        unit=DeathCounters.TAX_MINERAL_DC,
                    )
                ]
            )

            actions = Actions(
                actions=[
                    SetDeaths(
                        player=TriggerPlayer.CURRENT_PLAYER,
                        math=MathOperator.SUBTRACT,
                        amount=math.pow(2, i),
                        unit=DeathCounters.TAX_MINERAL_DC,
                    ),
                    SetResources(
                        player=TriggerPlayer.CURRENT_PLAYER,
                        math=MathOperator.ADD,
                        amount=math.pow(2, i),
                        resource_type=ResourceType.ORE,
                    ),
                    PreserveTrigger(),
                    Comment(text='"Binary Tax Conversion"'),
                ]
            )

            convert_triggers.append(
                Trigger(players=players, conditions=conditions, actions=actions)
            )

        return convert_triggers
