from .LogToConsole import LogToConsole

class RF_LogNumber:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("NUMBER", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (NUMBER)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("NUMBER",)
    RETURN_NAMES = ("NUMBER",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(prefix, value)
        return (value,)
