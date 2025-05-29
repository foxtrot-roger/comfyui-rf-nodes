from .LogToConsole import LogToConsole

class RF_LogVec3:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("VEC3", {
                    "forceInput": True,
                }),
            },
            "optional": {
                "prefix": ("STRING", { "multiline": True, "default": "Value:" })
            }
        }

    DISPLAY_NAME = "Log (VEC3)"
    CATEGORY = "RF/logging"

    RETURN_TYPES = ("VEC3",)
    RETURN_NAMES = ("VEC3",)
    OUTPUT_NODE = True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, prefix):
        LogToConsole(prefix, value)
        return (value,)
