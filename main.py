from base import BaseTriggerGenerator
from btik_triggers.hyper_triggers import HyperTriggerGenerator
from btik_triggers.lane_order_control import LaneOrderControlGenerator
from btik_triggers.tax_triggers import TaxTriggerGenerator


BaseTriggerGenerator.clear_all_output_file()

TaxTriggerGenerator.generate_triggers()
LaneOrderControlGenerator.generate_triggers()
HyperTriggerGenerator.generate_triggers()
