class RF_BoolToString:
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
        }

    DISPLAY_NAME = "To string (BOOL)"
    CATEGORY = "RF/toString"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        print(type(value))
        result = str(value)
        return (result,)
