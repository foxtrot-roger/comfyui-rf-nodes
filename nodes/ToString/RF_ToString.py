class RF_ToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("INT,BOOL,FLOAT,NUMBER", {
                    "forceInput": True,
                }),
            },
        }

    DISPLAY_NAME = "To string (ANY)"
    CATEGORY = "RF"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        result = str(value)
        return (result,)

