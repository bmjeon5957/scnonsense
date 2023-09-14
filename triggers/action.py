from map_data.locations import Locations
from map_data.switches import Switches
from map_data.units import DeathCounters, Unit
from triggers.bases.enums import QuotedStr
from triggers.common import BaseNode
from triggers.enums.builtin_names import (
    MathOperator,
    OrderType,
    ResourceType,
    ScoreType,
    SwitchAction,
    TriggerPlayer,
)
from pydantic import validator


class BaseAction(BaseNode):
    pass


class CenterView(BaseAction):
    location: Locations


class CreateUnit(BaseAction):
    amount: int
    unit: Unit
    location: Locations
    player: TriggerPlayer


class CreateUnitWithProperties(BaseAction):
    amount: int
    unit: Unit
    location: Locations
    player: TriggerPlayer
    property: object


class Defeat(BaseAction):
    pass


class Draw(BaseAction):
    pass


class GiveUnits(BaseAction):
    amount: int
    unit: Unit
    from_player: TriggerPlayer
    location: Locations
    to_player: TriggerPlayer


class KillUnit(BaseAction):
    unit: Unit
    player: TriggerPlayer


class KillUnitAt(BaseAction):
    amount: int
    unit: Unit
    location: Locations
    player: TriggerPlayer


class LeaderBoardScore(BaseAction):
    score_type: ScoreType
    label: str


class MinimapPing(BaseAction):
    location: Locations


class ModifyUnitEnergy(BaseAction):
    amount: int
    unit: Unit
    player: TriggerPlayer
    location: Locations
    percent: int


class ModifyUnitHitPoints(BaseAction):
    amount: int
    unit: Unit
    player: TriggerPlayer
    location: Locations
    percent: int


class ModifyUnitHangarCount(BaseAction):
    amount: int
    unit: Unit
    player: TriggerPlayer
    location: Locations
    percent: int


class ModifyUnitResourceAmount(BaseAction):
    amount: int
    player: TriggerPlayer
    location: Locations
    percent: int


class MoveUnit(BaseAction):
    amount: int
    unit: Unit
    player: TriggerPlayer
    from_location: Locations
    to_location: Locations


class MoveLocation(BaseAction):
    location: Locations
    unit: Unit
    player: TriggerPlayer
    in_location: Locations


class Comment(BaseAction):
    text: str


class Order(BaseAction):
    unit: Unit
    player: TriggerPlayer
    from_location: Locations
    order_type: OrderType
    to_location: Locations


class RemoveUnit(BaseAction):
    unit: Unit
    player: TriggerPlayer


class RemoveUnitAt(BaseAction):
    amount: int
    unit: Unit
    location: Locations
    player: TriggerPlayer


class PreserveTrigger(BaseAction):
    pass


class SetResources(BaseAction):
    player: TriggerPlayer
    math: MathOperator
    amount: int
    resource_type: ResourceType


class SetSwitch(BaseAction):
    switch: Switches
    state: SwitchAction


class SetCountdownTimer(BaseAction):
    math: MathOperator
    amount: int


class SetDeaths(BaseAction):
    player: TriggerPlayer
    math: MathOperator
    amount: int
    unit: DeathCounters


class Victory(BaseAction):
    pass


class Actions:
    def __init__(self, actions: list[BaseAction]):
        self.actions = actions

    def get_triggers(self):
        _return = "\tactions = {\n"

        for condition in self.actions:
            _return += "\t\t" + condition.get_trigger() + "\n"

        _return += "\t}"

        return _return

    def get_actions(self):
        return self.actions
