class RF_FloatToString:
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
        }

    DISPLAY_NAME = "To string (FLOAT)"
    CATEGORY = "RF"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        result = str(value)
        return (result,)