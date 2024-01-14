class RF_IntToString:
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
        }

    DISPLAY_NAME = "To string (INT)"
    CATEGORY = "RF"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        result = str(value)
        return (result,)