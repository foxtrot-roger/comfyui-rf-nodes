class RF_FloatToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("FLOAT", {
                    "forceInput": True,
                    "step": 0.00001,
                    "round": False,
                }),
                "precision": ("INT", {
                    "default": 2,
                }),
            },
        }

    DISPLAY_NAME = "To string (FLOAT)"
    CATEGORY = "RF/toString"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, precision):
        print(type(value))
        result = result = f"{value:.{precision}f}"
        return (result,)
