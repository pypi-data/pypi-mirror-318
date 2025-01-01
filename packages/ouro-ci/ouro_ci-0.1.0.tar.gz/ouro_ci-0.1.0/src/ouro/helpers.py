import yaml
from enum import Enum


class EnumYAMLDumper(yaml.SafeDumper):
    """Custom YAML dumper that handles reserved keys like 'on'."""

    def represent_dict(self, data):
        # Check for the 'on' key and ensure it is treated as a literal string
        if "on" in data:
            items = [("on", data.pop("on"))] + list(
                data.items()
            )  # Move 'on' to the front
            data = dict(items)
        return super().represent_dict(data)

    def represent_data(self, data):
        # Handle Enums by dumping their `.value`
        if isinstance(data, Enum):
            return self.represent_data(data.value)
        return super().represent_data(data)
