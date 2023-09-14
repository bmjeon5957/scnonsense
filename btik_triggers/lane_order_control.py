from base import BaseTriggerGenerator
from map_data.locations import LaneLocations
from map_data.units import DeathCounters, Unit
from triggers.action import Actions, Comment, Order, PreserveTrigger
from triggers.condition import Bring, Conditions, Deaths
from triggers.enums.builtin_names import CompareOperator, OrderType, TriggerPlayer
from triggers.trigger import Trigger


class LaneOrderControlGenerator(BaseTriggerGenerator):
    OUTPUT_FILE = "lane_triggers.txt"

    _LANES = [
        [
            LaneLocations.ANSHAN,
            LaneLocations.SINUIJU,
            LaneLocations.PYONGYANG,
            LaneLocations.HAEJU,
            LaneLocations.SEOUL_WEST,
            LaneLocations.AHSAN,
            LaneLocations.GWANGJU,
            LaneLocations.CHANGWON,
            LaneLocations.BUSAN,
        ],
        [
            LaneLocations.JUNGGANGJIN,
            LaneLocations.GANGGYE,
            LaneLocations.GAECHEON,
            LaneLocations.GAESUNG,
            LaneLocations.DONGDUCHEON,
            LaneLocations.SEOUL_EAST,
            LaneLocations.JINAHN,
            LaneLocations.BUSAN,
            LaneLocations.BETWEEN_BUSAN_ULSAN,
        ],
        [
            LaneLocations.JILIN,
            LaneLocations.GAEMA,
            LaneLocations.HAMHUNG,
            LaneLocations.GAESUNG_TOP,
            LaneLocations.WONJU,
            LaneLocations.DAEGU,
            LaneLocations.BETWEEN_BUSAN_ULSAN,
        ],
        [
            LaneLocations.CHEONGJIN,
            LaneLocations.HAESAN,
            LaneLocations.SINPO,
            LaneLocations.WONSAN,
            LaneLocations.GANGWON,
            LaneLocations.GYEONGJU,
            LaneLocations.ULSAN,
            LaneLocations.BETWEEN_BUSAN_ULSAN,
        ],
        [LaneLocations.SHENYANG, LaneLocations.XIHU, LaneLocations.GANGGYE],
        [LaneLocations.CHAOYANG, LaneLocations.ANSHAN],
        [LaneLocations.DALIAN, LaneLocations.SINUIJU],
    ]

    @classmethod
    def generate_triggers(cls):
        # Clear File
        cls.clear_output()

        for lane in cls._LANES:
            for i in range(len(lane) - 1):
                from_location = lane[i]
                to_location = lane[i + 1]
                players = [TriggerPlayer.FORCE2]
                conditions = Conditions(
                    conditions=[
                        Bring(
                            player=TriggerPlayer.FORCE2,
                            compare=CompareOperator.AT_LEAST,
                            amount=12,
                            unit=Unit.MEN,
                            location=from_location,
                        ),
                        Deaths(
                            player=TriggerPlayer.P5,
                            compare=CompareOperator.EXACTLY,
                            amount=0,
                            unit=DeathCounters.EVERY_12DC,
                        ),
                    ]
                )

                actions = Actions(
                    actions=[
                        Order(
                            unit=Unit.MEN,
                            player=TriggerPlayer.FORCE2,
                            from_location=from_location,
                            order_type=OrderType.ATTACK,
                            to_location=to_location,
                        ),
                        PreserveTrigger(),
                        Comment(text='"[Comment] Computer Lane Order Control"'),
                    ]
                )

                trigger = Trigger(
                    players=players, conditions=conditions, actions=actions
                ).get_trigger()

                cls.write_output(trigger)
