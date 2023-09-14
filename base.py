from conf import config
from abc import abstractmethod


class BaseTriggerGenerator:
    @classmethod
    @property
    @abstractmethod
    def OUTPUT_FILE(cls):
        raise NotImplementedError

    @classmethod
    def clear_all_output_file(cls):
        with open(config.output_dir / "_all_triggers", "w") as f:
            f.close()

    @classmethod
    def clear_output(cls):
        with open(config.output_dir / cls.OUTPUT_FILE, "w") as f:
            f.close()

    @classmethod
    def write_output(cls, content: str):
        with open(config.output_dir / cls.OUTPUT_FILE, "a") as f:
            f.write(content)

        with open(config.output_dir / "_all_triggers", "a") as f:
            f.write(content)
