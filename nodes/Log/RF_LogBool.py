from .LogToConsole import LogToConsole

class RF_LogBool:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("BOOL", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (BOOL)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("BOOL",)
    RETURN_NAMES = ("BOOL",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(value, prefix)
        return (value,)
