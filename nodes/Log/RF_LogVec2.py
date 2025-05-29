from .LogToConsole import LogToConsole

class RF_LogVec2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("VEC2", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (VEC2)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("VEC2",)
    RETURN_NAMES = ("VEC2",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(prefix, value)
        return (value,)
