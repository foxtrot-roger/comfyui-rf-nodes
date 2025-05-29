class RF_ToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("INT,BOOL,FLOAT,NUMBER", {
                    "forceInput": True,
                    "step": 0.00001,
                    "round": False,
                }),
                "precision": ("INT", {
                    "default": 2,
                }),
            },
        }

    DISPLAY_NAME = "To string (ANY)"
    CATEGORY = "RF/toString"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value, precision):
        print(type(value))
        if isinstance(value, float):
            result = f"{value:.{precision}f}"
        else:
            result = str(value)
        return (result,)
