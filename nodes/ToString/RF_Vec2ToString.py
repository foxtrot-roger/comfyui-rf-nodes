class RF_Vec2ToString:
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
        }

    DISPLAY_NAME = "To string (VEC2)"
    CATEGORY = "RF"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        result = str(value)
        return (result,)