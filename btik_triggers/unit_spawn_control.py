import math
from base import BaseTriggerGenerator
from map_data.locations import Locations
from map_data.switches import Switches
from map_data.units import DeathCounters, Unit
from triggers.action import (
    Actions,
    Comment,
    CreateUnit,
    MoveUnit,
    PreserveTrigger,
    SetDeaths,
    SetResources,
    SetSwitch,
)
from triggers.condition import (
    Accumulate,
    Always,
    Bring,
    Command,
    Conditions,
    Deaths,
    Switch,
)
from triggers.enums.builtin_names import (
    CompareOperator,
    MathOperator,
    ResourceType,
    SwitchAction,
    SwitchState,
    TriggerPlayer,
)
from pydantic import BaseModel

from triggers.trigger import Trigger


class Lane(BaseModel):
    lane_flow: list[Locations] | None = None
    temp_lane: Locations
    weight_start: int | None = None
    weight_end: int | None = None

    def lane_move_trigger(self):
        players = [TriggerPlayer.P8]

        condition_before = [
            Bring(
                player=TriggerPlayer.ALL_PLAYERS,
                compare=CompareOperator.AT_LEAST,
                amount=1,
                unit=Unit.MEN,
                location=Locations.UNIT_SPAWN_AREA,
            )
        ]

        if self.weight_start:
            condition_before.append(
                Deaths(
                    player=TriggerPlayer.P8,
                    compare=CompareOperator.AT_LEAST,
                    amount=self.weight_start,
                    unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
                )
            )

        if self.weight_end:
            condition_before.append(
                Deaths(
                    player=TriggerPlayer.P8,
                    compare=CompareOperator.AT_MOST,
                    amount=self.weight_end - 1,
                    unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
                )
            )

        conditions = Conditions(conditions=condition_before)

        action_before = [
            MoveUnit(
                amount=100,
                unit=Unit.MEN,
                player=TriggerPlayer.ALL_PLAYERS,
                from_location=Locations.UNIT_SPAWN_AREA,
                to_location=self.temp_lane,
            ),
            PreserveTrigger(),
            Comment(text='"[Comment] Unit Move Trigger"'),
        ]

        actions = Actions(actions=action_before)

        return Trigger(players=players, conditions=conditions, actions=actions)


class SpawnCores(BaseModel):
    min_techlevel: int | None = None
    max_techlevel: int | None = None
    cost: int = 500
    units: list[tuple[Unit, int]]
    weight_start: int | None = None
    weight_end: int | None = None
    player: TriggerPlayer = TriggerPlayer.P8

    def spawn_trigger(self):
        players = [self.player]

        condition_before = [
            Accumulate(
                player=TriggerPlayer.P8,
                compare=CompareOperator.AT_LEAST,
                amount=self.cost,
                resource_type=ResourceType.ORE,
            ),
        ]

        if self.min_techlevel:
            condition_before.append(
                Deaths(
                    player=TriggerPlayer.P8,
                    compare=CompareOperator.AT_LEAST,
                    amount=self.min_techlevel,
                    unit=DeathCounters.ENEMY_TECH_LEVEL,
                )
            )

        if self.max_techlevel:
            condition_before.append(
                Deaths(
                    player=TriggerPlayer.P8,
                    compare=CompareOperator.AT_MOST,
                    amount=self.max_techlevel - 1,
                    unit=DeathCounters.ENEMY_TECH_LEVEL,
                )
            )

        if self.weight_start:
            condition_before.append(
                Deaths(
                    player=TriggerPlayer.P8,
                    compare=CompareOperator.AT_LEAST,
                    amount=self.weight_start,
                    unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
                )
            )

        if self.weight_end:
            condition_before.append(
                Deaths(
                    player=TriggerPlayer.P8,
                    compare=CompareOperator.AT_MOST,
                    amount=self.weight_end - 1,
                    unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
                )
            )

        conditions = Conditions(conditions=condition_before)

        action_before = [
            SetResources(
                player=TriggerPlayer.P8,
                math=MathOperator.SUBTRACT,
                amount=self.cost,
                resource_type=ResourceType.ORE,
            ),
            PreserveTrigger(),
            Comment(text='"[Comment] Unit Spawn Trigger"'),
        ]

        for unit in self.units:
            action_before.append(
                CreateUnit(
                    amount=unit[1],
                    unit=unit[0],
                    location=Locations.UNIT_SPAWN_AREA,
                    player=self.player,
                )
            )

        actions = Actions(actions=action_before)

        return Trigger(players=players, conditions=conditions, actions=actions)


