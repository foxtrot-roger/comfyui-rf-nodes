from .LogToConsole import LogToConsole

class RF_LogInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("INT", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (INT)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(prefix, value)
        return (value,)
