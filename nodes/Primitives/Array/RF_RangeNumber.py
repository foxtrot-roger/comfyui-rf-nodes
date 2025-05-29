class RF_RangeNumber:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start": ("NUMBER", { "default": 0 }),
                "step": ("NUMBER", { "default": 1 }),
                "count": ("NUMBER", { "default": 10 }),
            },
        }

    DISPLAY_NAME = "Repeat (NUMBER)"
    CATEGORY = "RF/primitives/array"

    RETURN_NAMES = ("values",)
    RETURN_TYPES = ("NUMBER",)
    OUTPUT_IS_LIST =(True,)

    def VALIDATE_INPUTS(step):
        if step == 0:
            return "Value cannot be 0."
        return True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, start, step, count):
        return (range(start, start + count * step, step), )