class UnitSpawnGenerator(BaseTriggerGenerator):
    OUTPUT_FILE = "spawn_triggers.txt"

    GROUND_CORES = [
        SpawnCores(
            units=[
                (Unit.JIM_RAYNOR_MARINE, 12),
                (Unit.SARAH_KERRIGAN_GHOST, 12),
                (Unit.HUNTER_KILLER_HYDRALISK, 12),
            ],
            weight_end=64,
        )
    ]

    ARMORED_CORES = [
        SpawnCores(
            units=[(Unit.HUNTER_KILLER_HYDRALISK, 18)], weight_start=64, weight_end=128
        )
    ]

    STROKER_CORES = [
        SpawnCores(units=[(Unit.TERRAN_WRAITH, 24)], weight_start=128, weight_end=192)
    ]

    MEATGRINDER_CORES = [
        SpawnCores(
            units=[(Unit.NORAD_II_BATTLECRUISER, 12)],
            weight_start=192,
        )
    ]

    ALL_CORES = [GROUND_CORES, ARMORED_CORES, STROKER_CORES, MEATGRINDER_CORES]

    @classmethod
    def generate_triggers(cls):
        cls.clear_output()

        randomizer = cls.move_spawn_randomizer()
        for trigger in randomizer:
            t = trigger.get_trigger()
            cls.write_output(t)

        randomizer = cls.spawn_randomizer()
        for trigger in randomizer:
            t = trigger.get_trigger()
            cls.write_output(t)

        triggers = cls.spawn_triggers()
        for trigger in triggers:
            t = trigger.get_trigger()
            cls.write_output(t)

        triggers = cls.lane_based_move_trigger()
        for trigger in triggers:
            t = trigger.get_trigger()
            cls.write_output(t)

    @classmethod
    def lane_based_move_trigger(cls):
        temp_lanes = [
            Lane(temp_lane=Locations.JUNGGANGJIN, weight_end=64),
            Lane(temp_lane=Locations.CHAOYANG, weight_start=64, weight_end=128),
            Lane(temp_lane=Locations.CHEONGJIN, weight_start=128, weight_end=192),
            Lane(temp_lane=Locations.JILIN, weight_start=192),
        ]

        triggers = []
        for lane in temp_lanes:
            triggers.append(lane.lane_move_trigger())
        return triggers

    @classmethod
    def spawn_triggers(cls) -> list[Trigger]:
        all_cores = [
            cls.GROUND_CORES,
            cls.ARMORED_CORES,
            cls.STROKER_CORES,
            cls.MEATGRINDER_CORES,
        ]

        triggers = []

        for cores in all_cores:
            for core in cores:
                triggers.append(core.spawn_trigger())

        return triggers

    @classmethod
    def move_spawn_randomizer(cls):
        randomized_switches = [
            Switches.SPAWN_LOCATION_RANDOMIZER_1,
            Switches.SPAWN_LOCATION_RANDOMIZER_2,
            Switches.SPAWN_LOCATION_RANDOMIZER_3,
            Switches.SPAWN_LOCATION_RANDOMIZER_4,
            Switches.SPAWN_LOCATION_RANDOMIZER_5,
            Switches.SPAWN_LOCATION_RANDOMIZER_6,
            Switches.SPAWN_LOCATION_RANDOMIZER_7,
            Switches.SPAWN_LOCATION_RANDOMIZER_8,
        ]

        set_randomizers = []
        for switch in randomized_switches:
            set_randomizers.append(SetSwitch(switch=switch, state=SwitchAction.RANDOM))

        players = [TriggerPlayer.P8]

        conditions = Conditions(conditions=[Always()])

        actions = set_randomizers

        actions.append(PreserveTrigger())
        actions.append(
            SetDeaths(
                player=TriggerPlayer.P8,
                math=MathOperator.SET,
                amount=0,
                unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
            )
        )
        actions.append(Comment(text='"[Comment] Randomize Spawn moves"'))

        triggers = [
            Trigger(
                players=players, conditions=conditions, actions=Actions(actions=actions)
            )
        ]

        i = 0
        for switch in randomized_switches:
            conditions = [Switch(switch=switch, state=SwitchState.SET)]
            actions = [
                SetDeaths(
                    player=TriggerPlayer.P8,
                    math=MathOperator.ADD,
                    amount=math.pow(2, i),
                    unit=DeathCounters.SPAWN_LOCATION_RANDOM_VALUE,
                ),
                PreserveTrigger(),
                Comment(text='"[Comment] Randomized Switch -> DC"'),
            ]

            triggers.append(
                Trigger(
                    players=players,
                    conditions=Conditions(conditions=conditions),
                    actions=Actions(actions=actions),
                )
            )
            i = i + 1

        return triggers

    @classmethod
    def spawn_randomizer(cls):
        randomized_switches = [
            Switches.SPAWN_RANDOMIZER_1,
            Switches.SPAWN_RANDOMIZER_2,
            Switches.SPAWN_RANDOMIZER_3,
            Switches.SPAWN_RANDOMIZER_4,
            Switches.SPAWN_RANDOMIZER_5,
            Switches.SPAWN_RANDOMIZER_6,
            Switches.SPAWN_RANDOMIZER_7,
            Switches.SPAWN_RANDOMIZER_8,
        ]

        set_randomizers = []
        for switch in randomized_switches:
            set_randomizers.append(SetSwitch(switch=switch, state=SwitchAction.RANDOM))

        players = [TriggerPlayer.P8]

        conditions = Conditions(conditions=[Always()])

        actions = set_randomizers

        actions.append(PreserveTrigger())
        actions.append(
            SetDeaths(
                player=TriggerPlayer.P8,
                math=MathOperator.SET,
                amount=0,
                unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
            )
        )
        actions.append(Comment(text='"[Comment] Randomize before spawn"'))

        triggers = [
            Trigger(
                players=players, conditions=conditions, actions=Actions(actions=actions)
            )
        ]
        i = 0
        for switch in randomized_switches:
            conditions = [Switch(switch=switch, state=SwitchState.SET)]
            actions = [
                SetDeaths(
                    player=TriggerPlayer.P8,
                    math=MathOperator.ADD,
                    amount=math.pow(2, i),
                    unit=DeathCounters.SPAWN_UNIT_RANDOM_VALUE,
                ),
                PreserveTrigger(),
                Comment(text='"[Comment] Randomized Switch -> DC"'),
            ]

            triggers.append(
                Trigger(
                    players=players,
                    conditions=Conditions(conditions=conditions),
                    actions=Actions(actions=actions),
                )
            )
            i = i + 1

        return triggers
