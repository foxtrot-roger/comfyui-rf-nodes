class RF_RangeFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start": ("FLOAT", { "default": 0 }),
                "step": ("FLOAT", { "default": 1 }),
                "count": ("FLOAT", { "default": 10 }),
            },
        }

    DISPLAY_NAME = "Repeat (FLOAT)"
    CATEGORY = "RF/primitives/array"

    RETURN_NAMES = ("values",)
    RETURN_TYPES = ("FLOAT",)
    OUTPUT_IS_LIST =(True,)

    def VALIDATE_INPUTS(step):
        if step == 0:
            return "Value cannot be 0."
        return True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, start, step, count):
        return (range(start, start + count * step, step), )
