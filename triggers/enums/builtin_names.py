from triggers.bases.enums import strEnum, QuotedEnum


class ResourceType(strEnum):
    ORE = "Ore"
    ORE_AND_GAS = "OreAndGas"
    GAS = "Gas"


class CompareOperator(strEnum):
    AT_LEAST = "AtLeast"
    AT_MOST = "AtMost"
    EXACTLY = "Exactly"


class MathOperator(strEnum):
    ADD = "Add"
    SUBTRACT = "Subtract"
    SET = "SetTo"


class TriggerPlayer(strEnum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"
    P6 = "P6"
    P7 = "P7"
    P8 = "P8"
    P9 = "P9"
    P12 = "P12"
    FOES = "Foes"
    ALLIES = "Allies"
    ALL_PLAYERS = "AllPlayers"
    CURRENT_PLAYER = "CurrentPlayer"
    FORCE1 = "Force1"
    FORCE2 = "Force2"
    FORCE3 = "Force3"
    FORCE4 = "Force4"
    NON_ALLIED_VICTORY = "NonAlliedVictoryPlayers"


class SwitchState(strEnum):
    SET = "Set"
    CLEARED = "Cleared"


class SwitchAction(strEnum):
    SET = "Set"
    CLEAR = "Clear"
    RANDOM = "Random"
    TOGGLE = "Toggle"


class ScoreType(strEnum):
    NOT_IMPLEMENTED_YET = "NI"


class BuiltinUnit(QuotedEnum):
    ANY_UNIT = "AnyUnit"
    MEN = "Men"
    FACTORIES = "Factories"
    BUILDINGS = "Buildings"


class OrderType(strEnum):
    ATTACK = "Attack"
    PATROL = "Patrol"
    MOVE = "Move"


class AllyStatus(strEnum):
    ALLY = "Ally"
    ALLIED_VICTORY = "AlliedVictory"
    ENEMY = "Enemy"
