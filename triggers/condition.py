from triggers.common import BaseNode
from triggers.enums.builtin_names import (
    CompareOperator,
    ScoreType,
    SwitchState,
    TriggerPlayer,
    ResourceType,
)
from map_data.locations import Locations
from map_data.switches import Switches

from map_data.units import Unit


class BaseCondition(BaseNode):
    pass


class Accumulate(BaseCondition):
    player: TriggerPlayer
    compare: CompareOperator
    amount: int
    resource_type: ResourceType


class Always(BaseCondition):
    pass


class Bring(BaseCondition):
    player: TriggerPlayer
    compare: CompareOperator
    amount: int
    unit: Unit | str
    location: Locations


class Command(BaseCondition):
    player: TriggerPlayer
    compare: CompareOperator
    amount: int
    unit: Unit | str


class CommandMost(BaseCondition):
    unit: Unit | str


class CommandMostAt(BaseCondition):
    unit: Unit | str
    location: Locations


class CommandLeast(BaseCondition):
    unit: Unit | str


class CommandLeastAt(BaseCondition):
    unit: Unit | str
    location: Locations


class CountdownTimer(BaseCondition):
    compare: CompareOperator
    amount: int


class Deaths(BaseCondition):
    player: TriggerPlayer
    compare: CompareOperator
    amount: int
    unit: Unit


class ElapsedTime(BaseCondition):
    compare: CompareOperator
    amount: int


class HighestScore(BaseCondition):
    score_type: ScoreType


class Kills(BaseCondition):
    player: TriggerPlayer
    compare: CompareOperator
    amount: int
    unit: Unit | str


class LeastKills(BaseCondition):
    unit_name: Unit


class LeastResources(BaseCondition):
    resource_type: ResourceType


class LowestScore(BaseCondition):
    score_type: ScoreType


class MostKills(BaseCondition):
    unit_name: Unit


class MostResources(BaseCondition):
    resource_type: ResourceType


class Never(BaseCondition):
    pass


class Opponents(BaseCondition):
    player: TriggerPlayer
    compare: CompareOperator
    amount: int


class Score(BaseCondition):
    player: TriggerPlayer
    score_type: ScoreType
    compare: CompareOperator
    amount: int


class Switch(BaseCondition):
    switch: Switches
    state: SwitchState


class Conditions:
    def __init__(self, conditions: list[BaseCondition]):
        self.conditions = conditions

    def get_triggers(self):
        _return = "\tconditions = {\n"

        for condition in self.conditions:
            _return += "\t\t" + condition.get_trigger() + "\n"

        _return += "\t}"

        return _return

    def get_conditions(self):
        return self.conditions
