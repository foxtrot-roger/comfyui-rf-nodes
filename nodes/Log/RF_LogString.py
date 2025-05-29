from .LogToConsole import LogToConsole

class RF_LogString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("STRING", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (STRING)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(prefix, value)
        return (value,)
