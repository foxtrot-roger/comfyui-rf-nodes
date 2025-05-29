class RF_NumberToString:
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
        }

    DISPLAY_NAME = "To string (NUMBER)"
    CATEGORY = "RF/toString"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        print(type(value))
        result = str(value)
        return (result,)
