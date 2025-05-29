from .LogToConsole import LogToConsole

class RF_LogFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("FLOAT", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (FLOAT)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(prefix, value)
        return (value,)
