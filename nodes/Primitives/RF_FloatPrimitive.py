class RF_FloatPrimitive:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("FLOAT", {
                    "forceInput": False,
                    "default": 1.0,
                    "step": 0.00001,
                    "round": False,
                    "display": "number",
                })
            },
        }

    DISPLAY_NAME = "Float Primitive"
    CATEGORY = "RF/primitives"

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        return (value,)
